##################### Extra Hard Starting Project ######################
import pandas as pd
import random
import smtplib
import os
import datetime as dt
from dotenv import load_dotenv

my_email = os.environ.get('MY_EMAIL')
password = os.environ.get('EMAIL_PASS')

# 1. Update the birthdays.csv
df = pd.read_csv('birthdays.csv')


# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
month = now.month
day = now.day

bday_df = df.loc[(df['month'] == month) & (df['day'] == day)]
people = bday_df['name'].tolist()
emails = bday_df['email'].tolist()


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

if len(people) > 0:
    for i in range(0, len(people)):
        file = random.choice(os.listdir('./letter_templates'))
        with open(f'./letter_templates/{file}') as letter:
            contents = letter.read()
            new_content = contents.replace('[NAME]', people[i])
        # 4. Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP('smtp.gmail.com', 587) as connection:
            connection.starttls()
            connection.login(my_email, password)
            connection.sendmail(from_addr=my_email, to_addrs=emails[i], msg=f'Subject:Happy Birthday\n\n {new_content}')








