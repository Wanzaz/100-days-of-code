# Automated Tinder Swiper
# UNDONE PROJECT - I HAD PROBLEM TO CLICK ON THE ANY BUTTON ON TINDER.COM SO I SKIPPED THIS TASK

import os
import time
# import threading
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait      
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import NoSuchElementException

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

TINDER_EMAIL = "wanzaz.contact@gmail.com"
LINKEDIN_PASSWORD = os.environ.get("LINKEDIN_WANZAZ_PASSWORD")

chrome_driver_path = "/Users/ondrejpazourek/Development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://tinder.onelink.me/9K8a/3d4abb81")

time.sleep(2)

# cookies_button = driver.find_element(By.XPATH, '//*[@id="s-662773879"]/div/div[2]/div/div/div[1]/div[2]/button/div[2]/div[2]')
# cookies_button.click()
# log_in_with_facebook_button = driver.find_element(By.ID, "facebook-jssdk-en-GB")
log_in_with_facebook_button = driver.find_element(By.XPATH, '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/header/div[1]/div[2]/div/button')
log_in_with_facebook_button.click()
# print(log_in_with_facebook_button)
# log_in_with_facebook_button.click()

# Wait for the next page to load.
time.sleep(3)

# enter_email = driver.find_element(By.ID, "username").send_keys(LINKEDIN_EMAIL)
# enter_password = driver.find_element(By.ID, "password").send_keys(LINKEDIN_PASSWORD)
# sing_up_button = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')
# sing_up_button.click()

# # Saving jobs
# jobs = driver.find_elements(By.CSS_SELECTOR, ".job-card-list__insight")
# save_button = driver.find_element(By.XPATH, '//*[@id="main"]/div/section[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/div[3]/div/button')

# for job in jobs:
#     WebDriverWait(driver, 20).until(EC.element_to_be_clickable(job)).click()
#     WebDriverWait(driver, 20).until(EC.element_to_be_clickable(save_button)).click()

driver.quit()
