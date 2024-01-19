import pytest
from pages.login_page import LoginPage


@pytest.mark.usefixtures("setup")
class TestLoginPage:

    def test_login_success(self, setup, login):
        login.inputUsername("standard_user")
        login.inputPassword("secret_sauce")
        login.clickLogin()

    def test_login_success2(self, setup, login):
        login.inputUsername('problem_user')
        login.inputPassword("secret_sauce")
        login.clickLogin()
