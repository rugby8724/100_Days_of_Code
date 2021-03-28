import os
from selenium import webdriver
from dotenv import load_dotenv

load_dotenv()

url = 'http://secure-retreat-92358.herokuapp.com/'
chrome_driver_path = os.environ.get('CHROME_DRIVER')

driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(url)

fname = driver.find_element_by_name('fName')
fname.send_keys('Tad')
lname = driver.find_element_by_name('lName')
lname.send_keys('Pole')
e_mail = driver.find_element_by_name('email')
e_mail.send_keys('tadtesting24@gmail.com')
sub = driver.find_element_by_css_selector('.form-signin button')
sub.click()




