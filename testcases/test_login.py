import pytest


class TestLoginPage:

    def test_login_success(self, setup, page):
        page.inputUsername("standard_user")
        page.inputPassword("secret_sauce")
        page.clickLogin()

    def test_login_success2(self, setup, page):
        page.inputUsername('problem_user')
        page.inputPassword("secret_sauce")
        page.clickLogin()
