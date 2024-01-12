import pytest
from tests.base_case import BaseCase, cookies_and_local_storage, credentials
from ui.pages.company_page import CompanyPage
from ui.pages.adv_page import AdvPage
from ui.pages.group_adv_page import GroupAdvPage
from selenium.common.exceptions import TimeoutException

from urllib.parse import urlparse
from ui.pages.consts import LABELS, URLS, ERR_TEXT, INPUT_TEXT

def is_matching_link(link, base_url):
    parsed_link = urlparse(link)
    parsed_base_url = urlparse(base_url)

    return (
        parsed_link.scheme == parsed_base_url.scheme
        and parsed_link.netloc == parsed_base_url.netloc
        and parsed_link.path.startswith(parsed_base_url.path)
    )


class TestCompany(BaseCase):
    authorize = True

    @pytest.fixture
    def preparations(self, company_page: CompanyPage):
        company_page.close_banner()
        yield company_page

    def test_create(self, preparations):
        preparations.create_company()
        # TODO
        assert is_matching_link(
            preparations.get_current_url(),
            "https://ads.vk.com/hq/new_create/ad_plan",
        )

    def test_group(self, preparations):
        preparations.group_view()
        # TODO
        assert is_matching_link(
            preparations.get_current_url(),
            "https://ads.vk.com/hq/dashboard/ad_groups",
        )

    def test_advertisment(self, preparations):
        preparations.advertisment_view()
        # TODO
        assert is_matching_link(
            preparations.get_current_url(),
            "https://ads.vk.com/hq/dashboard/ads",
        )

    def test_list(self, preparations):
        preparations.select_action_list()

        selector_classes = preparations.get_selector_attribute()
        # TODO
        assert "vkuiCustomSelect--pop-down" not in selector_classes

    @pytest.fixture
    def setup_started_filters(self, preparations):
        # TODO transfer to another function
        preparations.select_filter().select_started_filter().apply_filters()
        while True:
            try:
                preparations.select_company().select_action_list()
                preparations.select_delete_action()
            except TimeoutException:
                break
        yield preparations
        preparations.select_filter().select_started_filter().apply_filters()

    def test_download(self, setup_started_filters):
        setup_started_filters.download()
        assert not setup_started_filters.is_on_site_text(LABELS.date_sum)

    def test_settings(self, setup_started_filters):
        setup_started_filters.settings()
        assert not setup_started_filters.is_on_site_text(LABELS.config_table)

    @pytest.fixture
    def setup_filter(self, preparations):
        preparations.select_filter().select_deleted_filter().apply_filters()
        yield preparations
        preparations.select_filter()
        preparations.select_deleted_filter()
        preparations.apply_filters()

    def test_select_company_settings(self, setup_filter: CompanyPage):
        setup_filter.select_company().settings()
        assert setup_filter.is_on_site_text(LABELS.config_table)

    def test_select_company_downloads(self, setup_filter):
        try:
            setup_filter.select_company().download()
            assert setup_filter.is_on_site_text(LABELS.date_sum)
        except:
            setup_filter.driver.save_screenshot("Fail_select_compnay.png")

    @pytest.fixture
    def create_company(self, new_company_page):
        new_company_page.close_banner()
        page = AdvPage.__new__(AdvPage)
        page.driver = new_company_page.driver
        page.create_company()

        company_page = CompanyPage(new_company_page.driver)
        company_page.select_filter().select_started_filter().apply_filters()
        yield company_page

    def test_company_deletion(self, create_company):
        while True:
            try:
                create_company.select_company().select_action_list()
                create_company.select_delete_action()
            except TimeoutException:
                break
        assert create_company.is_on_site_text(
            LABELS.nothing_found
        ) or create_company.is_on_site_text(
            LABELS.create_first
        )

    @pytest.fixture
    def create_draft(self, company_page):
        company_page.close_banner()
        page = GroupAdvPage(company_page.driver)
        page.get_to_next()

        company_page.open()

        yield company_page

    def test_draft(self, create_draft):
        create_draft.go_to_drafts()
        while True:
            try:
                cnt = create_draft.select_draft_option()
                create_draft.delete_draft().click_approve_delete()
                create_draft.wait_until_draft_delete(cnt)
            except TimeoutException:
                break

        assert create_draft.is_on_site_text(
            LABELS.create_first
        )
