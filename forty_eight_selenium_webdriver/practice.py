import os
from selenium import webdriver
from dotenv import load_dotenv

load_dotenv()

event_info = {}

url = 'https://www.python.org/'
chrome_driver_path = os.environ.get('CHROME_DRIVER')

driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(url)

event_dates = driver.find_elements_by_css_selector('.last .shrubbery .menu li time')


event_names = driver.find_elements_by_css_selector('.last .shrubbery .menu li a')


for i in range(0, 4):
    event_info[i] = {'time': event_dates[i].text, 'event': event_names[i].text}


print(event_info)
driver.quit()