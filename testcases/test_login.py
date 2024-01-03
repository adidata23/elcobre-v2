import pytest
from pages.login_page import LoginPage


@pytest.mark.usefixtures("setup")
class TestLoginPage:
    driver = None  # type Optional[LoginPage]

    def test_login_success(self):
        login = LoginPage(self.driver)
        login.inputUsername('standard_user')
        login.inputPassword("secret_sauce")
        login.clickLogin()

    def test_login_success2(self):
        login = LoginPage(self.driver)
        login.inputUsername('problem_user')
        login.inputPassword("secret_sauce")
        login.clickLogin()
