import requests
from sheets import *


class FlightSearch:
    def __init__(self):
        self.teqila_api_key = 'API_KEY'  # Use Tequila API key.
        self.headers = {
            'accept': 'application/json',
            'apikey': 'API_KEY'  # Use Tequila API key.
        }
        self.data = Auth()

    def codes(self):
        cities = self.data.getcities()
        self.code = []
        i = 0
        for cd in cities:
            res = requests.get(
                f'https://api.tequila.kiwi.com/locations/query?term={cities[i]}&locale=en-US&location_types=airport&limit=10&active_only=true', headers=self.headers).json()
            self.code.append(res['locations'][0]['id'])
            i += 1
        self.data.write_code(self.code)
        return self.code

    def search_flight_price(self):
        prices = []
        try:
            for code in self.code:
                res = requests.get(
                    f"https://api.tequila.kiwi.com/v2/search?fly_from=DEL&fly_to={code}&date_from=01%2F04%2F2024&date_to=03%2F10%2F2024&curr=INR&price_from=10000&max_stopovers=2", headers=self.headers)
                prices.append(res.json()['data'][0]['price'])
            self.data.write_price(prices)
        except IndexError:
            pass
