from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
driver = webdriver.Chrome()
driver.get("https://letcode.in/alert")
driver.find_element(By.ID,("accept")).click()
alert=driver.switch_to.alert
print(alert.text)
alert.accept()
driver.find_element(By.ID,("confirm")).click()
alert=driver.switch_to.alert
print(alert.text)
# driver.find_element(By.ID,("prompt")).click()
# alert=driver.switch_to.alert
# print(alert.text)
# driver.find_element(By.ID,("modern")).click()
# alert=driver.switch_to.alert
# print(alert.text)
driver.quit()