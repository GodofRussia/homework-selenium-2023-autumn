from tests.base_case import BaseCase
from ui.pages.main_page.main_page import MainPage


class TestMainPage(BaseCase):
    authorize = False

    def test_carousel(self, main_page: MainPage):
        banner_txt = main_page.get_slide_text()
        banner_words = banner_txt.split()

        main_page.click_on_know_more()

        assert main_page.contains_any_word(
            banner_words
        ), "new page doesnt contain words from banner"
