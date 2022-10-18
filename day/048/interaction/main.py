from selenium import webdriver
from selenium.webdriver.common.by import By


chrome_driver_path = "/Users/ondrejpazourek/Development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
# print(dir(driver)) printing all driver functions

driver.get("https://en.wikipedia.org/wiki/Main_Page")

num_of_articles = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]')
print(num_of_articles.text)



# driver.close()
driver.quit()

