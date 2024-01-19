import os
import pytest
import logging
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from pages import PAGE_CLASSES


@pytest.fixture
def setup(request):
    # Your setup logic here, e.g., initializing WebDriver
    option = webdriver.ChromeOptions()
    option.add_argument("--start-maximized")
    option.add_experimental_option("excludeSwitches", ["enable-automation"])
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=option)
    print("initiate webdriver on driver")
    driver.get('https://www.saucedemo.com/')
    print("Got to url")

    # Return the driver to make it available to tests
    yield driver

    # Teardown: Close the browser after the test
    driver.close()


@pytest.fixture
def page(setup, request):
    page_type = request.param
    if page_type not in PAGE_CLASSES:
        raise ValueError(f"Invalid page_type: {page_type}")
    return PAGE_CLASSES[page_type](setup)

def logger(name):
    log_item = logging.getLogger(name)
    with open('LogFile.log', 'a') as logFile:
        logFile.seek(0)
        # logFile.truncate()
    file_handler = logging.FileHandler("LogFile.log")
    log_format = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
    file_handler.setFormatter(log_format)
    log_item.addHandler(file_handler)
    log_item.setLevel(logging.DEBUG)
    return log_item


@pytest.fixture(scope='function')
def setup_logger(request):
    # full name: 'class name::function name'
    full_name = os.environ.get('PYTEST_CURRENT_TEST').split(' ')[0]
    # full_name = request.module.__name__ # print the function name
    # full_name = request.node.name # print the class name
    request.cls.log = logger(full_name)
    yield
    print('close')
