import pytest
import time
from tests.base_case import BaseCase
from ui.pages.login_page import LoginPage
from ui.pages.main_page.main_page import MainPage

from selenium.common.exceptions import TimeoutException


class TestNavbarMainPage(BaseCase):
    authorize = False

    def test_go_to_news_page(self, main_page: MainPage):
        main_page.go_to_news_page()

        assert main_page.get_active_tab_text() == main_page.NAVBAR_TITLES.NEWS

    def test_go_to_sertification_page(self, main_page: MainPage):
        main_page.go_to_sertification_page()

        with self.switch_to_window(True):
            assert (
                self.driver.current_url
                == main_page.EXTERNAL_LINKS.SERTIFICATION_URL
            )

    def test_go_to_courses_page(self, main_page: MainPage):
        main_page.go_to_video_courses_page()

        with self.switch_to_window(True):
            assert (
                self.driver.current_url == main_page.EXTERNAL_LINKS.COURSES_URL
            )

    def test_go_to_usefull_materials_page(self, main_page: MainPage):
        main_page.go_to_usefull_materials_page()

        assert main_page.get_active_tab_text() == main_page.NAVBAR_TITLES.STUDY

    def test_go_to_events_page(self, main_page: MainPage):
        main_page.go_to_events_page()

        assert main_page.get_active_tab_text() == main_page.NAVBAR_TITLES.STUDY

    def test_go_to_ideas_forum_page(self, main_page: MainPage):
        main_page.go_to_ideas_forum_page()

        assert (
            main_page.get_active_tab_text()
            == main_page.NAVBAR_TITLES.IDEAS_FORUM
        )

    def go_to_monetisation_page(self, main_page: MainPage):
        main_page.go_to_monetisation_page()

        assert (
            main_page.get_active_tab_text()
            == main_page.NAVBAR_TITLES.MONETISATION
        )

    def test_go_to_help_page(self, main_page: MainPage):
        main_page.go_to_help_page()

        assert main_page.get_active_tab_text() == main_page.NAVBAR_TITLES.HELP
