from django.contrib import admin
from django.urls import path
from trade.views import trade


urlpatterns = [
    path('trade/', trade, name='trade'),
]
