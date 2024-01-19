from base.base_driver import BaseDriver
from pages.locators import Locators as Lc


class LoginPage(BaseDriver):

    def inputUsername(self, userName):
        self.input_text(Lc.USERNAME, userName)
        print("User input username")

    def inputPassword(self, password):
        self.input_text(Lc.PASSWORD, password)
        print("User input password")
    def clickLogin(self):
        self.click(Lc.BUTTON_LOGIN)
        print("User click button login")