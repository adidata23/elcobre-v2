from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select


class BaseDriver:
    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):
        try:
            WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(locator)).click()
        except TimeoutException:
            print(f"TimeoutException: Click operation failed. Element not clickable within 10 seconds.")

    def input_text(self, locator, text):
        try:
            WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(locator)).send_keys(text)
        except TimeoutException:
            print(f"TimeoutException: Input text operation failed. Element not visible within 10 seconds.")

    def get_title(self, title) -> str:
        try:
            WebDriverWait(self.driver, 10).until(ec.title_is(title))
            return self.driver.title
        except TimeoutException:
            print(f"TimeoutException: Get title operation failed. Title not as expected within 10 seconds.")
            return ""

    def verify_text_element(self, locator, text) -> str:
        try:
            WebDriverWait(self.driver, 10).until(ec.text_to_be_present_in_element(locator, text))
            return self.driver.text
        except TimeoutException:
            print(f"TimeoutException: Verify text element operation failed. Text not present within 10 seconds.")
            return ""

    def select_option(self, locator, text):
        try:
            Select(self.driver.find_element(locator)).select_by_visible_text(text)
        except TimeoutException:
            print(f"TimeoutException: Select option operation failed. Element not found within 10 seconds.")

    def select_by_value(self, locator, value):
        try:
            Select(self.driver.find_element(locator)).select_by_value(value)
        except TimeoutException:
            print(f"TimeoutException: Select by value operation failed. Element not found within 10 seconds.")
