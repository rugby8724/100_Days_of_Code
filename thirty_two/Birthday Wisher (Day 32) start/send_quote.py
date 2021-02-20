import smtplib
import random
import datetime as dt

now = dt.datetime.now()
day_of_week = now.weekday()

my_email = 'tadtesting24@gmail.com'
password = 'Onehundred100'


def pick_quote():
    with open('quotes.txt') as file:
        all_quotes = file.readlines()
        quote = random.choice(all_quotes)
        return quote


if day_of_week == 6:
    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        quote = pick_quote()
        connection.sendmail(from_addr=my_email, to_addrs='tadtesting24@yahoo.com', msg='Subject:Weekly Quote\n\n '
                            f'{quote}')
