import requests

url = "https://stooq.pl/q/d/l/?s=cdr&d1=20240526&d2=20240626&i=d"


response = requests.get(url)

print(response.json())
