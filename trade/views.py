from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from company.views import show
from django import template
import requests


@login_required(login_url="/login/")
def trade(request):

    response = requests.get(
        'https://financialmodelingprep.com/api/v3/symbol/WSE?apikey=1naOu5k2WMCBylHjrlsRplGrDXNdSsqt').json()

    return render(request, "trade.html", {'response': response})
