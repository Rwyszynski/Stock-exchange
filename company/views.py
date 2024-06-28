
from django.shortcuts import render
from django.http import HttpResponse
import json
from django.contrib.auth.middleware import AuthenticationMiddleware
from django.http import JsonResponse
import requests
import pandas as pd
import wget
import matplotlib


def show(request):

    response = requests.get(
        'https://financialmodelingprep.com/api/v3/symbol/WSE?apikey=1naOu5k2WMCBylHjrlsRplGrDXNdSsqt').json()

    return render(request, 'index.html', {'response': response})
    # return JsonResponse({'url': url})
