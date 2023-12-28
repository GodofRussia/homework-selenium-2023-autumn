import json
import time
from typing import Dict
from contextlib import contextmanager
import os

from pytest import FixtureRequest
import pytest
from dotenv import load_dotenv
from ui.pages.base_page import BasePage
from ui.pages.lk_page import LKPage
from ui.fixtures import driver, get_driver
from conftest import config
from ui.pages.login_page import LoginPage
from selenium.webdriver.chrome.webdriver import WebDriver as ChromeWebDriver
from selenium.webdriver.chrome.webdriver import WebDriver as FireFoxWebDriver

from selenium.common.exceptions import NoAlertPresentException


class BaseCase:
    driver: ChromeWebDriver | FireFoxWebDriver | None = None
    authorize = True

    @contextmanager
    def switch_to_window(self, current, close=False):
        if len(self.driver.window_handles) == 1:
            raise Exception('only one window')

        for w in self.driver.window_handles:
            if w != current:
                self.driver.switch_to.window(w)
                break
        yield
        if close:
            self.driver.close()
        self.driver.switch_to.window(current)

    @contextmanager
    def assert_url(self, url: str, timeout=5):
        yield

        def _check():
            if self.driver.current_url != url:
                raise Exception(f"url: {self.driver.current_url}")
            
        self.wait_for(timeout, _check)

    
    @contextmanager
    def not_raises(self):
        try:
            yield
        except Exception as e:
            raise pytest.fail("DID RAISE {0}".format(e))


    def wait_for(self, timeout, callback, *args, **kwargs):
        start = time.time()

        while time.time() - start < timeout:
            try:
                return callback(*args, **kwargs)
            except Exception:
                time.sleep(0.05)
        return callback(*args, **kwargs)


    @pytest.fixture(scope="function", autouse=True)
    def setup(self, driver, config, request: FixtureRequest):
        self.driver = driver
        self.config = config

        self.driver.delete_all_cookies()

        main_page = BasePage(self.driver)
        if self.authorize:
            cookies = request.getfixturevalue("cookies_and_local_storage")

            try:
                alert = driver.switch_to.alert
                alert.accept()
            except NoAlertPresentException:
                pass
            print(cookies[1])
            for key, value in cookies[1]:
                self.driver.execute_script(f"localStorage.setItem('{key}', '{value}');")

            for cookie in cookies[0]:
                self.driver.add_cookie(cookie)


def load_localstorage_cookies_from_env():
    with open(os.path.join(os.path.dirname(__file__), "cookies.json"), "r") as f:
        cookies = json.load(f)

    with open(os.path.join(os.path.dirname(__file__), "localstorage.json"), "r") as f:
        localstorage = json.load(f)

    return cookies, localstorage


def save_localstorage_cookies_to_env(localstorage, cookies):
    with open(os.path.join(os.path.dirname(__file__), "localstorage.json"), "w") as f:
        json.dump(localstorage, f)

    with open(os.path.join(os.path.dirname(__file__), "cookies.json"), "w") as f:
        json.dump(cookies, f)


@pytest.fixture(scope="session")
def cookies_and_local_storage(credentials, config, service):
    browser = config["browser"]

    if os.path.exists(os.path.join(os.path.dirname(__file__), "cookies.json")):
        [cookies, local] = load_localstorage_cookies_from_env()
        return [cookies, local]
    new_driver = get_driver(browser, service)

    login_page = LoginPage(new_driver)
    login_page.login(credentials["user"], credentials["password"])

    # main_page = BasePage(new_driver)
    new_driver.refresh()
    co = new_driver.get_cookies()
    print(co)

    all_local_storage = new_driver.execute_script(
        "return Object.entries(localStorage);"
    )
    local_storage_dict = list(all_local_storage)

    save_localstorage_cookies_to_env(all_local_storage, co)

    return [co, local_storage_dict]


@pytest.fixture(scope="session")
def credentials() -> Dict[str, str | None]:
    dotenv_path = os.path.join(os.path.dirname(__file__), "../.env")
    print("DOTENV ")
    print(dotenv_path)
    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path)

    return {"user": os.getenv("USER_CRED"), "password": os.getenv("PASSWORD_CRED")}
