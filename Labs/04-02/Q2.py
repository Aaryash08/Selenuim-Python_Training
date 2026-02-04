from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()

try:
    driver.get("https://tutorialsninja.com/demo/")
    driver.maximize_window()
    print(f"Initial Page Title: {driver.title}")
    phones_link = driver.find_element(By.LINK_TEXT, "Phones & PDAs")
    phones_link.click()
    print(f"Navigated Page Title: {driver.title}")
    driver.back()
    print(f"After Back Title: {driver.title}")
    driver.forward()
    print(f"After Forward Title: {driver.title}")
    driver.refresh()
    print(f"After Refresh Title: {driver.title}")

finally:
    driver.quit()