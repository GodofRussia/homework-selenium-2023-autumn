import re
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from ui.pages.base_page import BasePage
from ui.locators.main import MainPageLocators

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class UsefulMaterialsPage(BasePage):
    url = "https://ads.vk.com/insights"
    locators = MainPageLocators

    def __init__(self, driver):
        super().__init__(driver)
        self.is_opened()
        