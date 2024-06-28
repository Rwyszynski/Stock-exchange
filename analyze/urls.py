from django.contrib import admin
from django.urls import path
from analyze.views import analyze


urlpatterns = [
    path('analyze/', analyze, name='analyze'),
]
