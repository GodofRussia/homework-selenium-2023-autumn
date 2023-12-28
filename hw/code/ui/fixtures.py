import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ServiceChrome
from selenium.webdriver.firefox.service import Service as ServiceFirefox
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from ui.pages.main_page.cases_page import CasesPage
from ui.pages.main_page.events_page import EventsPage
from ui.pages.main_page.ideas_forum_page import IdeasForumPage
from ui.pages.main_page.main_page import MainPage
from ui.pages.main_page.monetisation_page import MonetisationPage
from ui.pages.main_page.news_page import NewsPage
from ui.pages.main_page.useful_materials_page import UsefulMaterialsPage
from ui.pages.company_page import CompanyPage
from ui.pages.lk_page import LKPage
from ui.pages.login_page import LoginPage
from ui.pages.base_page import BasePage
from ui.pages.center_of_commerce import CenterOfCommercePage

import os
from ui.pages.new_company_page import NewCompanyPage
from ui.pages.group_adv_page import GroupAdvPage
from ui.pages.adv_page import AdvPage
from ui.pages.audience_page import AudiencePage
from ui.pages.site_page import SitePage

@pytest.fixture(scope="session")
def service(config):
    browser = config["browser"]
    if browser == "chrome":
        service  = ServiceChrome(executable_path=ChromeDriverManager().install())
        # service  = ServiceChrome(executable_path='/usr/local/bin/geckodriver')

    elif browser == "firefox":
        service  = ServiceFirefox(executable_path=GeckoDriverManager().install())

    elif browser == "yandex":
        service  = ServiceChrome(executable_path='/Users/mochalovskiy/Technopark/QA/homework-selenium-2023-autumn/chromedriver-mac-x64/chromedriver')
    else:
        raise RuntimeError(f'Unsupported browser: "{browser}"')

    return service


@pytest.fixture(scope="session")
def driver(config, service):
    print("Initialize driver")

    browser = config["browser"]

    driver = get_driver(browser, service)
    yield driver

    print("Stop driver")

    # Teardown
    driver.quit()
    service.stop()


def get_driver(browser, service):
    print("Get driver for browser: ", browser)
    options = webdriver.ChromeOptions()
    current_directory = os.getcwd()
    download_directory = os.path.join(current_directory, "tmp")
    prefs = {"download.default_directory": download_directory}
    options.add_experimental_option("prefs", prefs)
    
    if browser == "chrome":
        driver = webdriver.Chrome(options=options, service=service)

    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(options=options, service=service)

    elif browser == "yandex":
        options.binary_location = "/Applications/Yandex.app/Contents/MacOS/Yandex"
        
        driver = webdriver.Chrome(options=options, service=service)
    else:
        raise RuntimeError(f'Unsupported browser: "{browser}"')

    # Setup
    print("Maximize window in driver")
    driver.maximize_window()
    return driver


@pytest.fixture
def base_page(driver):
    print("INIT FIXTURE BASE PAGE")
    return BasePage(driver=driver)

@pytest.fixture
def login_page(driver):
    print("INIT FIXTURE LOGIN PAGE")
    return LoginPage(driver=driver)

@pytest.fixture
def lk_page(driver):
    print("INIT FIXTURE LKPAGE PAGE")
    return LKPage(driver=driver)

@pytest.fixture
def company_page(driver):
    print("INIT FIXTURE COMPANY PAGE")
    return CompanyPage(driver=driver)

@pytest.fixture
def center_of_commerce_page(driver):
    return CenterOfCommercePage(driver=driver)

@pytest.fixture
def new_company_page(driver):
    print("INIT FIXTURE NEW COMPANY PAGE")
    return NewCompanyPage(driver=driver)

@pytest.fixture
def group_adv_page(driver):
    print("INIT FIXTURE GROUP PAGE")
    return GroupAdvPage(driver=driver)

@pytest.fixture
def adv_page(driver):
    print("INIT FIXTURE ADV PAGE")
    return AdvPage(driver=driver)

@pytest.fixture
def audience_page(driver):
    print("INIT FIXTURE AUDIENCE PAGE")
    return AudiencePage(driver=driver)

@pytest.fixture
def site_page(driver):
    print("INIT FIXTURE SITE PAGE")
    return SitePage(driver=driver)

@pytest.fixture
def main_page(driver):
    print("INIT FIXTURE MAIN PAGE")
    return MainPage(driver=driver)

@pytest.fixture
def cases_page(driver):
    print("INIT FIXTURE CASES PAGE")
    return CasesPage(driver=driver)

@pytest.fixture
def events_page(driver):
    print("INIT FIXTURE EVENTS PAGE")
    return EventsPage(driver=driver)

@pytest.fixture
def ideas_forum_page(driver):
    print("INIT FIXTURE IDEAS FORUM PAGE")
    return IdeasForumPage(driver=driver)

@pytest.fixture
def monetisation_page(driver):
    print("INIT FIXTURE CASES PAGE")
    return MonetisationPage(driver=driver)

@pytest.fixture
def news_page(driver):
    print("INIT FIXTURE CASES PAGE")
    return NewsPage(driver=driver)

@pytest.fixture
def useful_materials_page(driver):
    print("INIT FIXTURE USEFUL MATERIALS PAGE")
    return UsefulMaterialsPage(driver=driver)
