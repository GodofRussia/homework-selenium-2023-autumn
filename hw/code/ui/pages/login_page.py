import time
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from ui.pages.lk_page import LKPage
from ui.pages.base_page import BasePage
from ui.locators.login import LoginPageLocators

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    url = "https://ads.vk.com/hq"
    locators = LoginPageLocators

    def login(self, user: str, password: str, timeout=None):
        self.fill(self.locators.LOGIN, user, timeout=timeout)

        self.click(self.locators.LOGIN_GO_ON_BOY_BUTTON, timeout=timeout)

        self.fill(self.locators.PASSWORD, password, timeout=timeout)

        self.click(self.locators.PASSWORD_GO_ON_BOY_BUTTON, timeout=timeout)
        # WebDriverWait(self.driver, 20).until(
        #     EC.presence_of_element_located((By.LINK_TEXT, "Блоги"))
        # )

        self.close_cookie_banner()

        print("login end")
        return LKPage(self.driver)
