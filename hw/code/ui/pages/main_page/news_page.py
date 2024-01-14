from ui.pages.base_page import BasePage
from ui.locators.main import MainPageLocators


class NewsPage(BasePage):
    url = "https://ads.vk.com/news"
    locators = MainPageLocators

