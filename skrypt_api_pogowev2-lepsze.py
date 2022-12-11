import os
from json import loads
import requests

pogoda = requests.get('https://danepubliczne.imgw.pl/api/data/synop')

response = pogoda.json()

wybor = str.capitalize(input("Podaj MIASTO!   "))

for wynik in response:
    if wynik['stacja'] == wybor :
        print(wynik)