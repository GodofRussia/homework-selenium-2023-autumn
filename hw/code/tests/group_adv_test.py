import pytest
from tests.base_case import BaseCase, cookies_and_local_storage, credentials

from ui.pages.group_adv_page import GroupAdvPage


class TestGroup(BaseCase):
    authorize = True

    @pytest.fixture
    def select_region(self, group_adv_page: GroupAdvPage):
        group_adv_page.get_page()
        yield group_adv_page
        group_adv_page.remove_selected_region()

    def test_region_select(self, select_region: GroupAdvPage):
        page = select_region
        page.site_region_click()

        assert page.get_selected_region() is not None

    def test_upper_limit(self, group_adv_page: GroupAdvPage):
        group_adv_page.get_page()
        group_adv_page.wait_load_page()
        group_adv_page.select_demograpy()

        group_adv_page.select_bottom_age(15)
        group_adv_page.select_upper_age(14)

        assert group_adv_page.get_upper_age() != 14

    def test_lower_limit(self, group_adv_page: GroupAdvPage):
        group_adv_page.get_page()
        group_adv_page.wait_load_page()

        group_adv_page.select_demograpy()
        group_adv_page.select_upper_age(15)
        group_adv_page.select_bottom_age(16)

        assert group_adv_page.get_lower_age() != 16

    def test_empty_region(self, group_adv_page: GroupAdvPage):
        group_adv_page.get_page()
        group_adv_page.wait_load_page()

        group_adv_page.click_continue_button()
        assert group_adv_page.is_on_site_text("ошибка")

    def test_key_phrases_error(self, group_adv_page: GroupAdvPage):
        group_adv_page.get_page().wait_load_page()

        group_adv_page.click_interest_region().click_key_phrases().wait_key_phrase_render()
        group_adv_page.send_key_phrases(
            "строка1" * 71, 10
        ).click_continue_button()

        assert group_adv_page.is_on_site_text("validation_failed")

    def test_key_phrases_duplicate(self, group_adv_page: GroupAdvPage):
        group_adv_page.get_page().wait_load_page()

        group_adv_page.click_interest_region().click_key_phrases().wait_key_phrase_render()
        group_adv_page.send_key_phrases("строка1", 10).send_keys_phrases_minus(
            "строка1"
        )

        assert group_adv_page.is_on_site_text("У вас дублируются")

    def test_key_devices(self, group_adv_page: GroupAdvPage):
        group_adv_page.get_page().wait_load_page()

        group_adv_page.click_device_region().remove_device(0).remove_device(1)

        assert group_adv_page.is_disabled_and_cheked_device(1)

    def test_url(self, group_adv_page: GroupAdvPage):
        group_adv_page.get_page().wait_load_page()

        group_adv_page.click_url_region().wait_for_utm_render().select_utm().wait_for_checkbox_load().send_text_url(
            "adbbbsabasb"
        ).click_continue_button()

        assert group_adv_page.is_utm_not_correct()
