from organizations.models import FinancialOrganization
import favicon
import requests
from django.core.files.base import ContentFile

def fetch_logos():
    organizations = FinancialOrganization.objects.all()
    for org in organizations:
        if org.logo:
            print(f"Логотип для {org.name} уже существует. Пропускаем.")
            continue  # Пропускаем, если логотип уже есть

        query = org.name.replace(" ", "+")
        try:
            # Пытаемся найти фавиконы по названию организации
            icons = favicon.get(f"https://{query}.com")
            
            if not icons:
                print(f"Фавиконы для {org.name} не найдены.")
                continue
            
            # Берем первый фавикон
            icon = icons[0]
            response = requests.get(icon.url)
            
            if response.status_code == 200:
                # Сохраняем фавикон в поле logo
                org.logo.save(f"{org.name}_logo.png", ContentFile(response.content))
                org.save()
                print(f"Логотип для {org.name} успешно сохранен.")
            else:
                print(f"Ошибка загрузки фавикона для {org.name}: {response.status_code}")
        
        except Exception as e:
            print(f"Ошибка при обработке {org.name}: {e}")
