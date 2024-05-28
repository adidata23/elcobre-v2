import pytest


# @pytest.mark.usefixtures("setup")
class TestLoginPage:

    def test_login_success(self, login):
        login.inputUsername("standard_user")
        login.inputPassword("secret_sauce")
        login.clickLogin()

    def test_login_success2(self, login):
        login.inputUsername('problem_user')
        login.inputPassword("secret_sauce")
        login.clickLogin()
