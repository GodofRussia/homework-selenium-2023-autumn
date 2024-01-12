import pytest
from tests.base_case import BaseCase, cookies_and_local_storage, credentials

from ui.pages.group_adv_page import GroupAdvPage
from ui.pages.consts import URLS, ERR_TEXT, INPUT_TEXT


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

        assert page.get_selected_region()

    def test_upper_limit(self, group_adv_page: GroupAdvPage):
        group_adv_page.get_page()
        group_adv_page.wait_load_page()
        group_adv_page.select_demograpy()

        group_adv_page.select_bottom_age(INPUT_TEXT.max_age)
        group_adv_page.select_upper_age(INPUT_TEXT.min_age)

        assert group_adv_page.get_upper_age() != INPUT_TEXT.min_age

    def test_lower_limit(self, group_adv_page: GroupAdvPage):
        group_adv_page.get_page()
        group_adv_page.wait_load_page()

        group_adv_page.select_demograpy()
        group_adv_page.select_upper_age(INPUT_TEXT.min_age)
        group_adv_page.select_bottom_age(INPUT_TEXT.max_age)

        assert group_adv_page.get_lower_age() != INPUT_TEXT.max_age

    def test_empty_region(self, group_adv_page: GroupAdvPage):
        group_adv_page.get_page()
        group_adv_page.wait_load_page()

        group_adv_page.click_continue_button()
        assert group_adv_page.is_on_site_text(ERR_TEXT.err_text)

    def test_key_phrases_error(self, group_adv_page: GroupAdvPage):
        group_adv_page.get_page().wait_load_page()

        group_adv_page.click_interest_region().click_key_phrases()
        group_adv_page.wait_key_phrase_render()
        group_adv_page.send_key_phrases(
            INPUT_TEXT.long_key_phrase_text
        ).click_continue_button()

        assert group_adv_page.is_on_site_text(ERR_TEXT.validation_failed)

    def test_key_phrases_duplicate(self, group_adv_page: GroupAdvPage):
        group_adv_page.get_page().wait_load_page()

        group_adv_page.click_interest_region().click_key_phrases()
        group_adv_page.wait_key_phrase_render()
        group_adv_page.send_key_phrases(INPUT_TEXT.key_phrase_text)
        group_adv_page.send_keys_phrases_minus(
            INPUT_TEXT.key_phrase_text
        )

        assert group_adv_page.is_on_site_text(ERR_TEXT.duplication_err)

    def test_key_devices(self, group_adv_page: GroupAdvPage):
        group_adv_page.get_page().wait_load_page()

        group_adv_page.click_device_region().remove_device(0).remove_device(1)

        assert group_adv_page.is_disabled_and_checked_device(1)

    def test_url(self, group_adv_page: GroupAdvPage):
        group_adv_page.get_page().wait_load_page()

        group_adv_page.click_url_region().wait_for_utm_render().select_utm()
        group_adv_page.wait_for_checkbox_load().send_text_url(
            URLS.bad_url
        ).click_continue_button()

        assert group_adv_page.is_utm_not_correct()
