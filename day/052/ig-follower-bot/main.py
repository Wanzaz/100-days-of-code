import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

IG_ACCOUNT_NAME = os.environ.get("IG_ACCOUNT_NAME")
IG_PASSWORD = os.environ.get("IG_PASSWORD")
SIMILIAR_ACCOUNT = "uscedu"
IG_LOGIN_LINK = "https://www.instagram.com/accounts/login/"
USC_LINK = f"https://www.instagram.com/{SIMILIAR_ACCOUNT}"

class InstaFollower:
    def __init__(self) -> None:
        self.chrome_options = Options()
        self.chrome_options.add_argument("--incognito")
        self.chrome_options.add_experimental_option("detach", True) #for interactive testing
        self.s = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.s, options=self.chrome_options)
        self.driver.maximize_window()

    def login(self):
        self.driver.get(IG_LOGIN_LINK)
        sleep(3)

        cookies_button = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[1]')
        cookies_button.click()
        sleep(3)

        username = self.driver.find_element(By.NAME, "username")
        username.send_keys(IG_ACCOUNT_NAME)
        sleep(3)

        username = self.driver.find_element(By.NAME, "password")
        username.send_keys(IG_PASSWORD)
        sleep(3)

        login_button = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[3]')
        login_button.click()
        sleep(10)

        self.driver.quit()

    def find_followers(self):
        pass

    def follow(self):
        pass

ig_follower = InstaFollower()
ig_follower.login()
ig_follower.find_followers()
ig_follower.follow()
