import os
import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv

load_dotenv()
url = 'https://tinder.com/'
chrome_driver_path = os.environ.get('CHROME_DRIVER')

driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(url)


def random_num(num1, num2):
    num = random.randint(num1, num2)
    return num


t_login = driver.find_element_by_xpath(
    '//*[@id="t--771258051"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/button')
t_login.click()
time.sleep(3)
fb_login = driver.find_element_by_xpath('//*[@id="t-1483503441"]/div/div/div[1]/div/div[3]/span/div[2]/button')
fb_login.click()
# time.sleep(1)
# fb_name = driver.find_element_by_name('email')
# fb_name.send_keys('testing')