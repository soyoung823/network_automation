import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver = webdriver.Firefox()
driver.implicitly_wait(5)

driver.get("https://bandcamp.com/discover/")

# accept cookies
try:
    cookie_accept_button = driver.find_element(By.CSS_SELECTOR, "#cookie-control-dialog button.g-button.outline")
    cookie_accept_button.click()
except NoSuchElementException as e:
    pass

time.sleep(1)

search = driver.find_element(By,CLASS_NAME, "site-search-form")
search_field = search.find_element(By.TAG_NAME, "input")
search_field.send_keys("selenium")
search_field.submit()

driver.execute_script("arguments[0].click();", overlay_element)

menu = driver.find_element(By.CSS_SELECTOR, ".menu")
submenu = driver.find_element(By.CSS_SELECTOR, ".menu #submenu")

actions = ActionChains(driver)
actions.move_to_element(menu)
actions.click(submenu)

actions.perform()

time.sleep(5)

driver.close()
