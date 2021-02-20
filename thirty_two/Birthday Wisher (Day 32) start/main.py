# import smtplib
#
# my_email = 'tadtesting24@gmail.com'
# password = 'Onehundred100'
#
# with smtplib.SMTP('smtp.gmail.com', 587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, to_addrs='tadtesting24@yahoo.com', msg='Subject:Testing\n\n Testing Body')

import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
today = now.day

date_of_birth = dt.datetime(year=1995, month=12, day=15)
print(date_of_birth)