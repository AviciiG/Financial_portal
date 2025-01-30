import pandas as pd
from organizations.models import FinancialOrganization

def import_organizations_with_pandas(file_path):
    df = pd.read_excel(file_path)

    # Заменяем 'null' и NaN на пустую строку
    df = df.fillna('').replace('null', '')

    for _, row in df.iterrows():
        try:
            FinancialOrganization.objects.get_or_create(
                name=row.get('name', 'Unknown'),
                license_number=row.get('license_number', ''),
                registration_date=row.get('registration_date'),
                status=row.get('status', 'Active'),
                address=row.get('address', ''),
                phone=row.get('phone', ''),
                email=row.get('email', ''),
                website=row.get('website', '')
            )
        except Exception as e:
            print(f"Ошибка при обработке строки: {row}")
            print(e)
