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


class BaseCase:
    driver = None
    authorize = True

    @contextmanager
    def switch_to_window(self, current, close=False):
        for w in self.driver.window_handles:
            if w != current:
                self.driver.switch_to.window(w)
                break
        yield
        if close:
            self.driver.close()
        self.driver.switch_to.window(current)

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest):
        self.driver = driver
        self.config = config

        self.login_page: LoginPage = (request.getfixturevalue('login_page'))
        self.lk_page: LKPage = (request.getfixturevalue('lk_page'))

        main_page = BasePage(self.driver)
        if self.authorize:
            cookies = request.getfixturevalue('cookies')

            for cookie in cookies:
                self.driver.add_cookie(cookie)
            # self.driver.refresh()

# TODO может убрать в confest или fixtures?

@pytest.fixture(scope='session')
def cookies(credentials, config, service):
    browser = config["browser"]
    new_driver = get_driver(browser, service)

    login_page = LoginPage(new_driver)
    login_page.login(credentials["user"], credentials["password"])

    # main_page = BasePage(new_driver)

    time.sleep(10)
    new_driver.refresh()
    co = new_driver.get_cookies()
    print(co)
    # sorted_objects = [obj for obj in co if obj.get("domain") != "id.vk.com"]
    # print(sorted_objects)
    return co

@pytest.fixture(scope='session')
def credentials() -> Dict[str, str | None]:
    dotenv_path = os.path.join(os.path.dirname(__file__), '../.env')
    print('DOTENV ')
    print(dotenv_path)
    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path)
    
    return {'user': os.getenv('USER_CRED'), 'password': os.getenv('PASSWORD_CRED')}
