from django.urls import path
from .views import financial_organizations_view

urlpatterns = [
    path('', financial_organizations_view, name='financial_organizations'),
]
