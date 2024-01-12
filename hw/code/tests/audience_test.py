import time

from tests.base_case import BaseCase, cookies_and_local_storage, credentials

from ui.pages.audience_page import AudiencePage
from ui.pages.consts import URLS, ERR_TEXT, INPUT_TEXT, LABELS


class TestAudience(BaseCase):
    authorize = True

    def test_open_creation_window(self, audience_page: AudiencePage):
        audience_page.click_create_button()

        assert audience_page.is_on_site_text(LABELS.create_auditory_text)

    def test_max_len_name(self, audience_page: AudiencePage):
        audience_page.click_create_button().write_text_to_name(
            INPUT_TEXT.string_256_symbols)

        assert audience_page.is_on_site_text(ERR_TEXT.len_err_auditory)

    def test_change_number_to_bigger(self, audience_page: AudiencePage):
        audience_page.click_create_button().click_add_source()
        audience_page.select_lead_region()
        audience_page.click_lead_input().select_lead_option()
        audience_page.click_checkbox_lead()

        audience_page.write_to_from_field(
            INPUT_TEXT.big_value_for_days)
        audience_page.write_to_to_field(
            INPUT_TEXT.small_value_for_days)

        assert audience_page.wait_to_filed_equal(INPUT_TEXT.big_value_for_days)

    def test_change_number_to_smaller(self, audience_page: AudiencePage):
        audience_page.click_create_button().click_add_source()
        audience_page.select_lead_region()
        audience_page.click_lead_input().select_lead_option()
        audience_page.click_checkbox_lead()

        audience_page.write_to_to_field(
            INPUT_TEXT.small_value_for_days)
        audience_page.write_to_from_field(
            INPUT_TEXT.big_value_for_days)

        assert audience_page.wait_from_filed_equal(
            INPUT_TEXT.small_value_for_days)

    def test_select_period_zero(self, audience_page: AudiencePage):
        audience_page.click_create_button().click_add_source()
        audience_page.select_key_phrases_region()

        audience_page.write_to_period(INPUT_TEXT.less_than_min_period)

        assert audience_page.wait_period_filed_equal(INPUT_TEXT.min_period)

    def test_select_period_big_value(self, audience_page: AudiencePage):
        audience_page.click_create_button().click_add_source()
        audience_page.select_key_phrases_region()

        audience_page.write_to_period(INPUT_TEXT.more_than_max_period)
        assert audience_page.wait_period_filed_equal(INPUT_TEXT.max_period)

    def test_user_list(self, audience_page: AudiencePage):
        audience_page.click_user_list()
        assert audience_page.is_user_list_url()

    def test_filter_vk_group(self, audience_page: AudiencePage):
        audience_page.click_create_button().click_add_source()
        audience_page.select_vk_group_region()
        audience_page.write_to_vk_group(URLS.vk_group_url).select_vk_group()
        audience_page.click_save_button_modal()

        name = audience_page.get_name_audience()
        audience_page.click_save_button()
        audience_page.select_vk_group_filter()

        assert audience_page.is_on_site_text(name)

    def test_delete_sources(self, audience_page: AudiencePage):
        audience_page.click_create_button().click_add_source()
        audience_page.select_vk_group_region()
        audience_page.write_to_vk_group(
            URLS.vk_group_url).select_vk_group()
        audience_page.click_save_button_modal()

        audience_page.delte_source()

        audience_page.click_save_button()

        assert audience_page.is_on_site_text(LABELS.create_auditory_text)
