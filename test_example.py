from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://www.example.com")

element = driver.find_element(By.ID, "username_field")

element.send_keys("your_username")
element.click()
element.submit()

wait = WEbDriverWait(driver, 10) # 10 sec
element = wait.until(EC.element_to_be_clickable((By.ID, "submit_button")))

# web scrapping (extracting data)
text_content = element.text
attribute_value = element.get_attribute("href")

driver.close()
