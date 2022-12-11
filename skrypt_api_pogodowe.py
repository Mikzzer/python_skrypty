import os 
from requests import get
from json import loads

wybor2 = ['Warszawa']


def main():
    url = 'https://danepubliczne.imgw.pl/api/data/synop'
    response = (get(url))
    rows = ['Miasto', 'Temperatura', 'Godzina pomiaru']

    for row in loads(response.text):
        if row['stacja'] in wybor2:
             print(row)

if __name__ == '__main__':
        main()

             
