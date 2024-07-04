from base.base_driver import BaseDriver
from pages.locators import Locators as Lc
from loguru import logger


class LoginPage(BaseDriver):

    def inputUsername(self, userName):
        self.input_text(Lc.USERNAME, userName)
        logger.info("User input username --> " + userName)
        self.func_take_screenshot_pass(screenshot=True, desc1="input username", desc2="user berhasil inputusername")

    def inputPassword(self, password):
        self.input_text(Lc.PASSWORD, password)
        logger.info("User input username --> " + password)
        self.func_take_screenshot_pass(screenshot=True, desc1="input password", desc2="user berhasil password")

    def clickLogin(self):
        self.click(Lc.BUTTON_LOGIN)
        logger.info("User click button login")

    def user_login(self, userName, password):
        self.inputUsername(userName)
        self.inputPassword(password)
        self.clickLogin()

    def url_success_login(self):
        url = self.get_current_url()
        return url
