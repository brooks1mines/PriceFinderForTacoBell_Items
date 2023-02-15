import requests
import json
from time import sleep
import decimal
import time

TACO_BELL_URL = 'https://www.tacobell.com/'

file = open('stores.txt', 'w')

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
    'Origin': 'https://www.tacobell.com',
    'Connection': 'keep-alive',
    'Referer': 'https://www.tacobell.com',
    'TE': 'Trailers'
}

def prange(x, y, jump):
  while x < y:
    yield float(x)
    x += decimal.Decimal(jump)

def nrange(x, y, jump):
  while x > y:
    yield float(x)
    x += decimal.Decimal(jump)
     

def find_store(latitude: str, longitude: str):
        """
        Find the nearest stores
        """

        # Request payload for finding stores
        location = {
            'latitude': latitude,
            'longitude': longitude
        }
        
        # Make GET call to find nearest stores
        response = requests.get(
            TACO_BELL_URL + f'store-finder/findStores',
            headers=HEADERS,
            params=location
        )

        if response.status_code != 200:
            return None
        
        stores_data = json.loads(response.text)

        return_data = []
        for store in stores_data.get('nearByStores', []):
            yield (store['formattedDistance'], store['storeNumber'])
        

lats = list(prange(25,50,'0.142857'))
#lats = [45,46,47]
#progress = [25,25.1]
longs = list(nrange(-66,-125,'-0.1667'))   
#longs = [-99,-100,-101]

#lats = [39.4,39.5,39.6]
#longs = [-104.9,-105,-105.1]

timer = []
stores = []
for i in lats:
    if i in timer:
        continue
    else:
        print(i)
        timer.append(i)
    for j in longs:
        for k in find_store(latitude=i, longitude=j):            
            if k is type(None):
                continue
            else:    
                stores.append(k[1])          
set_stores = list(set(stores))
for store in set_stores:
    file.write(store + '\n')


# succesfully retrieved full store list by scraping the taco bell website in a grid.
