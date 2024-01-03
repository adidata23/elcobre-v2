from selenium.webdriver.common.by import By


class Locators:
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    BUTTON_LOGIN = (By.ID, "login-button")
    SIDEBAR_HB = (By.ID, "react-burger-menu-btn")
    LOGOUT_BUTTON = (By.ID, "logout_sidebar_link")
    PRODUCT_BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    PRODUCT_BIKE = (By.ID, "add-to-cart-sauce-labs-bike-light")
    CART_BUTTON = (By.ID, "shopping_cart_container")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    FIRST_NAME_CHECKOUT = (By.ID, "first-name")
    LAST_NAME_CHECKOUT = (By.ID, "last-name")
    ZIPCODE_CHECKOUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")
    COMPLETE_LABLE = (By.ID, "checkout_complete_container")
    PRODUCT_LABEL = (By.ID, "inventory_filter_container")
    BACK_TO_PRODUCT = (By.ID, "back-to-products")
    DROPDOWN = (By.CLASS_NAME, "product_sort_container")
    SCROLLDOWN = (By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)")
