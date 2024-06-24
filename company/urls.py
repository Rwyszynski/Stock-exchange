from django.contrib import admin
from django.urls import path
from company.views import test_response

urlpatterns = [
    path('test/', test_response),
]
