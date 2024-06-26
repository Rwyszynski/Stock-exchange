
from django.shortcuts import render
from django.http import HttpResponse
import json
from django.contrib.auth.middleware import AuthenticationMiddleware
from django.http import JsonResponse
import requests


def show(request):

    response = requests.get(
        'https://api.twelvedata.com/stocks?country=pl').json()

    return render(request, 'index.html', {'response': response})
    # return JsonResponse({'url': url})
