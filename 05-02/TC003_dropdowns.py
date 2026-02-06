from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
driver = webdriver.Firefox()
driver.get("https://demo.opencart.com/index.php?route=product/product&path=57&product_id=49")
sleep(20)
driver.find_element(By.LINK_TEXT,"Desktops").click()
driver.find_element(By.LINK_TEXT,"Mac (1)").click()
dropdown=Select(driver.find_element(BY.ID,"input-sort"))
dropdown.select_by_indec(4)

for option in dropdown.options:
    print(option.text)
dropdown.select_by_index(4)