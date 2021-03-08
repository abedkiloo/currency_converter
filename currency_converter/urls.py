from django.urls import path

from currency_converter.views import CurrencyConverter

urlpatterns = [
    path('currency_converter/', CurrencyConverter.as_view(), name='currency_converter'),
]
