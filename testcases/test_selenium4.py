# selenium 4
import logging

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from utilities.logger import TestLogger

# Create an instance of the TestLogger class
logger = TestLogger(log_file_name='test_case.log')


def test_eight_components():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    logger.info('Starting test case: test_eight_component')
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")
    logger.info('Get url to --> https://www.selenium.dev/selenium/web/web-form.html')

    title = driver.title
    logger.info(f'The browser title is: {title}')
    assert title == "Web form"
    logger.info(f'assert {title} is equal with Web form')

    # driver.implicitly_wait(0.5)

    text_box = driver.find_element(by=By.NAME, value="my-text")
    submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

    text_box.send_keys("Selenium")
    logger.info('Send text selenium in field Text Input')

    driver.implicitly_wait(55)
    submit_button.click()
    logger.info('Click button submit')

    message = driver.find_element(by=By.ID, value="message")
    text = message.text
    assert text == "Received!"
    logger.info(f'Verify that form already submitted and got message --> {text}')
    #driver.quit()
