from django.contrib import admin
from django.urls import path
from company.views import show, login_view


urlpatterns = [
    path('show/', show, name='show'),

]
