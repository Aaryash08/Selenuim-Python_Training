from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://tutorialsninja.com/demo/index.php?route=account/register")
first_name = driver.find_element(By.ID, "input-firstname")
last_name = driver.find_element(By.NAME, "lastname")
email_field = driver.find_element(By.CSS_SELECTOR, "#input-email")
telephone = driver.find_element(By.XPATH, "//input[@id='input-telephone']")
continue_button = driver.find_element(By.CLASS_NAME, "btn-primary")
first_name.send_keys("Admin")
last_name.send_keys("123")
email_field.send_keys("admin@example.com")
telephone.send_keys("1234567890")
driver.find_element(By.ID, "input-password").send_keys("admin123")
driver.find_element(By.ID, "input-confirm").send_keys("admin123")
driver.find_element(By.NAME, "agree").click()
continue_button.click()

try:
    error_msg = driver.find_element(By.CSS_SELECTOR, ".alert-danger").text
    print(f"Validation Message Found: {error_msg}")
    if "Warning" in error_msg:
        print("Test Passed: System correctly identified a registration issue.")
except:
    if "Success" in driver.title:
        print("Test Passed: Account created successfully.")
    else:
        print("Validation failed: No message or success page detected.")

driver.quit()