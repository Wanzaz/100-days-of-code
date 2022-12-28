import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.wait import WebDriverWait

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

TWITTER_ACCOUNT_NAME = os.environ.get("TWITTER_ACCOUNT_NAME")
TWITTER_PASSWORD = os.environ.get("TWITTER_PASSWORD")
PROMISED_DOWN = 150
PROMISED_UP = 10
SPEED_TEST_LINK = "https://www.speedtest.net/"
TWITTER_LINK = "https://www.twitter.com/"
# CHROME_DRIVER_PATH = Service("/Users/ondrejpazourek/Development/chromedriver")
# driver = webdriver.Chrome(service=CHROME_DRIVER_PATH)


class InternetSpeedTwitterBot:

    def __init__(self):
        self.chrome_options = Options()
        self.chrome_options.add_argument("--incognito")
        # self.chrome_options.add_experimental_option("detach", True) #for interactive testing
        self.s = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.s, options=self.chrome_options)
        self.down = None
        self.up = None
        self.driver.maximize_window()

    def measuring_speed(self):
        self.down = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/'
                                             'div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        self.up = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/'
                                           'div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        return self.down, self.up

    def get_internet_speed(self):
        self.driver.get(SPEED_TEST_LINK)
        sleep(2)

        cookies_button = self.driver.find_element(By.ID, "onetrust-accept-btn-handler")
        cookies_button.click()
        sleep(1)

        go_button = self.driver.find_element(By.CLASS_NAME, "start-text")
        go_button.click()
        sleep(15)

        self.down, self.up = self.measuring_speed()

        while self.down == "--" or self.up == "--":
            sleep(2)
            self.down, self.up = self.measuring_speed()

        self.down = float(self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/'
                                                   'div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text)
        self.up = float(self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/'
                                                 'div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text)

        print(f"Download = {self.down} Mbps\nUpload = {self.up} Mbps")
        sleep(2)

        if self.down < PROMISED_DOWN or self.up < PROMISED_UP:
            self.tweet_at_provider()
            print("Your connectoin sucks!")
        else:
            print("Your connection is good!")

    def tweet_at_provider(self):
        self.driver.get(TWITTER_LINK)
        sleep(3)

        login_button = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div[1]/div/div/div/div[2]/div[2]/div/div/div[1]/a')
        login_button.click()
        sleep(5)

        account_name = self.driver.find_element(By.NAME, "text")
        account_name.send_keys(TWITTER_ACCOUNT_NAME)
        sleep(5)

        next_button = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/'
                                               'div[2]/div[2]/div/div/div/div[6]/div')
        next_button.click()
        sleep(5)

        password = self.driver.find_element(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/'
                                            'div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        password.send_keys(TWITTER_PASSWORD)
        sleep(5)

        pass_login = self.driver.find_element(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/'
                                              'div[2]/div[2]/div[2]/div/div[1]/div/div/div/div')
        pass_login.click()
        sleep(5)

        write = self.driver.find_element(By.CSS_SELECTOR, 'br[data-text="true"]')
        sleep(10)
        write.send_keys(f"Hey Internet Provider, why is my internet speed down:{self.down}/up:{self.up} when I pay for 150down/10up!?")
        tweet = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/'
                                                   'div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/'
                                                   'div[3]/div/span/span')
        sleep(10)
        tweet.click()
        sleep(10)

        self.driver.quit()


twitter_bot = InternetSpeedTwitterBot()
twitter_bot.get_internet_speed()
