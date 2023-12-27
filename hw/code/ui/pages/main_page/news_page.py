import re
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from ui.pages.base_page import BasePage
from ui.locators.main import MainPageLocators

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class NewsPage(BasePage):
    url = "https://ads.vk.com/news"
    locators = MainPageLocators

