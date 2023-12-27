import pytest
from tests.base_case import BaseCase, credentials
from tests.base_case import cookies_and_local_storage
from ui.pages.lk_page import LKPage

TIMEOUT = 30

class TestSidebar(BaseCase):
    authorize = True

    @pytest.mark.parametrize("tab", ["Кампании", "Аудитории", "Бюджет", "Обучение", "Центр коммерции", "Сайты", "Мобильные приложения", "Лид-формы", "Настройки", "Помощь"])
    def test_tab_redirecting(self, tab, lk_page: LKPage, cookies_and_local_storage):
        lk_page.close_banner(15)
        lk_page.switch_tab(tab, TIMEOUT)

        assert lk_page.check_tab_switched(tab, TIMEOUT)

    def test_wrap_works(self, lk_page: LKPage, cookies_and_local_storage):
        lk_page.close_banner()
        lk_page.click_on_wrap(TIMEOUT)

        assert lk_page.found_redirect_titles(TIMEOUT) is False
    