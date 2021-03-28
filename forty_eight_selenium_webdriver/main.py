import os
from selenium import webdriver
from dotenv import load_dotenv

load_dotenv()

url = 'https://www.python.org/'
chrome_driver_path = os.environ.get('CHROME_DRIVER')

driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(url)

# price = driver.find_element_by_id('priceblock_ourprice')
# print(price.text)

# search_bar = driver.find_element_by_name('q')
# print(search_bar.get_attribute('placeholder'))

# logo = driver.find_element_by_class_name('python-logo')
# print(logo.size)

# doc_link = driver.find_elements_by_css_selector('#documentation a')
# print(doc_link)

# bug_link = driver.find_element_by_xpath('//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)





driver.quit()