from django.test import TestCase
from django.urls import reverse
from organizations.models import FinancialOrganization

class OrganizationViewTest(TestCase):
    def setUp(self):
        # Создаем тестовую организацию
        self.org = FinancialOrganization.objects.create(
            name="Test Bank",
            address="123 Test St",
            status="Active",
            phone="+123456789",
            license_number="12345",
            registration_date="2023-01-01",
            bin_iin="123456789012"
        )

    def test_index_view(self):
        # Проверяем, что страница доступна
        response = self.client.get(reverse('organizations:index'))
        self.assertEqual(response.status_code, 200)
        # Проверяем, что "Test Bank" отображается в шаблоне
        self.assertContains(response, "Test Bank")
