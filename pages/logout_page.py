from base.base_driver import BaseDriver
from pages.locators import Locators as Lc


class LogoutPage(BaseDriver):
    def __init__(self, driver):
        self.driver = driver

    def clickSidebar(self):
        self.click(Lc.SIDEBAR_HB)

    def clickLogoutLink(self):
        self.click(Lc.LOGOUT_BUTTON)
