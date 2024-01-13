import os
import json
from typing import Dict
from dotenv import load_dotenv
import logging

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
from ui.pages.new_company_page import NewCompanyPage
from ui.pages.group_adv_page import GroupAdvPage
from ui.pages.adv_page import AdvPage
from ui.pages.audience_page import AudiencePage
from ui.pages.site_page import SitePage

logger = logging.getLogger("tests")


@pytest.fixture(scope="session", autouse=True)
def download_directory():
    tmp_dir = "tmp"
    os.makedirs(tmp_dir, exist_ok=True)
    current_directory = os.getcwd()
    download_dir = os.path.join(current_directory, tmp_dir)
    logger.info("download dir: %s", download_dir)
    return download_dir


@pytest.fixture(scope="session", autouse=True)
def mock_files():
    upload_dir = "mock_files"
    os.makedirs(upload_dir, exist_ok=True)
    current_directory = os.getcwd()
    files_dir = os.path.join(current_directory, upload_dir)
    logger.debug("mock dir: %s", files_dir)
    return files_dir


@pytest.fixture(scope="session")
def service(config):
    browser = config["browser"]
    if browser == "chrome":
        service = ServiceChrome(
            executable_path=ChromeDriverManager().install()
        )

    elif browser == "firefox":
        service = ServiceFirefox(
            executable_path=GeckoDriverManager().install()
        )

    elif browser == "yandex":
        service = ServiceChrome(executable_path=config["yandex_driver_path"])
    else:
        raise RuntimeError(f'Unsupported browser: "{browser}"')

    return service


@pytest.fixture(scope="session")
def driver(config, service, download_directory):
    browser = config["browser"]

    driver = get_driver(browser, service, config, download_directory)
    yield driver

    # Teardown
    driver.quit()
    service.stop()


def get_driver(browser, service, config, download_directory):
    options = webdriver.ChromeOptions()

    prefs = {"download.default_directory": download_directory}
    options.add_experimental_option("prefs", prefs)

    if browser == "chrome":
        driver = webdriver.Chrome(options=options, service=service)

    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(options=options, service=service)

    elif browser == "yandex":
        options.binary_location = config["yandex_browser_path"]

        driver = webdriver.Chrome(options=options, service=service)
    else:
        raise RuntimeError(f'Unsupported browser: "{browser}"')

    # Setup
    driver.maximize_window()
    return driver


def load_localstorage_cookies_from_env():
    with open(
        os.path.join(os.path.dirname(__file__), "cookies.json"), "r"
    ) as f:
        cookies = json.load(f)

    with open(
        os.path.join(os.path.dirname(__file__), "localstorage.json"), "r"
    ) as f:
        localstorage = json.load(f)

    return cookies, localstorage


def save_localstorage_cookies_to_env(localstorage, cookies):
    with open(
        os.path.join(os.path.dirname(__file__), "localstorage.json"), "w"
    ) as f:
        json.dump(localstorage, f)

    with open(
        os.path.join(os.path.dirname(__file__), "cookies.json"), "w"
    ) as f:
        json.dump(cookies, f)


@pytest.fixture(scope="session")
def cookies_and_local_storage(
    credentials, config, service, download_directory
):
    browser = config["browser"]

    if os.path.exists(os.path.join(os.path.dirname(__file__), "cookies.json")):
        [cookies, local] = load_localstorage_cookies_from_env()
        return [cookies, local]
    new_driver = get_driver(browser, service, config, download_directory)

    login_page = LoginPage(new_driver)
    login_page.login(credentials["user"], credentials["password"])

    new_driver.refresh()
    co = new_driver.get_cookies()

    all_local_storage = new_driver.execute_script(
        "return Object.entries(localStorage);"
    )
    local_storage_dict = list(all_local_storage)

    save_localstorage_cookies_to_env(all_local_storage, co)

    return [co, local_storage_dict]


@pytest.fixture(scope="session")
def credentials() -> Dict[str, str | None]:
    dotenv_path = os.path.join(os.path.dirname(__file__), "../.env")

    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path)

    return {
        "user": os.getenv("USER_CRED"),
        "password": os.getenv("PASSWORD_CRED"),
    }


@pytest.fixture
def base_page(driver):
    return BasePage(driver=driver)


@pytest.fixture
def login_page(driver):
    return LoginPage(driver=driver)


@pytest.fixture
def lk_page(driver):
    return LKPage(driver=driver)


@pytest.fixture
def company_page(driver):
    return CompanyPage(driver=driver)


@pytest.fixture
def center_of_commerce_page(driver):
    return CenterOfCommercePage(driver=driver)


@pytest.fixture(scope="session")
def center_of_commerce_page_session(driver):
    return CenterOfCommercePage(driver=driver)


@pytest.fixture
def new_company_page(driver):
    return NewCompanyPage(driver=driver)


@pytest.fixture
def group_adv_page(driver):
    return GroupAdvPage(driver=driver)


@pytest.fixture
def adv_page(driver):
    return AdvPage(driver=driver)


@pytest.fixture
def audience_page(driver):
    return AudiencePage(driver=driver)


@pytest.fixture
def site_page(driver):
    return SitePage(driver=driver)


@pytest.fixture
def main_page(driver):
    return MainPage(driver=driver)


@pytest.fixture
def cases_page(driver):
    return CasesPage(driver=driver)


@pytest.fixture
def events_page(driver):
    return EventsPage(driver=driver)


@pytest.fixture
def ideas_forum_page(driver):
    return IdeasForumPage(driver=driver)


@pytest.fixture
def monetisation_page(driver):
    return MonetisationPage(driver=driver)


@pytest.fixture
def news_page(driver):
    return NewsPage(driver=driver)


@pytest.fixture
def useful_materials_page(driver):
    return UsefulMaterialsPage(driver=driver)
