import pandas as pd
import wget
import matplotlib


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

# # calculate the standard deviation
# std_dev = data_frame.rolling(window=20).std()
# # calculate Simple Moving Average with 20 days window
# sma = data_frame.rolling(window=20).mean()

# lower_band = sma - 2*std_dev
# lower_band = lower_band.rename(columns={TICKER: "lower band"})


# upper_band = sma + 2*std_dev
# upper_band = upper_band.rename(columns={TICKER: "upper band"})

# data_frame = data_frame.join(upper_band).join(lower_band)
# ax = data_frame.plot(title=TICKER)
# ax.fill_between(data_frame.index, lower_band['lower band'],
#                 upper_band['upper band'], color='#5F9F9F')
# ax.set_xlabel('Date')
# ax.set_ylabel('Price')
# ax.grid()
# plt.show(block=True)
