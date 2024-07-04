import wget
import pandas as pd

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
