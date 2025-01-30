from django.db import models
from organizations.models import FinancialOrganization

class FinancialOrganizationNews(models.Model):
    organization = models.ForeignKey(
        FinancialOrganization,
        on_delete=models.CASCADE,
        related_name='news',
        verbose_name="Организация"
    )
    title = models.CharField(max_length=500, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание")
    published_date = models.DateTimeField(verbose_name="Дата публикации")
    source_url = models.URLField(max_length=1000, verbose_name="Ссылка на источник")

    def __str__(self):
        return self.title


