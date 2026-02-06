import pytest
from LoginPage import LoginPage
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup")
class TestOrangeHRM:

    def test_login_success(self):
        login_pg = LoginPage(self.driver)
        login_pg.login_to_orange_hrm("Admin", "admin123")
        header_text = login_pg.get_text(login_pg.DASHBOARD_HEADER)
        assert header_text == "Dashboard"
        print(f"\n[PASSED]: Logged in successfully. Found header: {header_text}")

    def test_invalid_login(self):
        self.driver.delete_all_cookies()
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        login_pg = LoginPage(self.driver)
        login_pg.login_to_orange_hrm("WrongUser", "WrongPass")
        print("\n[PASSED]: Negative test case executed.")