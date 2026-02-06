from selenium.webdriver.common.by import By
from BasePage import BasePage

class LoginPage(BasePage):
    # Locators
    USERNAME_FIELD = (By.NAME, "username")
    PASSWORD_FIELD = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")
    DASHBOARD_HEADER = (By.TAG_NAME, "h6")

    def login_to_orange_hrm(self, user, pwd):
        self.input_text(self.USERNAME_FIELD, user)
        self.input_text(self.PASSWORD_FIELD, pwd)
        self.click_element(self.LOGIN_BUTTON)