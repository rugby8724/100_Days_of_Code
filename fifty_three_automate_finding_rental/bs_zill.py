import os
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()
URL = os.environ.get('APT_URL')
HEADERS = {
    'User-Agent': os.environ.get('USER_AGENT'),
    'Accept-Language': os.environ.get('LANGUAGE')
}


class Zillow:
    def __init__(self):
        self.apt_links = []
        self.apt_prices = []
        self.apt_addresses = []
        response = requests.get(URL, headers=HEADERS)
        apt_web = response.text
        self.soup = BeautifulSoup(apt_web, 'html.parser')
        self.a_links()
        self.a_prices()
        self.a_address()

    def a_links(self):
        apt_link = self.soup.select('.list-card-link')

        for apt in apt_link:
            a_link = apt.get('href')
            if a_link[0] != 'h':
                a_link = 'https://www.zillow.com' + a_link
            self.apt_links.append(a_link)

    def a_prices(self):
        apt_price = self.soup.select('.list-card-price')

        for apt in apt_price:
            apt = apt.getText()
            if '+' in apt:
                self.apt_prices.append(apt.split('+')[0])
            elif '/' in apt:
                self.apt_prices.append(apt.split('/')[0])
            elif ' ' in apt:
                self.apt_prices.append(apt.split(' ')[0])
            else:
                self.apt_prices.append(apt)

    def a_address(self):
        apt_address = self.soup.select('.list-card-addr')

        for apt in apt_address:
            apt = apt.getText()
            if '|' in apt:
                self.apt_addresses.append(apt.split('| ')[1])
            else:
                self.apt_addresses.append(apt)
