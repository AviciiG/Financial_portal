from django.contrib import admin
from .models import FinancialOrganizationNews

@admin.register(FinancialOrganizationNews)
class FinancialOrganizationNewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'organization', 'published_date')
    search_fields = ('title', 'organization__name')
    list_filter = ('published_date',)
