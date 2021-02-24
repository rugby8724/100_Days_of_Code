import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
from dotenv import load_dotenv
from datetime import datetime, timedelta

load_dotenv()

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

TWILIO_SID = os.environ.get('TWILIO_ACCOUNT_SID')
TWILIO_TOKEN = os.environ.get('TWILIO_AUTH_KEY')

BACK_DAY = 1
BACK_TWO_DAYS = 2

# API Parameters
stock_params = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK,
    'outputsize': 'compact',
    'apikey': os.environ.get('ALPHA_VANTAGE_API_KEY')
}

new_params = {
    'q': 'Tesla',
    'apiKey': os.environ.get('NEWS_API_KEY')
}

# Get API Data
response = requests.get(url='https://www.alphavantage.co/query', params=stock_params)
response.raise_for_status()
data = response.json()
stock_data = data['Time Series (Daily)']

news_response = requests.get(url='https://newsapi.org/v2/top-headlines', params=new_params)
news_response.raise_for_status()
n_data = news_response.json()
news_data = n_data['articles']

today = datetime.today()
day = today.weekday()
if day == 6:
    BACK_DAY += 1
    BACK_TWO_DAYS += 1
if day == 0:
    BACK_DAY += 2
    BACK_TWO_DAYS += 2
if day == 1:
    BACK_TWO_DAYS += 2
yesterday = str(today - timedelta(days=BACK_DAY)).split()[0]
two_days_ago = str(today - timedelta(days=BACK_TWO_DAYS)).split()[0]
yesterday_open = float(stock_data[yesterday]['1. open'])
yesterday_close = float(stock_data[yesterday]['4. close'])
two_days_ago_open = float(stock_data[two_days_ago]['1. open'])
two_days_ago_close = float(stock_data[two_days_ago]['4. close'])


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
if two_days_ago_close * .95 >= yesterday_close or yesterday_close >= two_days_ago_close * 1.05:
    news = []
    for i in range(0, 2):
        headline = news_data[i]['title']
        brief = news_data[i]['description']
        article = {'Headline': headline, 'Brief': brief}
        news.append(article)
        
    proxy_client = TwilioHttpClient()
    proxy_client.session = {'https': os.environ['https_proxy']}
    client = Client(TWILIO_SID, TWILIO_TOKEN, http_client=proxy_client)
    message = client.messages \
        .create(
        body=f'{STOCK}: {percent_change} \n '
             f'Headline: {news[0]["Headline"]} \n Brief: {news[0]["Brief"]} \n'
             f'Headline: {news[1]["Headline"]} \n Brief: {news[1]["Brief"]} \n'
             f'Headline: {news[2]["Headline"]} \n Brief: {news[2]["Brief"]} \n',
        from_='+17738256243',
        to='+17133800777'
    )
    print(message.status)



# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
