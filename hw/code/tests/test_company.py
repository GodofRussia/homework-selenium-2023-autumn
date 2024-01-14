import time
import pytest
from tests.base_case import BaseCase
from ui.pages.company_page import CompanyPage
from ui.pages.adv_page import AdvPage
from ui.pages.group_adv_page import GroupAdvPage
from selenium.common.exceptions import TimeoutException

from ui.pages.consts import LABELS, URLS, ERR_TEXT, INPUT_TEXT, WaitTime


class TestCompany(BaseCase):
    authorize = True

    @pytest.fixture
    def preparations(self, company_page: CompanyPage):
        company_page.close_banner()
        yield company_page

    def test_create(self, preparations: CompanyPage):
        preparations.create_company()
        assert preparations.is_ad_plan()

    def test_group(self, preparations: CompanyPage):
        preparations.group_view()
        assert preparations.is_ad_groups()

    def test_advertisment(self, preparations):
        preparations.advertisment_view()
        assert preparations.is_advertisment()

    def test_list(self, preparations):
        preparations.select_action_list_without_wait()

        assert preparations.selector_has_not_pop_down()

    @pytest.fixture
    def setup_started_filters(self, preparations: CompanyPage):
        preparations.select_filter().select_started_filter().apply_filters()
        preparations.delete_all_companies()

        yield preparations
        preparations.select_filter().select_started_filter().apply_filters()

    def test_download(self, setup_started_filters: CompanyPage):
        setup_started_filters.download()
        assert not setup_started_filters.is_on_site_text(LABELS.date_sum)

    def test_settings(self, setup_started_filters):
        setup_started_filters.settings()
        assert not setup_started_filters.is_on_site_text(LABELS.config_table)

    @pytest.fixture
    def setup_filter(self, preparations: CompanyPage):
        preparations.select_filter().select_deleted_filter().apply_filters()
        yield preparations
        preparations.select_filter().select_deleted_filter().apply_filters()

    def test_select_company_settings(self, setup_filter: CompanyPage):
        setup_filter.select_company().settings()
        assert setup_filter.is_on_site_text(LABELS.config_table)

    def test_select_company_downloads(self, setup_filter: CompanyPage):
        setup_filter.select_company().download()
        assert setup_filter.is_on_site_text(
            LABELS.date_sum, WaitTime.MEDIUM_WAIT
        )

    @pytest.fixture
    def create_company(self, new_company_page):
        new_company_page.close_banner()
        page = AdvPage.__new__(AdvPage)
        page.driver = new_company_page.driver
        page.create_company(URLS.correct_url_text)

        company_page = CompanyPage(new_company_page.driver)
        company_page.select_filter().select_started_filter().apply_filters()
        yield company_page
        company_page.delete_all_companies()

    def test_company_deletion(self, create_company: CompanyPage):
        create_company.delete_all_companies()

        assert create_company.is_on_site_text(
            LABELS.nothing_found
        ) or create_company.is_on_site_text(LABELS.create_first)

    @pytest.fixture
    def create_draft(self, company_page: CompanyPage):
        company_page.close_banner()
        page = GroupAdvPage(company_page.driver)
        page.get_to_next()

        company_page.open()

        yield company_page

    def test_draft(self, create_draft: CompanyPage):
        create_draft.go_to_drafts()
        create_draft.delete_all_drafts()

        assert create_draft.is_on_site_text(LABELS.create_first)
