import time
import threading
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = "/Users/ondrejpazourek/Development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("http://orteil.dashnet.org/experiments/cookie/")


def checking_for_upgrades():
    """Looks for the most expesive feature available every five seconds"""

    cookie_amount = int(driver.find_element(By.ID, "money").text.replace(",", ""))
    # store = driver.find_element(By.ID, "store")
    store_elements = driver.find_elements(By.TAG_NAME, "b")
    prices = []
    for element in store_elements[10:18]:
        price_statement = element.text.split()
        price = element.text.split()[len(price_statement) - 1]
        price_trimmed = int(price.replace(",", ""))
        prices.append(price_trimmed)

    i = 0
    max_price = 0
    for price in prices:
        i += 1
        if price > max_price and price < cookie_amount:
            max_price = i

    store_elements = ["buyCursor", "buyGrandma", "buyFactory", "buyMine", "buyShipment", "buyAlchemy lab", "buyPortal", "buyTime machine"]

    upgrade_to_buy = driver.find_element(By.ID, store_elements[max_price - 1])

    upgrade_to_buy.click()


    threading.Timer(5.0, checking_for_upgrades).start()


timeout = time.time() + 1*60   # 1 minutes from now

checking_for_upgrades()

cookie = driver.find_element(By.ID, "cookie")

while True:
    test = 0
    if test == 5 or time.time() > timeout:
        cps = driver.find_element(By.ID, "cps").text
        print(f"Cookies per second after 1 minute:\n {cps}")
        break

    test -= 1

    cookie.click()



driver.quit()
