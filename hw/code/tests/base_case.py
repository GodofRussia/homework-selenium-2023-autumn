from contextlib import contextmanager

from pytest import FixtureRequest
import pytest
from ui.pages.consts import get_screenshots_path

from ui.pages.base_page import BasePage
from ui.fixtures import get_driver
from ui.pages.login_page import LoginPage
from selenium.webdriver.chrome.webdriver import WebDriver as ChromeWebDriver
from selenium.webdriver.firefox.webdriver import WebDriver as FireFoxWebDriver

from selenium.common.exceptions import NoAlertPresentException


class SwithToWindowException(Exception):
    pass


class BaseCase:
    driver: ChromeWebDriver | FireFoxWebDriver
    authorize = True

    @contextmanager
    def switch_to_window(self, close=False):
        if len(self.driver.window_handles) == 1:
            raise SwithToWindowException("only one window")

        current = self.driver.current_window_handle
        
        for w in self.driver.window_handles:
            if w != current:
                self.driver.switch_to.window(w)
                break
        yield
        if close:
            self.driver.close()
        self.driver.switch_to.window(current)

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
            for key, value in cookies[1]:
                self.driver.execute_script(
                    f"localStorage.setItem('{key}', '{value}');"
                )

            for cookie in cookies[0]:
                self.driver.add_cookie(cookie)

        before_failed = request.session.testsfailed

        yield

        after_failed = request.session.testsfailed

        if after_failed != before_failed:
            node_name = request.node.name
            self.driver.save_screenshot(get_screenshots_path(node_name))
