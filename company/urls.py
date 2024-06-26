from django.contrib import admin
from django.urls import path
from company.views import show


urlpatterns = [
    path('show/', show, name='show'),
]
