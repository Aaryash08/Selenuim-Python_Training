from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
driver = webdriver.Chrome()
driver.get("file:///C:/Users/KIIT/OneDrive/Desktop/Wipro_NGA/Labs/Day17/form.html")
driver.maximize_window()
driver.find_element(By.ID, "fname").send_keys("Jane")
driver.find_element(By.ID, "email").send_keys("jane@example.com")
dropdown_element = driver.find_element(By.ID, "subject")
dropdown = Select(dropdown_element)
dropdown.select_by_value("support")
driver.find_element(By.ID, "message").send_keys("Testing automation...")
submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
submit_button.click()
time.sleep(2)
print("Form submitted successfully!")
driver.quit()
