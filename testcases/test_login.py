import pytest
from pages.login_page import LoginPage


class TestLoginPage:
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)

    @pytest.mark.usefixtures("setup")
    def test_login_success(self):
        login = LoginPage(self.driver)
        login.inputUsername('standard_user')
        login.inputPassword("secret_sauce")
        login.clickLogin()
