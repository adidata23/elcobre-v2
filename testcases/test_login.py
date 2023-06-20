import pytest
from pages.login_page import LoginPage

@pytest.mark.usefixtures("setup")
class TestLoginPage:

    def test_login_success(self):
        login = LoginPage(self.driver)
        login.inputUsername('standard_user')
        login.inputPassword("secret_sauc")
        login.clickLogin()

