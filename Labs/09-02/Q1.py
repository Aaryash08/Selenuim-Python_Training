from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)

try:
    driver.get("https://www.google.com")
    explicit_wait = WebDriverWait(driver, 15)
    search_box = explicit_wait.until(
        EC.element_to_be_clickable((By.NAME, "q"))
    )
    print("Message: Search box is now clickable via Explicit Wait.")
    search_box.send_keys("Selenium Python")
    fluent_wait = WebDriverWait(
        driver,
        timeout=20,
        poll_frequency=0.5,
        ignored_exceptions=[NoSuchElementException]
    )
    search_button = fluent_wait.until(
        EC.visibility_of_element_located((By.NAME, "btnK"))
    )
    if search_button:
        print("Message: Search button is available for interaction via Fluent Wait.")
        search_button.click()

finally:
    time.sleep(3)
    driver.quit()
