import os
import time
from selenium import webdriver
from dotenv import load_dotenv

load_dotenv()

PROMISED_DOWN = 150
PROMISED_UP = 10
CHROME_DRIVER_PATH = os.environ.get('CHROME_DRIVER')
TWITTER_EMAIL = os.environ.get('TWIT_USER')
TWITTER_PASSWORD = os.environ.get('TWIT_PASS')


class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        url='https://www.speedtest.net/'
        self.driver.get(url)
        time.sleep(7)
        start_test = self.driver.find_element_by_class_name('start-text')
        start_test.click()
        time.sleep(90)
        close_not = self.driver.find_element_by_link_text('Back to test results')
        close_not.click()
        time.sleep(2)
        self.down = self.driver.find_element_by_class_name('download-speed').text
        self.up = self.driver.find_element_by_class_name('upload-speed').text

    def tweet_at_provider(self):
        url='https://twitter.com/'
        self.driver.get(url)
        time.sleep(3)
        twit_login = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div/div['
                                                       '1]/div/div[3]/a[2]/div/span/span')
        twit_login.click()
        time.sleep(3)
        twit_user = self.driver.find_element_by_name('session[username_or_email]')
        twit_user.send_keys(os.environ.get('TWIT_USER'))
        twit_pass = self.driver.find_element_by_name('session[password]')
        twit_pass.send_keys(os.environ.get('TWIT_PASS'))
        twit_enter = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div['
                                                       '2]/form/div/div[3]/div/div/span/span')
        twit_enter.click()
        time.sleep(3)
        tweeter = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div['
                                                    '1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div['
                                                    '1]/div/div/div/div/div/div/div/div/div/div['
                                                    '1]/div/div/div/div/div/div/div/div')
        tweeter.send_keys(f'python bot testing download speed:{self.down} upload speed:{self.up}  #100daysofcode day51 #python3 ')
        time.sleep(3)
        send_tweet = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div['
                                                       '1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div['
                                                       '4]/div/div/div[2]/div[3]/div/span/span')
        send_tweet.click()



bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
bot.get_internet_speed()
bot.tweet_at_provider()

# print(bot.up, bot.down)
