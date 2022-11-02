import time
import threading
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys


chrome_driver_path = "/Users/ondrejpazourek/Development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, "cookie")
cookie_amount = driver.find_element(By.ID, "money").text
cps = driver.find_element(By.ID, "cps")

# def checking_for_upgrades():
#     """Looks for the most expesive feature available every five seconds"""
#     cookie_amount = driver.find_element(By.ID, "money").text
#     store = driver.find_element(By.ID, "store")
#     store_elements = driver.find_elements(By.TAG_NAME, "b")
#     for element in store_elements[11:18]:
#         price_statement = element.text.split()
#         price = element.text.split()[len(price_statement) - 1]
#         price_trimmed = int(price.replace(",", ""))
#         print(price_trimmed)
#     # if 

#     threading.Timer(5.0, checking_for_upgrades).start()


timeout = time.time() + 5*60   # 5 minutes from now

# checking_for_upgrades()
while True:
    test = 0
    if test == 5 or time.time() > timeout:
        break

    test -= 1

    cookie.click()




# driver.close()
driver.quit()
