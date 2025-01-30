import requests
import logging
from news.models import FinancialOrganizationNews
from organizations.models import FinancialOrganization

# логирование
logger = logging.getLogger(__name__)

NEWSAPI_KEY = "639e289f339044ef83ad2b0992e09e99"  # API ключ для newsapi.org
NEWSDATA_KEY = "pub_668760612571052c90029e5d4f2a333e74165"  # API ключ для newsdata.io

def fetch_news():
    organizations = FinancialOrganization.objects.all()

    for org in organizations:
        query = org.name

        # Запрос к newsapi
        try:
            response = requests.get(
                "https://newsapi.org/v2/everything",
                params={
                    "q": query,
                    "apiKey": NEWSAPI_KEY,
                    "language": "ru", 
                    "from": "2024-01-01",  # Дата начала
                    "to": "2025-01-28",    
                    "sortBy": "publishedAt",
                    "pageSize": 5,
                },
            )
            response.raise_for_status()  # Вызывает ошибку, если статус не 200
            articles = response.json().get("articles", [])

            if not articles:
                logger.warning(f"⚠️ NewsAPI: нет новостей для {org.name}")

            for article in articles:
                FinancialOrganizationNews.objects.update_or_create(
                    organization=org,
                    title=article["title"],
                    defaults={
                        "description": article["description"] or "Описание отсутствует",
                        "published_date": article["publishedAt"],
                        "source_url": article["url"]
                    }
                )
        except requests.exceptions.RequestException as e:
            logger.error(f"❌ Ошибка запроса к NewsAPI для {org.name}: {e}")

        #Запрос к newsdata
        try:
            response = requests.get(
                "https://newsdata.io/api/1/news",
                params={
                    "apikey": NEWSDATA_KEY,
                    "q": query,
                    "from": "2024-01-01",  
                    "to": "2025-01-28", 
                    "language": "ru,en", 
                    "country": "kz", 
                },
            )
            response.raise_for_status()
            articles = response.json().get("results", [])

            if not articles:
                logger.warning(f"⚠️ NewsData: нет новостей для {org.name}")

            for article in articles:
                FinancialOrganizationNews.objects.update_or_create(
                    organization=org,
                    title=article["title"],
                    defaults={
                        "description": article.get("description", "Описание отсутствует"),
                        "published_date": article["pubDate"],
                        "source_url": article["link"]
                    }
                )
        except requests.exceptions.RequestException as e:
            logger.error(f"❌ Ошибка запроса к NewsData для {org.name}: {e}")

    logger.info("✅ Все новости успешно обновлены.")
