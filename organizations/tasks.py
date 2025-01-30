from celery import shared_task
import requests
from .models import FinancialOrganization
from news.models import FinancialOrganizationNews


@shared_task
def update_news():
    api_key = "639e289f339044ef83ad2b0992e09e99"
    base_url = "https://newsapi.org/v2/everything"

    organizations = FinancialOrganization.objects.all()
    for org in organizations:
        query = org.name
        params = {
            'q': query,
            'apiKey': api_key,
            'language': 'ru,en',
            'country': 'kz',

        }
        response = requests.get(base_url, params=params)
        if response.status_code == 200:
            news_data = response.json().get('articles', [])
            for article in news_data:
                FinancialOrganizationNews.objects.update_or_create(
                    organization=org,
                    title=article['title'],
                    defaults={
                        'description': article['description'],
                        'published_date': article['publishedAt'],
                        'source_url': article['url']
                    }
                )
        else:
            print(f"Ошибка при получении новостей для {org.name}: {response.status_code}")
