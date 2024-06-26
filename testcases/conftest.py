import logging
import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from loguru import logger
from pages.logout_page import LogoutPage
from pages.login_page import LoginPage
from pages.purchase_page import PurchasePage
from utilities.take_screenshot import TakeScreenshot as TS
from base.base_driver import BaseDriver
from utilities.report_pdf import PDF
from webdriver_manager.chrome import ChromeDriverManager

log = logger


@pytest.fixture(scope="session")
def setup():
    # Create ChromeOptions instance and configure it
    option = webdriver.ChromeOptions()
    option.add_argument("--start-maximized")
    option.add_experimental_option('detach', True)
    # option.add_argument("--headless")
    option.add_experimental_option("excludeSwitches", ["enable-automation"])

    # initiate Chrome driver using ChromeDriverManager and options driver = webdriver.Chrome(service=ChromeService(
    # ChromeDriverManager().install()), options=option) #initiate driver for mac
    log.info("Initiate Webdriver Chrome")
    driver = webdriver.Chrome(service=ChromeService(executable_path="C:\webdriver\chromedriver-win64\chromedriver.exe"),
                              options=option)
    log.info("Initiate TakeScreenShot and Set Working Directory")
    print("initiate webdriver on driver")
    ss = TS(driver)
    ss.set_working_dir()
    log.add(ss.working_dir + "/tracelog.log",  # self.ss_obj.working_dir+
            format="{time:YYYY-MM-DD HH:mm:ss.SSS} {level}\t{message}",
            level="INFO",
            catch=False,
            backtrace=False,
            # diagnose=False
            )
    yield driver, ss
    driver.quit()


class Pages:
    def __init__(self, setup):
        self.login_page = LoginPage(setup[0], setup[1])
        self.logout_page = LogoutPage(setup[0], setup[1])
        self.purchase_page = PurchasePage(setup[0], setup[1])


@pytest.fixture
def base(setup):
    driver, ss = setup
    return BaseDriver(driver, ss)


@pytest.fixture
def pages(setup):
    return Pages(setup)


@pytest.fixture(scope="session", autouse=True)
def before_test_session(setup):
    driver, ss = setup
    log.info("Maximize window")
    setup[0].maximize_window()
    print("=====BEFORE TEST SESSION=====")
    print("Open browser")
    # yield
    # print("=====AFTER TEST SESSION on yield before test session=====")


@pytest.fixture(autouse=True)
def before_test_method(setup):
    print("=====BEFORE TEST METHOD=====")
    print("Access to website")
    url = 'https://www.saucedemo.com/'
    log.info("Go to Website url --> " + url)
    setup[0].get(url)


@pytest.fixture(autouse=True)
def after_test_method(setup):
    yield  # Yield to allow the test method to run
    print("=====AFTER TEST METHOD=====")

    # # Open a new tab
    # setup.execute_script("window.open('');")
    # setup.switch_to.window(setup.window_handles[-1])
    # print("Open new Tab")
    #
    # # Navigate to YouTube
    # # setup.get("https://www.google.co.id/")
    # print("Access to Homepage")
    #
    # # Close the new tab
    # setup.close()
    # print("Close new Tab")
    #
    # # Switch back to the original tab
    # setup.switch_to.window(setup.window_handles[0])


@pytest.fixture(scope="session", autouse=True)
def after_test_session(setup):
    yield  # Yield to ensure this runs after all tests
    print("=====AFTER TEST SESSION=====")
    driver, ss = setup
    log.info("Initiate PDF Object")
    pdf = PDF(pdf_filename=ss.working_dir + "//TestingPDF_elcobrev2.pdf",
              param_path="elcobre-v2//data//param.txt",
              result_path="elcobre-v2//data//scenario_result.txt",
              cvpg_subtitle="Liquid Managemen - Cash Ditribution",
              cvpg_author="Automation Team",
              cvpg_tcid="Cash Distribution Thru to Casa Thru - Fix - Immediate",
              header_author="Automation Team",
              header_tcid="Cash Distribution Thru to Casa Thru - Fix - Immediate")
    log.info("Run PDF reader scenario result")
    pdf.data_reader()
    log.info("Run generate report PDF")
    pdf.generate_report()

    setup[0].refresh()
    log.info("Browser tab quit")
    setup[0].quit()


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
