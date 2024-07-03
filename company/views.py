
from django.shortcuts import render
from django.http import HttpResponse
import json
from django.contrib.auth.middleware import AuthenticationMiddleware
from django.http import JsonResponse
import requests
import pandas as pd
import wget
import matplotlib
import os
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from StockExhange.settings import *
from django.shortcuts import redirect


def show(request):

    response = requests.get(
        'https://financialmodelingprep.com/api/v3/symbol/WSE?apikey=1naOu5k2WMCBylHjrlsRplGrDXNdSsqt').json()

    return render(request, 'index.html', {'response': response})
    # return JsonResponse({'url': url})


def login_view(request):
    atr = 'registration/login.html'
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return render(request, 'logged.html', {"form": form})
    else:
        form = AuthenticationForm()

    return render(request, atr, {"form": form})
