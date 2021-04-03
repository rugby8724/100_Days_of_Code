import os
import time
from selenium import webdriver
from dotenv import load_dotenv
from bs_zill import Zillow

load_dotenv()

apt = Zillow()
rental_form = os.environ.get('RENTAL_FORM')
chrome_driver_path = os.environ.get('CHROME_DRIVER')
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(rental_form)

for i in range(len(apt.apt_prices)):
    time.sleep(5)
    address = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div['
                                           '1]/div/div[1]/input')
    address.send_keys(apt.apt_addresses[i])
    price = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div['
                                         '1]/div/div[1]/input')
    price.send_keys(apt.apt_prices[i])
    link = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div['
                                        '1]/div/div[1]/input')
    link.send_keys(apt.apt_links[i])
    time.sleep(2)
    send_info = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span')
    send_info.click()
    time.sleep(2)
    next_apt = driver.find_element_by_link_text('Submit another response')
    next_apt.click()






