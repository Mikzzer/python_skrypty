import requests
from json import loads
import os
## losuje 200 piw xd ##
for i in range(200):
    piwo = requests.get('https://random-data-api.com/api/v2/beers')

    response = piwo.json()

    for piwko in piwo:
        print(piwko)
