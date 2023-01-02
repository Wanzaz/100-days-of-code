import os
import requests
from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

FORM_ADDRESS = "https://forms.gle/HkGZnyUSqaKNoTgx6"
ZILLOW_ADDRESS = "https://www.zillow.com/homes/for_rent/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.94007338476563%2C%22east%22%3A-121.92658461523438%2C%22south%22%3A37.33000071459292%2C%22north%22%3A38.21791625384213%7D%2C%22isMapVisible%22%3Afalse%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D"
IG_ACCOUNT_NAME = os.environ.get("IG_ACCOUNT_NAME")
IG_PASSWORD = os.environ.get("IG_PASSWORD")

req_headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.8',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
}

class HousePricesScraper:
    def __init__(self) -> None:
        self.chrome_options = Options()
        self.chrome_options.add_argument("--incognito")
        # self.chrome_options.add_experimental_option("detach", True) #for interactive testing
        self.s = Service(ChromeDriverManager().install())
        # self.driver = webdriver.Chrome(service=self.s, options=self.chrome_options)
        # self.driver.maximize_window()
        self.links = []
        self.prices = []
        self.address = []

    def scrape_house_info(self):
        """web scraping - BeautifulSoup/Request to scrape all the listings from the Zillow web address"""
        response = requests.get(ZILLOW_ADDRESS, headers=req_headers)
        zillow_web_page = response.text
        soup = BeautifulSoup(zillow_web_page, "html.parser")

        house_links = soup.find_all(class_="property-card-link")
        self.links = [h_link.get("href") for h_link in house_links]
        print(self.links)


    def fill_form(self):
        # Selenium
        pass

housePrices = HousePricesScraper()
housePrices.scrape_house_info()
