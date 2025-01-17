from datetime import datetime, timedelta
import time
import pytest
from ui.pages.lead_page import LeadPage
from tests.base_case import BaseCase
from ui.pages.new_company_page import NewCompanyPage

from selenium.webdriver.support import expected_conditions as EC

from datetime import datetime, timedelta
from ui.pages.consts import URLS, ERR_TEXT, INPUT_TEXT


class TestNewCompany(BaseCase):
    authorize = True

    @pytest.fixture
    def fill_site_field(self, new_company_page: NewCompanyPage):
        new_company_page.site_region_click().send_keys_site(URLS.test_site)
        yield new_company_page

    def test_min_value_cost(self, fill_site_field: NewCompanyPage):
        fill_site_field.send_cost(
            INPUT_TEXT.less_than_need_cost
        ).continue_click()

        assert fill_site_field.is_less_than_hundred()

    def test_empty_cost(self, fill_site_field: NewCompanyPage):
        fill_site_field.send_cost(INPUT_TEXT.empty_value).continue_click()

        assert fill_site_field.is_must_field()

    def test_empty_pred_cost(self, fill_site_field: NewCompanyPage):
        fill_site_field.click_selector_strategy().select_pred_cost()
        fill_site_field.send_cost(INPUT_TEXT.corrected_cost)
        fill_site_field.send_max_click_cost(INPUT_TEXT.empty_value)
        fill_site_field.continue_click()

        assert fill_site_field.is_must_field()

    def test_empty_catalog(self, new_company_page: NewCompanyPage):
        new_company_page.catalog_region_click().continue_click()
        assert new_company_page.is_must_field()

    def test_wrong_group(self, new_company_page: NewCompanyPage):
        new_company_page.catalog_region_click()
        new_company_page.select_vk_group(URLS.vk_group_incorrect_url)

        assert new_company_page.is_not_found_community()

    @pytest.fixture
    def create_lead(self, new_company_page: NewCompanyPage):
        driver = new_company_page.driver
        page = LeadPage.__new__(LeadPage)
        page.driver = driver
        page.open()
        page.create_lead()

        new_company_page.open()

        yield new_company_page

        page.open()
        page.delete_leads()

    def test_select_lead_again(self, create_lead: NewCompanyPage):
        create_lead.lead_region_click().select_split()
        create_lead.select_lead_click(0).select_lead_option()

        create_lead.select_lead_click(1)
        assert create_lead.is_already_selected()

    def test_date_last_not_sooner(self, new_company_page: NewCompanyPage):
        new_company_page.site_region_click().send_keys_site(URLS.test_site)
        new_company_page.click_date().select_prev_month().click_first_day()

        current_date: datetime = datetime.now()
        month_ago_date = current_date - timedelta(days=current_date.day)
        assert not new_company_page.is_on_site_text(
            f"01.${month_ago_date.month}.${month_ago_date.year}"
        )
