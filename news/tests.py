from django.test import TestCase
from news.models import FinancialOrganization, FinancialOrganizationNews
from news.tasks import fetch_news_for_organizations

class FinancialOrganizationModelTest(TestCase):
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
    
    def test_financial_organization_creation(self):
        # Проверяем, что организация создается с правильными данными
        self.assertEqual(self.org.name, "Test Bank")
        self.assertEqual(self.org.status, "Active")

    def test_news_creation(self):
        # coздаем новость и проверяем связь с организацией
        news = FinancialOrganizationNews.objects.create(
            organization=self.org,
            title="Test News",
            description="This is a test news description.",
            source_url="http://example.com",
            published_date="2023-01-02"
        )
        self.assertEqual(news.organization, self.org)
        self.assertEqual(news.title, "Test News")
        self.assertEqual(news.source_url, "http://example.com")


class NewsTaskTest(TestCase):
    def setUp(self):
        # Создаем тестовую организацию
        self.org = FinancialOrganization.objects.create(
            name="Kaspi Bank",
            address="123 Test St",
            status="Active",
            phone="+123456789",
            license_number="12345",
            registration_date="2023-01-01",
            bin_iin="123456789012"
        )
    
    def test_fetch_news_task(self):
        try:
            result = fetch_news_for_organizations()
            self.assertIsNone(result)  # Задача не возвращает значения, проверяем, что исключений нет
        except Exception as e:
            self.fail(f"fetch_news_for_organizations вызвала исключение: {e}")
