from base.base_driver import BaseDriver
from pages.locators import Locators as Lc


class LogoutPage(BaseDriver):

    def clickLogoutLink(self):
        self.click(Lc.SIDEBAR_HB)
        self.click(Lc.LOGOUT_BUTTON)
