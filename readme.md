Финансовый портал 

Проект представляет собой веб-приложение на Django для учета финансовых организаций, с возможностью получения актуальных новостей через API, а также развертыванием в Docker

Функционал проекта:
1) Список финансовых организаций (название, логотип, контакты и т. д.).
2) Автоматическое обновление новостей с помощью Celery и API.
3) Админ-панель Django для управления организациями.
4) Кеширование данных для оптимизации запросов.
5) Запуск через Docker (PostgreSQL, Redis, Celery, Nginx).

Что было использовано в проекте: 
Python 3.9, Django 4.2
PostgreSQL (База данных)
Celery + Redis (Фоновые задачи)
Docker + Docker Compose
Bootstrap (Фронтенд)

Как запустить проект правильно? 

Клонирование проекта: 
git clone https://github.com/AviciiG/financial_portal.git
cd financial_portal


Запуск проекта через Docker:
docker-compose up --build -d

Миграции: 
docker-compose exec web python manage.py migrate

Создание суперпользователя:
docker-compose exec web python manage.py createsuperuser

Celery worker:
docker-compose exec web celery -A config worker --loglevel=info

Celery beat:
docker-compose exec web celery -A config beat --loglevel=info
Новости обновляются каждые 10 минут с помощью Celery.
Можно запустить вручную:
docker-compose exec web python manage.py shell
from news.tasks import fetch_news_for_organizations
fetch_news_for_organizations.delay()

Admin панель доступна:
http://localhost:8000/admin/

Новостной портал с фин организациями:
http://localhost:8000/news/
http://127.0.0.1:8000/news/

Для тестирования: 
docker-compose exec web python manage.py test

просмотр логов:
docker-compose logs web

обновление зависимостей:
docker-compose exec web pip install -r requirements.txt

очистка Docker:
docker-compose down -v




