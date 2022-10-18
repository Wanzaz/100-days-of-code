from selenium import webdriver
from selenium.webdriver.common.by import By


chrome_driver_path = "/Users/ondrejpazourek/Development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
# print(dir(driver)) printing all driver functions

driver.get("https://www.python.org/")
upcoming_envents = driver.find_element(By.XPATH, '//*[@id="content"]/div/section/div[3]/div[2]/div/ul')
content = upcoming_envents.text.split("\n")
print(content)

events_dict = { index // 2 + 1 : { "time" :  item , "name" : content[index+1]} for index, item in enumerate(content) if index % 2 == 0}
print(events_dict)


# product_price = driver.find_element(By.CLASS_NAME, "a-price-whole")
# # print(product_price.text)

# product_title = driver.find_element(By.CSS_SELECTOR,"#productTitle")
# # print(product_title.text)

# news_link = driver.find_element(By.XPATH, '//*[@id="nav-xshop"]/a[1]')
# print(news_link.text)




# driver.close()
driver.quit()

