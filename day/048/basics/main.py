from selenium import webdriver
from selenium.webdriver.common.by import By


chrome_driver_path = "/Users/ondrejpazourek/Development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
# print(dir(driver)) printing all driver functions

driver.get("https://www.amazon.com/2022-Apple-MacBook-Laptop-chip/dp/B0B3C5H787/ref=sr_1_1?keywords=macbook+air+m2&qid=1666020223&qu=eyJxc2MiOiIzLjk2IiwicXNhIjoiMy43OCIsInFzcCI6IjMuMDkifQ%3D%3D&sprefix=macbook%2Caps%2C208&sr=8-1")
product_price = driver.find_element(By.CLASS_NAME, "a-price-whole")
print(product_price.text)

product_title = driver.find_element(By.CSS_SELECTOR,"#productTitle")
print(product_title.text)

news_link = driver.find_element(By.XPATH, '//*[@id="nav-xshop"]/a[1]')
print(news_link.text)




# driver.close()
driver.quit()

