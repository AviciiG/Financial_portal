import logging
import requests
from celery import shared_task
from django.core.cache import cache
from organizations.models import FinancialOrganization
from news.models import FinancialOrganizationNews

# Настройка логирования
logger = logging.getLogger(__name__)

NEWSAPI_URL = 'https://newsapi.org/v2/everything'
NEWSDATA_API_URL = 'https://newsdata.io/api/1/news'


def fetch_from_newsapi(org_name):
    """Получить новости из NewsAPI.org."""
    try:
        response = requests.get(
            NEWSAPI_URL,
            params={
                'q': f'"{org_name}"',
                'apiKey': '639e289f339044ef83ad2b0992e09e99',
                'language': 'ru',
                'sortBy': 'publishedAt',
                'pageSize': 5,
            },
        )
        response.raise_for_status()
        return response.json().get('articles', [])
    except requests.RequestException as e:
        logger.error(f"Ошибка при запросе к NewsAPI для {org_name}: {e}")
        return []


def fetch_from_newsdata(org_name):
    """Получить новости из NewsData.io."""
    try:
        response = requests.get(
            NEWSDATA_API_URL,
            params={
                'q': org_name,
                'apikey': 'pub_668760612571052c90029e5d4f2a333e74165',
                'language': 'ru',
                'country': 'kz',
            },
        )
        response.raise_for_status()
        return response.json().get('results', [])
    except requests.RequestException as e:
        logger.error(f"Ошибка при запросе к NewsData для {org_name}: {e}")
        return []

logger = logging.getLogger(__name__)
@shared_task
def fetch_news_for_organizations():
    """Фоновая задача для получения новостей с логированием."""
    logger.info("Запущено обновление новостей для организаций.")
    organizations = FinancialOrganization.objects.all()

    for org in organizations:
        logger.info(f"Обновление новостей для организации: {org.name}")
        try:
            cache_key = f"news_{org.id}"
            if cache.get(cache_key):
                logger.info(f"Пропущена организация {org.name}: данные есть в кеше.")
                continue

            all_articles = []
            logger.info(f"Успешно обновлено новостей для {org.name}: {len(all_articles)}")

            # Получение новостей из newsapi.org
            newsapi_articles = fetch_from_newsapi(org.name)
            for article in newsapi_articles:
                all_articles.append({
                    'title': article['title'],
                    'description': article['description'][:500],
                    'source_url': article['url'],
                    'published_date': article['publishedAt'],
                })

            # Получение новостей из newsdata.io
            newsdata_articles = fetch_from_newsdata(org.name)
            for article in newsdata_articles:
                all_articles.append({
                    'title': article['title'],
                    'description': article.get('description', '')[:500],
                    'source_url': article['link'],
                    'published_date': article['pubDate'],
                })

            # Сохранение новостей
            for article in all_articles:
                FinancialOrganizationNews.objects.update_or_create(
                    organization=org,
                    title=article['title'],
                    defaults={
                        'description': article['description'],
                        'source_url': article['source_url'],
                        'published_date': article['published_date'],
                    },
                )
            logger.info(f"Обновление новостей завершено для организации {org.name}.")

            # Кеширование на 1 час
            cache.set(cache_key, True, timeout=3600)
        except Exception as e:
            logger.error(f"Ошибка при обработке организации {org.name}: {e}")

    logger.info("Обновление новостей завершено.")
