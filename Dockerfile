FROM python:3.9-slim

# Установим рабочую директорию
WORKDIR /app
# Установим зависимости системы
RUN apt-get update && apt-get install -y gcc libpq-dev && rm -rf /var/lib/apt/lists/*
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
# Скопируем все файлы проекта в контейнер
COPY . /app/
# Установим статические файлы
RUN mkdir -p /app/staticfiles
RUN python manage.py collectstatic --noinput
# Открываем порт для приложения
EXPOSE 8000
# Команда для запуска сервера
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "config.wsgi:application"]
