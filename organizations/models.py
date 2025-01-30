from django.db import models

class FinancialOrganization(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    address = models.TextField(verbose_name="Адрес", null=True, blank=True)
    status = models.CharField(max_length=100, verbose_name="Статус", null=True, blank=True)
    phone = models.CharField(max_length=20, verbose_name="Телефон", null=True, blank=True)
    license_number = models.CharField(max_length=100, verbose_name="Номер лицензии", null=True, blank=True)
    registration_date = models.DateField(verbose_name="Дата регистрации", null=True, blank=True)
    bin_iin = models.CharField(max_length=12, verbose_name="БИН/ИИН", null=True, blank=True)
    logo = models.ImageField(upload_to='organization_logos/', null=True, blank=True, verbose_name="Логотип")
    email = models.EmailField(verbose_name="Email", null=True, blank=True) 
    website = models.URLField(verbose_name="Веб-сайт", null=True, blank=True)

    def __str__(self):
        return self.name


