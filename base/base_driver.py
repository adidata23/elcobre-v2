from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from loguru import logger
from utilities.take_screenshot import TakeScreenshot


class BaseDriver(object):
    def __init__(self, driver, ss):
        self.driver = driver
        self.ss = ss


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

    def get_text(self, locator):
        element = self.driver.find_element(locator)
        return element.text

    def get_current_url(self):
        return self.driver.current_url

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

    @logger.catch(reraise=True)
    def func_take_screenshot_fail(self, screenshot, desc1="", desc2=""):
        if screenshot:
            self.ss.take_ss_w_desc("Failed", desc1, desc2)
            logger.error(f"Take screenshot fail: '{desc1}' - '{desc2}'")

    @logger.catch(reraise=True)
    def func_take_screenshot_pass(self, screenshot, desc1="", desc2=""):
        if screenshot:
            self.ss.take_ss_w_desc("Passed", desc1, desc2)
            logger.info(f"Take screenshot pass: '{desc1}' - '{desc2}'")

    @logger.catch(reraise=True)
    def func_take_screenshot_by_element(self, screenshot, alias="", by=By.ID, locator="", desc1="", desc2="",
                                        status="passed"):
        alias = self.driver.find_element(by, locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", alias)
        logger.info(f"Javascript scroll to element located by '{by}' = '{locator}'")
        if status == "failed":
            self.ss.take_ss_w_desc("Failed", desc1, desc2)
            logger.info(f"Take screenshot failed: '{desc1}' - '{desc2}'")
        elif screenshot:
            self.ss.take_ss_w_desc("Passed", desc1, desc2)
            logger.info(f"Take screenshot pass: '{desc1}' - '{desc2}'")

    @logger.catch(reraise=True)
    def func_upload(self, by=By.ID, locator="", path=""):
        WebDriverWait.until(ec.presence_of_element_located((by, locator)))
        logger.info(f"Element wait located by '{by}' = '{locator}'")
        self.driver.find_element(by, locator).send_keys(path)
        logger.info(f"Element send keys located by '{by}' = '{locator}', file path = {path}")

    @logger.catch(reraise=True)
    def func_window_close(self):
        """webdriver close()
        """
        self.driver.close()
        logger.info("Webdriver close window")

    @logger.catch(reraise=True)
    def func_window_maximize(self):
        self.driver.maximize_window()

    @logger.catch(reraise=True)
    def func_window_new_close(self):
        self.driver.switch_to.window(self.driver.window_handles[0])
        logger.info("Webdriver switch to window [0]")

    @logger.catch(reraise=True)
    def func_window_open_new(self, num=1):
        newtab = self.driver.window_handles[num]
        self.driver.switch_to.window(newtab)
        logger.info(f"Webdriver switch to window [{num}]")

    @logger.catch(reraise=True)
    def func_window_open_new_tab(self, url):
        assert len(self.driver.window_handles) == 1, "Window Handles total (len) is not 1"
        logger.info(f"Assert check current window handles total = {len(self.driver.window_handles)}")
        self.driver.execute_script("window.open('');")
        logger.info("Javascript open new tab")
        self.driver.switch_to.window(self.driver.window_handles[1])
        logger.info("Webdriver switch to window [1]")
        self.driver.get(url)
        logger.info(f"Webdriver open (get) url: {url}")
