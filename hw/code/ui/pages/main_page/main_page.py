from ui.pages.main_page.cases_page import CasesPage
from ui.pages.main_page.events_page import EventsPage
from ui.pages.main_page.ideas_forum_page import IdeasForumPage
from ui.pages.main_page.monetisation_page import MonetisationPage
from ui.pages.main_page.news_page import NewsPage
from ui.pages.main_page.useful_materials_page import UsefulMaterialsPage
from ui.pages.main_page.help_page import HelpPage
from ui.pages.base_page import BasePage
from ui.pages.consts import (
    NavbarTabsTitles,
    MainPageExternalLinks,
    MainPageNavigationClass as Navigation,
)
from ui.locators.main import MainPageLocators

from selenium.webdriver.common.action_chains import ActionChains


class MainPage(BasePage):
    url = "https://ads.vk.com"
    locators = MainPageLocators

    EXTERNAL_LINKS = MainPageExternalLinks
    NAVBAR_TITLES = NavbarTabsTitles

    def open_all_cases(self):
        elem = self.multiple_find(self.locators.ALL_CASES_BUTTON)[0]
        self.action_click(elem)

        return CasesPage(self.driver, False, check_url=True)

    def click_on_top_news(self):
        elem = self.find(self.locators.TOP_NEWS)
        self.action_click(elem)

        return NewsPage(self.driver, False, check_url=True)

    def click_on_vebinars(self):
        self.click(self.locators.VEBINARS_BUTTON)
        return EventsPage(self.driver, False, check_url=True)

    def click_on_know_more(self):
        with self.wait_for_url_change():
            self.click(self.locators.KNOW_MORE_BUTTONS)

    def get_slide_text(self):
        carousel_top_elem = self.find(self.locators.CAROUSEL_TOP_TEXT)
        return carousel_top_elem.text

    # Navbar navigation

    def click_on_logo(self):
        self.click_element_with_class("a", "HeaderLeft")
        return MainPage(self.driver, False, check_url=True)

    def go_to_news_page(self):
        self._click_on_navigation_element(self.NAVBAR_TITLES.NEWS)
        return NewsPage(self.driver, False, check_url=True)

    def go_to_usefull_materials_page(self):
        self._dropdown_and_move_to(
            self.NAVBAR_TITLES.STUDY_DROPDOWN.USEFULL_MATERIALS
        )
        return UsefulMaterialsPage(self.driver, False, check_url=True)

    def go_to_events_page(self):
        self._dropdown_and_move_to(self.NAVBAR_TITLES.STUDY_DROPDOWN.EVENTS)
        return EventsPage(self.driver, False, check_url=True)

    def go_to_sertification_page(self):
        with self.wait_for_new_tab_open():
            self._dropdown_and_move_to(
                self.NAVBAR_TITLES.STUDY_DROPDOWN.SERTIFICATION
            )

    def go_to_video_courses_page(self):
        with self.wait_for_new_tab_open():
            self._dropdown_and_move_to(
                self.NAVBAR_TITLES.STUDY_DROPDOWN.COURSES
            )

    def go_to_ideas_forum_page(self):
        self._click_on_navigation_element(self.NAVBAR_TITLES.IDEAS_FORUM)
        return IdeasForumPage(self.driver, False, check_url=True)

    def go_to_monetisation_page(self):
        self._click_on_navigation_element(self.NAVBAR_TITLES.MONETISATION)
        return MonetisationPage(self.driver, False, check_url=True)

    def go_to_help_page(self):
        self._click_on_navigation_element(self.NAVBAR_TITLES.HELP)
        return HelpPage(self.driver, False, check_url=True)

    def get_active_tab_text(self):
        return self.find(self.locators.ACTIVE_NAVBAR_TAB).text

    def _click_on_navigation_element(self, text: str, element="*"):
        self.click_element_with_text_and_class(element, text, Navigation)

    def _dropdown_and_move_to(self, header: str):
        dropdown = self.find(
            self.basic_locators.ELEMENT_WITH_TEXT_AND_CLASS(
                "*", self.NAVBAR_TITLES.STUDY, Navigation
            )
        )

        action = ActionChains(self.driver).move_to_element(dropdown).click()
        action.perform()

        elem = self.find(
            self.basic_locators.ELEMENT_WITH_TEXT_AND_CLASS(
                "*", header, Navigation
            )
        )

        self.action_click(elem)
