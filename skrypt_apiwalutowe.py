import os
from json import loads
import requests

currency = input("Co byś chciał sprzedać? : THB USD AUD HKD CAD NZD SGD EUR HUF CHF GBP UAH JPY CZK DKK ISK NOK SEK HRK RONB GNT RYI LSC LPP HPM XNZ ARB RLM YRI DRI NRK RWC NYX : ")
quantiny  = int(input("Ile byś chciał sprzedać"))

body = requests.get('https://api.nbp.pl/api/exchangerates/tables/A/?format=json')
response = body.json()
for rate in response[0]['rates']:
    print(rate['code'])
    if currency == rate['code']:
     result = quantiny * float(rate['mid'])
     print(f'Otrzymasz : {result} PLN')
     break

   


