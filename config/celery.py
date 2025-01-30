from __future__ import absolute_import, unicode_literals
import os
import logging
from celery import Celery
from celery.schedules import crontab

# Настройка логирования
logger = logging.getLogger(__name__)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('financial_portal')

# Настройки из Django settings
app.config_from_object('django.conf:settings', namespace='CELERY')

# Автоматическое обнаружение задач
app.autodiscover_tasks()

# Настройка расписания для Celery Beat
app.conf.beat_schedule = {
    'update-news-every-10-minutes': {
        'task': 'news.tasks.fetch_news_for_organizations',
        'schedule': crontab(minute='*/10'),  # Каждые 10 минут
    },
}

@app.task(bind=True)
def debug_task(self):
    logger.info(f"Запущена задача: {self.request!r}")
