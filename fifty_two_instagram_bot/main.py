import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
from dotenv import load_dotenv

load_dotenv()
CHROME_DRIVER_PATH = os.environ.get('CHROME_DRIVER')
SIMILAR_ACCOUNT = 'pycoders'
INSTA_USER = os.environ.get('INSTA_EMAIL')
INSTA_PASS = os.environ.get('INSTA_PASS')


class InstaFollower:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

    def login(self):
        url='https://www.instagram.com/accounts/login/'
        self.driver.get(url)
        time.sleep(5)
        inst_login = self.driver.find_element_by_name('username')
        inst_login.send_keys(INSTA_USER)
        inst_pass = self.driver.find_element_by_name('password')
        inst_pass.send_keys(INSTA_PASS)
        time.sleep(2)
        inst_pass.send_keys(Keys.ENTER)
        time.sleep(2)
        inst_skip = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
        inst_skip.click()
        time.sleep(2)
        no_noti = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
        no_noti.click()


    def find_follwers(self):
        time.sleep(3)
        self.driver.get(f'https://www.instagram.com/{SIMILAR_ACCOUNT}/followers/')
        time.sleep(2)
        followers = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers.click()
        time.sleep(2)
        modal = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        all_buttons = self.driver.find_elements_by_css_selector("li button")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()


inst_bot = InstaFollower(CHROME_DRIVER_PATH)
inst_bot.login()
inst_bot.find_follwers()
inst_bot.follow()
