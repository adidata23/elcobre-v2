from base.base_driver import BaseDriver
from pages.locators import Locators as Lc


class PurchasePage(BaseDriver):

    def clickaddbackpak(self):
        self.click(Lc.PRODUCT_BACKPACK)

    def clickaddbike(self):
        self.click(Lc.PRODUCT_BIKE)

    def clickchart(self):
        self.click(Lc.CART_BUTTON)

    def clickcheckout(self):
        self.click(Lc.CHECKOUT_BUTTON)

    def inputFirstname(self, firstName):
        self.input_text(Lc.FIRST_NAME_CHECKOUT, firstName)

    def inputLastname(self, lastName):
        self.input_text(Lc.LAST_NAME_CHECKOUT, lastName)

    def inputPostalCode(self, postalCode):
        self.input_text(Lc.ZIPCODE_CHECKOUT, postalCode)

    def clickcontinue(self):
        self.click(Lc.CONTINUE_BUTTON)

    def clickfinish(self):
        self.click(Lc.FINISH_BUTTON)

    def clickbackttoproduct(self):
        self.click(Lc.BACK_TO_PRODUCT)

    def selectitemmmm(self, option):
        self.click(Lc.DROPDOWN, option)

    def selectitemm(self):
        self.select_by_value(Lc.DROPDOWN, "lohi")
