from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://letcode.in/frame")
driver.switch_to.frame("firstFr")
driver.find_element(By.NAME, "fname").send_keys("Saritha")
driver.find_element(By.NAME, "lname").send_keys("R")
print("Step 1: Text entered inside iframe.")
driver.switch_to.default_content()
insight = driver.find_element(By.XPATH, "//p[text()=' Insight ']").is_displayed()
print(f"Step 2: Switched back. Insight displayed: {insight}")
parent_window = driver.current_window_handle
driver.execute_script("window.open('https://www.google.com', '_blank');")
print("Step 3: New window opened.")
all_handles = driver.window_handles
for handle in all_handles:
    driver.switch_to.window(handle)
    print(f"Window Handle: {handle} | Title: {driver.title}")
for handle in all_handles:
    if handle != parent_window:
        driver.switch_to.window(handle)
        driver.close()
        print("Step 5: Child window closed.")
driver.switch_to.window(parent_window)
print(f"Back to Parent Window. Title: {driver.title}")

driver.quit()