import os
import requests
import lxml
import smtplib
from bs4 import BeautifulSoup
from dotenv import load_dotenv


load_dotenv()

url = 'https://smile.amazon.com/Programmers-Rubber-Computer-Coding-T-Shirt/dp/B081BMKV8D/ref=sr_1_3?dchild=1&keywords' \
      '=coding+duck&qid=1616679838&sr=8-3 '

headers = {
    'User-Agent': os.environ.get('USER_AGENT'),
    'Accept-Language': os.environ.get('LANGUAGE')
}

my_email = os.environ.get('MY_EMAIL')
password = os.environ.get('EMAIL_PASS')

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.content, 'lxml')


price = soup.find(id="priceblock_ourprice").get_text()
price_wo_currency = price.split('$')[1]
price_float = float(price_wo_currency)
print(price_float)

if price_float < 13:
    with smtplib.SMTP('smtp.gmail.com', 507) as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=f'Shirt on Sale for {price_float}\n\n {url}')