from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium import webdriver


class BaseDriver:
    def __int__(self, driver):
        self.driver = driver

    def click(self, locator):
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(locator)).click()

    def input_text(self, locator, text):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(locator)).send_keys(text)

    def get_title(self, title) -> str:
        WebDriverWait(self.driver, 10).until(ec.title_is(title))
        return self.driver.title

    def verify_text_element(self, locator, text) -> str:
        WebDriverWait(self.driver, 10).until(ec.text_to_be_present_in_element(locator, text))
        return self.driver.text

    def select_option(self, locator, text):
        Select(self.driver.find_element(locator)).select_by_visible_text(text)

    def select_by_value(self, locator, value):
        Select(self.driver.find_element(locator)).select_by_value(value)

    def click_native(self, locator):
        self.click(locator)
