from base.base_driver import BaseDriver
from pages.locators import Locators as Lc


class PurchasePage(BaseDriver):

    def click_add_backpack(self):
        self.click(Lc.PRODUCT_BACKPACK)

    def click_add_bike(self):
        self.click(Lc.PRODUCT_BIKE)

    def click_chart(self):
        self.click(Lc.CART_BUTTON)

    def click_checkout(self):
        self.click(Lc.CHECKOUT_BUTTON)

    def input_firstname(self, firstName):
        self.input_text(Lc.FIRST_NAME_CHECKOUT, firstName)

    def input_lastname(self, lastName):
        self.input_text(Lc.LAST_NAME_CHECKOUT, lastName)

    def input_postalcode(self, postalCode):
        self.input_text(Lc.ZIPCODE_CHECKOUT, postalCode)

    def clickcontinue(self):
        self.click(Lc.CONTINUE_BUTTON)

    def click_finish(self):
        self.click(Lc.FINISH_BUTTON)

    def click_back_to_product(self):
        self.click(Lc.BACK_TO_PRODUCT)

    def select_item(self, option):
        self.click(Lc.DROPDOWN, option)

    def select_itemm(self):
        self.select_by_value(Lc.DROPDOWN, "lohi")
