import pytest
from tests.base_case import BaseCase
from ui.pages.lk_page import LKPage

from ui.pages.consts import SidebarTabsTitles

TIMEOUT = 30


class TestSidebar(BaseCase):
    authorize = True

    @pytest.mark.parametrize(
        "tab",
        [
            SidebarTabsTitles.COMPANIES,
            SidebarTabsTitles.AUDITORIES,
            SidebarTabsTitles.BUDGET,
            SidebarTabsTitles.LEARNING,
            SidebarTabsTitles.CENTER_OF_COMMERCE,
            SidebarTabsTitles.SITES,
            SidebarTabsTitles.MOBILE_APPS,
            SidebarTabsTitles.LEAD_FORMS,
            SidebarTabsTitles.SETTINGS,
            SidebarTabsTitles.HELP,
        ],
    )
    def test_tab_redirecting(
        self, tab, lk_page: LKPage, cookies_and_local_storage
    ):
        lk_page.close_banner()
        lk_page.switch_tab(tab, TIMEOUT)

        assert lk_page.check_tab_switched(tab, TIMEOUT)

    def test_wrap_works(self, lk_page: LKPage, cookies_and_local_storage):
        lk_page.close_banner()
        lk_page.click_on_wrap(TIMEOUT)

        assert lk_page.found_redirect_titles(TIMEOUT) is False
