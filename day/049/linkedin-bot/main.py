# Automated Job Application LinkedIn Bot

import os
import time
import threading
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

LINKEDIN_EMAIL = "wanzaz.contact@gmail.com"
LINKEDIN_PASSWORD = os.environ.get("LINKEDIN_WANZAZ_PASSWORD")

chrome_driver_path = "/Users/ondrejpazourek/Development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3311660396&f_LF=f_AL&geoId=104508036&keywords=python%20developer&location=Czechia&refresh=true")

# "Save" all the jobs that meet your criteria and follow the company that posted the job.

sign_in_button = driver.find_element(By.XPATH, "/html/body/div[3]/header/nav/div/a[2]")
sign_in_button.click()

# Wait for the next page to load.
time.sleep(5)

enter_email = driver.find_element(By.ID, "username").send_keys(LINKEDIN_EMAIL)
enter_password = driver.find_element(By.ID, "password").send_keys(LINKEDIN_PASSWORD)
sing_up_button = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')
sing_up_button.click()



# driver.quit()
