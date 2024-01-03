import pytest
from pages.login_page import LoginPage
from pages.logout_page import LogoutPage
from pages.purchase_page import PurchasePage
import time


class TestLoginPage:
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)

    @pytest.mark.usefixtures("setup")
    def test_login_success(self):
        login = LoginPage(self.driver)
        login.inputUsername('standard_user')
        login.inputPassword("secret_sauce")
        login.clickLogin()

#dropdown        
        login.selectitem('hilo')
        time.sleep(5)
#addtochart
    def test_purchase_success(self):
        purchase = PurchasePage(self.driver)
        purchase.clickaddbackpak()
        purchase.clickchart()
        purchase.clickcheckout()

#information
        purchase.inputFirstname("Siti")
        purchase.inputLastname("Markonah")
        purchase.inputPostalCode("48222")
        purchase.clickcontinue()

#overview page
        purchase.clickfinish()
        time.sleep (3)
#back to home
        purchase.clickbackttoproduct()

        time.sleep (4)
#    def test_logout_success(self):
#       logout = LogoutPage(self.driver)
#       logout.clickSidebar()
#       logout.clickLogoutLink()