from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.conf import settings
from django.conf.urls.static import static

# Главная страница
def home_view(request):
    return HttpResponse("<h1>Добро пожаловать на финансовый портал!</h1>")

urlpatterns = [
    path('admin/', admin.site.urls),  # Админ-панель
    path('news/', include('news.urls')),  # Подключаем маршруты приложения `news`
    path('', home_view, name='home'),  # Главная страница
    path('organizations/', include('organizations.urls', namespace='organizations')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
