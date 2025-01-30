from django.shortcuts import render
from organizations.models import FinancialOrganization

def financial_organizations_view(request):
    organizations = FinancialOrganization.objects.prefetch_related('news').all()
    return render(request, 'news/organization_news.html', {'organizations': organizations})
