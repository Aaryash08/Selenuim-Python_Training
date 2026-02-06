from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("file:///C:/Users/KIIT/OneDrive/Desktop/Wipro_NGA/Labs/Day17/form2.html")
wait = WebDriverWait(driver, 10)
driver.find_element(By.ID, "btnAlert").click()
alert1 = wait.until(EC.alert_is_present())
print(f"Alert 1 Message: {alert1.text}")
alert1.accept()
driver.find_element(By.ID, "btnConfirm").click()
alert2 = wait.until(EC.alert_is_present())
print(f"Alert 2 Message: {alert2.text}")
alert2.dismiss()
print("Result after Dismiss:", driver.find_element(By.ID, "result").text)
driver.find_element(By.ID, "btnPrompt").click()
alert3 = wait.until(EC.alert_is_present())
print(f"Prompt Message: {alert3.text}")
alert3.send_keys("Selenium is Awesome!")
alert3.accept()
result_text = driver.find_element(By.ID, "result").text
print(f"Final Page Result: {result_text}")
time.sleep(3)
driver.quit()