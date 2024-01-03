import pytest
from pages.login_page import LoginPage
from pages.logout_page import LogoutPage

@pytest.mark.usefixtures("setup")
class TestLogoutPage:

    def test_login_success(self):
        logout = LogoutPage(self.driver)
        logout.clickSidebar()
        logout.clickLogoutLink()