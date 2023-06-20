class SeleniumAssertions:
    def __init__(self, driver):
        self.driver = driver

    def assert_title(self, expected_title):
        assert self.driver.title == expected_title, f"Title assertion failed. Expected: {expected_title}, Actual: {self.driver.title}"

    def assert_url(self, expected_url):
        assert self.driver.current_url == expected_url, f"URL assertion failed. Expected: {expected_url}, Actual: {self.driver.current_url}"

    def assert_element_present(self, locator):
        assert self.driver.find_element(*locator), f"Element assertion failed. Element not present: {locator}"

    def assert_element_text(self, locator, expected_text):
        element = self.driver.find_element(*locator)
        assert element.text == expected_text, f"Element text assertion failed. Expected: {expected_text}, Actual: {element.text}"

    def assert_element_attribute(self, locator, attribute_name, expected_value):
        element = self.driver.find_element(*locator)
        actual_value = element.get_attribute(attribute_name)
        assert actual_value == expected_value, f"Element attribute assertion failed. Attribute: {attribute_name}, Expected: {expected_value}, Actual: {actual_value}"

    def assert_element_selected(self, locator):
        element = self.driver.find_element(*locator)
        assert element.is_selected(), f"Element selection assertion failed. Element not selected: {locator}"

    def assert_element_displayed(self, locator):
        element = self.driver.find_element(*locator)
        assert element.is_displayed(), f"Element display assertion failed. Element not displayed: {locator}"
