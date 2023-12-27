import time

from selenium.webdriver.remote.webelement import WebElement
from ui.locators import basic
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class PageNotOpenedExeption(Exception):
    pass


class BasePage(object):
    basic_locators = basic.BasePageLocators()
    url = "https://ads.vk.com/"

    # Open url
    def open(self):
        print("OPEN URL: ", self.url)
        self.driver.get(self.url)

    def url_cmp(self):
        driver_url = self.driver.current_url
        for i, v in enumerate(self.url):
            if self.url[i] == "*":
                return True
            if self.url[i] != driver_url[i]:
                return False

    # Check url of opened page and page set in url
    def is_opened(self, timeout=15):
        time.sleep(5)
        """started = time.time()
        while time.time() - started < timeout:

            # TODO
            if self.url_cmp():
            # if self.url == self.driver.current_url:    
                return True
        raise PageNotOpenedExeption(
            f"{self.url} did not open in {timeout} sec, current url {self.driver.current_url}"
        )"""

    def close_cookie_banner(self):
        try:
            self.click(self.basic_locators.COOKIE_BANNER_BUTTON)
        except Exception as e:
            print(e)
            pass

    def close_banner(self):
        try:
            self.click(self.basic_locators.BANNER_BUTTON)
        except Exception as e:
            print(e)
            pass

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
    def find(self, locator, timeout=None):
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

    def fill(self, locator, text, timeout=None) -> WebElement:
        elem = self.find(locator, timeout=timeout)
        print(elem)
        elem.clear()
        elem.send_keys(text)
        return elem

    # Search for element by locator and click on it
    def click(self, locator, timeout=None) -> None:
        self.find(locator, timeout=timeout)
        elem = self.wait(timeout).until(EC.element_to_be_clickable(locator))
        elem.click()

    def multiple_find(self, locator, timeout=15):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located(locator)
        )

    def action_click(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        WebDriverWait(self.driver, 10).until(EC.visibility_of(element))
        actions = ActionChains(self.driver, 500)
        actions.move_to_element(element)
        actions.click(element)
        actions.perform()
        return self
