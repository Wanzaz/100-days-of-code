from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


chrome_driver_path = "/Users/ondrejpazourek/Development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
# print(dir(driver)) printing all driver functions

# driver.get("https://en.wikipedia.org/wiki/Main_Page")

# num_of_articles = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]')
# print(num_of_articles.text)

# link = driver.find_element(By.PARTIAL_LINK_TEXT, "Offham Hill")
# link.click()


# search = driver.find_element(By.NAME, "search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)


# Filling webpage
driver.get("https://secure-retreat-92358.herokuapp.com/")
first_name = driver.find_element(By.NAME, "fName").send_keys("Andrew")
last_name = driver.find_element(By.NAME, "lName").send_keys("Flint")
email = driver.find_element(By.NAME, "email").send_keys("wanaz.contact@gmail.com")
sign_up_button = driver.find_element(By.CSS_SELECTOR, "button")
sign_up_button.click()




# driver.close()
driver.quit()

