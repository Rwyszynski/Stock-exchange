from django.shortcuts import render
import numpy
import requests
import pandas as pd
from matplotlib import pyplot as plt
import io
import base64
import urllib
import numpy as np
from API2 import download


def analyze(request, val=15):
    response = requests.get(download(15, "06N.PL")).json()

    df = pd.DataFrame(
        columns=["ctm", "ctmString", "open", "close", "high", "low", "vol"])
    for i in range(0, len(response["returnData"]["rateInfos"])):
        currentItem = response[i]
        df.loc[i] = [response[i]["ctm"], response[i]["ctmString"], response[i]["open"],
                     response[i]["close"], response[i]["high"], response[i]["low"], response[i]["vol"]]

    date = df['ctmString'].tolist()
    close = df['open'].tolist()
    plt.clf()

    period = date

    # plt.xticks(0, 1)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.style.use('ggplot')

    plt.plot(date, close)

    plt.title("Wykres cenowy spółki")
    plt.xlabel("Data")
    plt.ylabel("Cena")
    plt.grid()
    fig = plt.gcf()
    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    url = urllib.parse.quote(string)

    context = {
        'df': df.head(10).to_html(),
        'y': date,
        's': close,
        'dt': url,
        'period': period

    }
    return render(request, 'analyze.html', context)

    # # nazwa tickera papieru wartościowego (CDR = CD Projekt SA)
    # TICKER = "CDR"
    # # data początkowa
    # START_DATE = "2024-05-24"
    # # data końcowa
    # END_DATE = "2024-06-24"
    # # plik w którym będą przechowywane archiwalne notowania dla danego tickera
    # FILENAME = "data.txt"

    # url = "https://stooq.pl/q/d/l/?s={0}&d1={1}&d2={2}&i=d".format(
    #     TICKER, START_DATE.replace("-", ""), END_DATE.replace("-", ""))
    # wget.download(url, FILENAME)

    # data_frame = pd.read_csv(FILENAME, index_col='Data',
    #                          parse_dates=True, usecols=['Data', 'Zamkniecie'],
    #                          na_values='nan')
    # # rename the column header with ticker
    # data_frame = data_frame.rename(columns={'Zamkniecie': TICKER})
    # data_frame.dropna(inplace=True)
    # print(data_frame)
