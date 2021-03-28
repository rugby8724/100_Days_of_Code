import os
import time
from selenium import webdriver
from dotenv import load_dotenv
load_dotenv()
url = 'https://www.linkedin.com/jobs/search/?f_AL=true&f_E=2&keywords=python%20developer'
chrome_driver_path = os.environ.get('CHROME_DRIVER')

driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(url)

entrance = driver.find_element_by_link_text('Sign in')
entrance.click()

time.sleep(5)

li_un = driver.find_element_by_id('username')
li_un.send_keys(os.environ.get('LIN_UN'))

li_wd = driver.find_element_by_id('password')
li_wd.send_keys(os.environ.get('LIN_WD'))

get_in = driver.find_element_by_css_selector('.login__form_action_container button')
get_in.click()
