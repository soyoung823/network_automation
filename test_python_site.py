from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# create a new instance of the Chrome driver
driver = webdriver.Chrome('./chromedriver')

# open python website
driver.get("https://www.python.org")

# print page title
print(driver.title)

# find search bar using name attribute
search_bar = driver.find_element_by_name('q')
search_bar.clear()
search_bar.send_keys("getting started with python")
search_bar.send_keys(Keys.RETURN)

# print current url
print(driver.current_url)

# close browser window
driver.close()
