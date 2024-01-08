import time

from tests.base_case import BaseCase, cookies_and_local_storage, credentials

from ui.pages.audience_page import AudiencePage


class TestAudience(BaseCase):
    authorize = True

    def test_open_creation_window(self, audience_page: AudiencePage):
        audience_page.click_create_button()

        assert audience_page.is_on_site_text("Создание аудитории")

    def test_max_len_name(self, audience_page: AudiencePage):
        audience_page.click_create_button().write_text_to_name("a" * 256)

        assert audience_page.is_on_site_text("Максимальная длина 255 символов")

    def test_change_number_to_bigger(self, audience_page: AudiencePage):
        audience_page.click_create_button().click_add_source()
        audience_page.select_lead_region()
        audience_page.click_lead_input().select_lead_option()
        audience_page.click_checkbox_lead()

        audience_page.write_to_from_field(10).write_to_to_field(5)

        assert audience_page.wait_to_filed_equal(10)

    def test_change_number_to_smaller(self, audience_page: AudiencePage):
        audience_page.click_create_button().click_add_source()
        audience_page.select_lead_region()
        audience_page.click_lead_input().select_lead_option()
        audience_page.click_checkbox_lead()

        audience_page.write_to_to_field(5).write_to_from_field(6)

        assert audience_page.wait_from_filed_equal(5)

    def test_select_period_zero(self, audience_page: AudiencePage):
        audience_page.click_create_button().click_add_source()
        audience_page.select_key_phrases_region()
        
        audience_page.write_to_period(0)

        assert audience_page.wait_period_filed_equal(1)

    def test_select_period_big_value(self, audience_page: AudiencePage):
        audience_page.click_create_button().click_add_source()
        audience_page.select_key_phrases_region()

        audience_page.write_to_period(9999)
        assert audience_page.wait_period_filed_equal(30)

    def test_user_list(self, audience_page: AudiencePage):
        audience_page.click_user_list()
        assert audience_page.is_user_list_url()

    def test_filter_vk_group(self, audience_page: AudiencePage):
        audience_page.click_create_button().click_add_source()
        audience_page.select_vk_group_region()
        audience_page.write_to_vk_group("vk.com/vkeducation").select_vk_group()
        audience_page.click_save_button_modal()

        name = audience_page.get_name_audience()
        audience_page.click_save_button()
        audience_page.select_vk_group_filter()

        assert audience_page.is_on_site_text(name)

    def test_delete_sources(self, audience_page: AudiencePage):
        audience_page.click_create_button().click_add_source()
        audience_page.select_vk_group_region()
        audience_page.write_to_vk_group("vk.com/vkeducation").select_vk_group()
        audience_page.click_save_button_modal()

        audience_page.delte_source()

        audience_page.click_save_button()

        assert audience_page.is_on_site_text("Создание аудитории")
