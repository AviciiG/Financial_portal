from organizations.models import FinancialOrganization

def add_financial_organizations():
    organizations = [
        {
            "name": "Kaspi Bank",
            "address": "050013, Almaty, Nauryzbay Batyr str., 154",
            "email": "office@kaspibank.kz",
            "phone": "+7 (727) 258 59 55",
            "website": "https://kaspi.kz"
        },
        {
            "name": "Home Credit Bank",
            "address": "050059, Almaty, N.Nazarbayev Avenue, 248",
            "email": "info@homecredit.kz",
            "phone": "+7 (727) 244 54 84",
            "website": "https://homecredit.kz"
        },
        {
            "name": "ForteBank",
            "address": "City Astana, Dostyk str., 8/1",
            "email": "info@fortebank.kz",
            "phone": "+7 (727) 258 75 75",
            "website": "www.fortebank.com"
        },
        {
            "name": "Bank RBK",
            "address": "A15X3C7, city Almaty, Republic Square Street, house №15",
            "email": "info@bankrbk.kz",
            "phone": "+7 (727) 258 75 75",
            "website": "www.bankrbk.kz"
        }
    ]

    for org_data in organizations:
        FinancialOrganization.objects.get_or_create(**org_data)

    print("Финансовые организации успешно добавлены.")
