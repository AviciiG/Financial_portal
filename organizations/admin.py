from django.contrib import admin
from .models import FinancialOrganization

@admin.register(FinancialOrganization)
class FinancialOrganizationAdmin(admin.ModelAdmin):
    list_display = ('name', 'bin_iin', 'license_number', 'status', 'address', 'phone', 'email')
    search_fields = ('name', 'bin_iin')
    list_filter = ('status', 'registration_date')
