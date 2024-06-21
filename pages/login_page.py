from base.base_driver import BaseDriver
from pages.locators import Locators as Lc


class LoginPage(BaseDriver):

    def inputUsername(self, userName):
        self.input_text(Lc.USERNAME, userName)
        print("User input username")
        self.func_take_screenshot_pass(screenshot=True, desc1="input username", desc2="")

    def inputPassword(self, password):
        self.input_text(Lc.PASSWORD, password)
        print("User input password")
        self.func_take_screenshot_pass(screenshot=True, desc1="input password", desc2="")

    def clickLogin(self):
        self.click(Lc.BUTTON_LOGIN)
        print("User click button login")

    def user_login(self, userName, password):
        self.inputUsername(userName)
        self.inputPassword(password)
        self.clickLogin()

    def url_success_login(self):
        url = self.get_current_url()
        return url
