import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv

load_dotenv()

url = 'https://en.wikipedia.org/wiki/Main_Page'
chrome_driver_path = os.environ.get('CHROME_DRIVER')

driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(url)

# total_articles = driver.find_element_by_css_selector('#articlecount a')
# total_articles.click()

# all_portals = driver.find_element_by_link_text('All portals')
# all_portals.click()

search = driver.find_element_by_name('search')
search.send_keys('Python')
search.send_keys(Keys.ENTER)
# start_search = driver.find_element_by_name('go')
# start_search.click()

# driver.quit()