import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

TWITTER_ACCOUNT_NAME = os.environ.get("TWITTER_ACCOUNT_NAME")
TWITTER_PASSWORD = os.environ.get("TWITTER_PASSWORD")
PROMISED_DOWN = 150
PROMISED_UP = 10
# CHROME_DRIVER_PATH = Service("/Users/ondrejpazourek/Development/chromedriver")
# driver = webdriver.Chrome(service=CHROME_DRIVER_PATH)


class InternetSpeedTwitterBot:

    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        sleep(2)

        cookies_button = self.driver.find_element(By.ID, "onetrust-accept-btn-handler")
        cookies_button.click()
        sleep(1)

        go_button = self.driver.find_element(By.CLASS_NAME, "start-text")
        go_button.click()
        sleep(40)

        self.down = float(self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text)
        self.up = float(self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text)

        print(f"Download = {self.down} Mbps")
        print(f"Upload = {self.up} Mbps")
        sleep(2)
        if self.down < PROMISED_DOWN or self.up < PROMISED_UP:
            # twitter_bot.tweet_at_provider()
            print("Your connectoin sucks!")
        else:
            print("Your connection is good!")

    def tweet_at_provider(self):
        self.driver.get("https://www.twitter.com/")
        sleep(2)






twitter_bot = InternetSpeedTwitterBot()
twitter_bot.get_internet_speed()
