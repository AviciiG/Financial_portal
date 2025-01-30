from django.shortcuts import render
from .models import FinancialOrganization

def index(request):
    """ Представление для отображения списка финансовых организаций. """
    organizations = FinancialOrganization.objects.all()
    return render(request, 'organizations/index.html', {'organizations': organizations})
