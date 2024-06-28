
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


def diagram(request):
    # nazwa tickera papieru wartościowego (CDR = CD Projekt SA)
    TICKER = "CDR"
    # data początkowa
    START_DATE = "2024-05-24"
    # data końcowa
    END_DATE = "2024-06-24"
    # plik w którym będą przechowywane archiwalne notowania dla danego tickera
    FILENAME = "data.txt"

    url = "https://stooq.pl/q/d/l/?s={0}&d1={1}&d2={2}&i=d".format(
        TICKER, START_DATE.replace("-", ""), END_DATE.replace("-", ""))
    wget.download(url, FILENAME)

    data_frame = pd.read_csv(FILENAME, index_col='Data',
                             parse_dates=True, usecols=['Data', 'Zamkniecie'],
                             na_values='nan')
    # rename the column header with ticker
    data_frame = data_frame.rename(columns={'Zamkniecie': TICKER})
    data_frame.dropna(inplace=True)
    print(data_frame)
