import re
import pytest
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from ui.pages.main_page.cases_page import CasesPage
from ui.pages.main_page.events_page import EventsPage
from ui.pages.main_page.ideas_forum_page import IdeasForumPage
from ui.pages.main_page.monetisation_page import MonetisationPage
from ui.pages.main_page.news_page import NewsPage
from ui.pages.main_page.useful_materials_page import UsefulMaterialsPage
from ui.pages.base_page import BasePage
from ui.locators.main import MainPageLocators
from selenium.webdriver.support.ui import Select

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class MainPage(BasePage):
    url = "https://ads.vk.com"
    locators = MainPageLocators

    def __init__(self, driver):
        super().__init__(driver)
        self.is_opened()

    def open_all_cases(self):
        # self.click_element_with_text('a', 'Смотреть все')
        elem = self.multiple_find(self.locators.ALL_CASES_BUTTON)[0]
        self.action_click(elem)

        return CasesPage(self.driver)
    
    def click_on_top_news(self):
        elem = self.find(self.locators.TOP_NEWS)
        self.action_click(elem)

        return NewsPage(self.driver)
    
    def click_on_vebinars(self):
        self.click(self.locators.VEBINARS_BUTTON)
        return EventsPage(self.driver)
    
    def click_on_know_more(self):
        # button = self.find(self.locators.KNOW_MORE_BUTTONS)[0]
        with self.wait_for_url_change():
            self.click(self.locators.KNOW_MORE_BUTTONS)
    
    def get_slide_text(self):
        carousel_top_elem = self.find(self.locators.CAROUSEL_TOP_TEXT)
        return carousel_top_elem.text

    def click_on_logo(self):
        self.click_element_with_class('a', 'HeaderLeft')
        return MainPage(self.driver)

    def go_to_news_page(self):
        self._click_on_navigation_element('Новости')
        return NewsPage(self.driver)

    def go_to_usefull_materials_page(self):
        self._dropdown_and_move_to('Полезные материалы')
        return UsefulMaterialsPage(self.driver)
        
    def go_to_events_page(self):
        self._dropdown_and_move_to('Мероприятия')
        return EventsPage(self.driver)

    def go_to_sertification_page(self):
        self._dropdown_and_move_to('Сертификация')

    def go_to_video_courses_page(self):
        self._dropdown_and_move_to('Видеокурсы')
        
    def go_to_ideas_forum_page(self):
        self._click_on_navigation_element('Форум идей')
        return IdeasForumPage(self.driver)

    def go_to_monetisation_page(self):
        self._click_on_navigation_element('Монетизация')
        return MonetisationPage(self.driver)

    def go_to_help_page(self):
        self._click_on_navigation_element('Справка')

    def _click_on_navigation_element(self, text: str, element='*'):
        self.click_element_with_text_and_class(element, text, 'Navigation')
    
    def _dropdown_and_move_to(self, header: str):
        dropdown = self.find(
            self.basic_locators.ELEMENT_WITH_TEXT_AND_CLASS('*', 'Обучение', 'Navigation')
        )
        events = self.find(
            self.basic_locators.ELEMENT_WITH_TEXT_AND_CLASS('*', header, 'Navigation')
        )

        action = ActionChains(self.driver).move_to_element(dropdown).move_to_element(events).click()
        action.perform()
