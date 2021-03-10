import requests
import os
from dotenv import load_dotenv



load_dotenv()

TEQUILA_ENDPOINT = 'https://tequila-api.kiwi.com/v2/search'
TEQUILA_API = os.environ.get('TEQUILA_API_KEY')


class FlightData:
    def __init__(self, price, origin_city, origin_airport, destination_city, destination_airport, out_date, return_date):
        self.price = price
        self.origin_city = origin_city
        self.origin_airport = origin_airport
        self.destination_city = destination_city
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date