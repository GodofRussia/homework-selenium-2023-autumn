import time
from typing import Callable

from selenium.webdriver.remote.webelement import WebElement
from ui.locators import basic
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from contextlib import contextmanager
from ui.pages.consts import WaitTime

class PageNotOpenedExeption(Exception):
    pass


class BasePage(object):
    basic_locators = basic.BasePageLocators()
    url = "https://ads.vk.com"

    # Open url
    def open(self):
        self.driver.get(self.url)

    def url_cmp_pref(self, url: str, url_pref: str):
        return url.startswith(url_pref)

    def url_cmp(self):
        return self.url_cmp_pref(self.driver.current_url, self.url)

    # Check url of opened page and page set in url
    def is_opened(self, timeout=15):
        started = time.time()
        while time.time() - started < timeout:
            if self.url_cmp():
                return True
        raise PageNotOpenedExeption(
            f"{self.url} did not open in {timeout} sec, current url {self.driver.current_url}"
        )

    def close_cookie_banner(self):
        try:
            self.click(self.basic_locators.COOKIE_BANNER_BUTTON)
        except Exception as e:
            print(e)

    def close_banner(self, timeout=3):
        try:
            self.click(self.basic_locators.BANNER_BUTTON, timeout)
        except Exception as e:
            print(e)

    # Open url that set in url of page and check if opened
    def __init__(self, driver):
        self.driver = driver
        self.open()
        # self.is_opened()

    # wait for timeout. Default timeout 5
    def wait(self, timeout=None):
        if timeout is None:
            timeout = 5
        return WebDriverWait(self.driver, timeout=timeout)

    # Wait timeout to find element by locator
    def find(self, locator, timeout=5, first=False) -> WebElement:
        return self.wait(timeout).until(self._located_cond(locator, first))

    def find_with_text(
        self, element, text, timeout=None, first=False
    ) -> WebElement:
        return self.wait(timeout).until(
            self._located_cond(
                self.basic_locators.ELEMENT_WITH_TEXT(element, text), first
            )
        )

    def click_element_with_text(
        self, element, text, timeout=None
    ) -> WebElement:
        element = self.wait(timeout).until(
            EC.element_to_be_clickable(
                self.basic_locators.ELEMENT_WITH_TEXT(element, text)
            )
        )
        element.click()

    def find_with_text_and_class(
        self, element, text, class_name, timeout=None, first=False
    ) -> WebElement:
        return self.wait(timeout).until(
            self._located_cond(
                self.basic_locators.ELEMENT_WITH_TEXT_AND_CLASS(
                    element, text, class_name
                ),
                first,
            )
        )

    def click_element_with_text_and_class(
        self, element, text, class_name, timeout=None
    ) -> WebElement:
        element = self.wait(timeout).until(
            EC.element_to_be_clickable(
                self.basic_locators.ELEMENT_WITH_TEXT_AND_CLASS(
                    element, text, class_name
                )
            )
        )
        element.click()

    def click_element_with_class(
        self, element, class_name, timeout=None
    ) -> WebElement:
        element = self.wait(timeout).until(
            EC.element_to_be_clickable(
                self.basic_locators.ELEMENT_WITH_CLASS(element, class_name)
            )
        )
        element.click()

    def _located_cond(self, locator, first=False):
        if first:

            def get_first_element_of_all(driver):
                return EC.presence_of_all_elements_located(locator)(driver)[0]

            return get_first_element_of_all
        else:
            return EC.presence_of_element_located(locator)

    def fill(self, locator, text, timeout=None) -> WebElement:
        elem = self.find(locator, timeout=timeout)
        elem.clear()
        elem.send_keys(text)
        return elem

    def fill_input_with_placeholder(
        self, placeholder, text, timeout=None
    ) -> WebElement:
        elem = self.wait(timeout).until(
            EC.presence_of_element_located(
                self.basic_locators.INPUT_WITH_PLACEHOLDER(placeholder)
            )
        )
        elem.clear()
        elem.send_keys(text)
        return elem

    def clear(self, locator, timeout=None) -> WebElement:
        elem = self.find(locator, timeout=timeout)
        elem.clear()
        return elem

    def clear_with_validation(self, locator, timeout=None):
        elem = self.find(locator, timeout=timeout)
        self.click(locator, timeout=timeout)
        elem.send_keys(Keys.END + Keys.SHIFT + Keys.HOME)
        time.sleep(3)
        elem.send_keys(Keys.BACKSPACE)

    def search(self, search_locator, query, timeout=None):
        elem = self.find(search_locator, timeout)
        elem.send_keys(query)

    # Search for element by locator and click on it
    def click(self, locator, timeout=None) -> None:
        elem = self.wait(timeout).until(EC.element_to_be_clickable(locator))
        elem.click()

    def click_element(self, element, timeout=None):
        self.wait(timeout).until(EC.element_to_be_clickable(element)).click()

    def is_checkbox_checked(self, locator, timeout=None) -> bool:
        checkbox = self.find(locator, timeout)
        return self.driver.execute_script(
            "return arguments[0].checked", checkbox
        )

    def hover_on_element(self, locator, timeout=None) -> WebElement:
        element_to_hover = self.find(locator, timeout)
        hover = ActionChains(self.driver).move_to_element(element_to_hover)
        hover.perform()
        return element_to_hover

    def find_link_with_href(self, href, timeout=None) -> WebElement:
        return self.wait(timeout).until(
            EC.presence_of_element_located(
                self.basic_locators.LINK_WITH_HREF(href)
            )
        )

    def find_validation_failed_notification(self, timeout=None) -> WebElement:
        return self.wait(timeout).until(
            EC.presence_of_element_located(
                self.basic_locators.VALIDATION_FAILED_NOTIFICATION
            )
        )

    def multiple_find(self, locator, timeout=WaitTime.MEDIUM_WAIT):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located(locator)
        )

    def action_click(self, element, timeout=WaitTime.LONG_WAIT):
        self.driver.execute_script(
            "arguments[0].scrollIntoView(true);", element
        )
        WebDriverWait(self.driver, timeout).until(EC.visibility_of(element))

        actions = ActionChains(self.driver, timeout)
        actions.move_to_element(
            WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(element)
            )
        )
        actions.click(element)
        actions.perform()
        return self

    def action_click_not_clickable(self, element, timeout = WaitTime.MEDIUM_WAIT):
        self.driver.execute_script(
            "arguments[0].scrollIntoView(true);", element
        )
        actions = ActionChains(self.driver, timeout)
        actions.move_to_element(element)
        actions.click(element)
        actions.perform()
        return self

    def search_action_click(self, locator, what_choose:int = 0, timeout:int = WaitTime.LONG_WAIT):
        el = self.multiple_find(locator, timeout)[what_choose]
        self.action_click(el,timeout)
        
        return self

    def search_action_click_not_clickable(self, locator, what_choose:int = 0, timeout:int = WaitTime.LONG_WAIT):
        if not timeout:
            timeout = WaitTime.LONG_WAIT
        el = self.multiple_find(locator, timeout)[what_choose]
        self.action_click_not_clickable(el,timeout)
        
        return self


    def is_on_site_text(self, text: str, timeout: int = WaitTime.SHORT_WAIT):
        returnVal = False
        try:
            returnVal = self.wait(timeout).until(
                EC.presence_of_element_located(
                    (By.XPATH, f"//*[contains(text(), '{text}')]")
                )
            )
        except TimeoutException as e:
            returnVal = False

        return returnVal

    @contextmanager
    def wait_for_url_change(self, timeout=10, **kwargs):
        start_url = self.driver.current_url

        yield

        url_checker = (
            lambda driver: driver.current_url != start_url
            if "url" not in kwargs
            else self.url_cmp_pref(driver.current_url, kwargs["url"])
        )
        WebDriverWait(self.driver, timeout).until(url_checker, f'curent url = {self.driver.current_url}')

    @contextmanager
    def wait_for_new_tab_open(self, timeout=10):
        tabs_num = len(self.driver.window_handles)

        yield

        WebDriverWait(self.driver, timeout).until(EC.number_of_windows_to_be(tabs_num + 1))