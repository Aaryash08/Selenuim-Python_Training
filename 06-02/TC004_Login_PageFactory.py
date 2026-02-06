from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from Loginpage_PageFactory import loginpage_PageFactory
driver = webdriver.Firefox()
driver.implicitly_wait(10)
wait = WebDriverWait(driver, 10)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(5)
loginobj = loginpage_PageFactory(driver)
loginobj.enterusername("Admin")
loginobj.enterpassword("admin123")
loginobj.clicklogin()
time.sleep(10)
driver.quit()