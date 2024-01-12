import pytest

from tests.base_case import BaseCase, cookies_and_local_storage, credentials
from ui.pages.site_page import SitePage

from ui.pages.consts import URLS, ERR_TEXT, INPUT_TEXT


class TestSite(BaseCase):
    authorize = True

    def test_open_add_form(self, site_page: SitePage):
        site_page.click_add_button()
        assert site_page.is_domen_input_exist()

    @pytest.fixture
    def create_pixel_go_settings(self, site_page: SitePage):
        id = site_page.create_pixel()
        site_page.wait_for_pixel(id)
        site_page.click_settings_until_change()
        yield site_page

        site_page.open()

        while True:
            try:
                site_page.delete_pixel()
            except Exception as e:
                print(e)
                break

    @pytest.fixture
    def teardown_checkbox(self, create_pixel_go_settings: SitePage):
        site_page = create_pixel_go_settings
        site_page.select_collection_checkbox()
        yield site_page
        site_page.select_collection_checkbox()

    def test_valid_input(self, teardown_checkbox: SitePage):
        teardown_checkbox.input_collection_data(
            INPUT_TEXT.incorrect_input_data)

        # assert teardown_checkbox.is_error_on_page(
        #     ERR_TEXT.incorrect_value_err
        # )
        # XXX
        assert teardown_checkbox.is_on_site_text(
            ERR_TEXT.incorrect_value_err
        )

    def test_click_events(self, create_pixel_go_settings: SitePage):
        site_page = create_pixel_go_settings
        pixel_id = site_page.current_id()

        site_page.click_events()
        # TODO
        assert (
            site_page.get_url()
            == f"https://ads.vk.com/hq/pixels/{pixel_id}/events"
        )

    def test_click_tags(self, create_pixel_go_settings: SitePage):
        site_page = create_pixel_go_settings
        pixel_id = site_page.current_id()
        site_page.click_tags()
        # TODO
        assert (
            site_page.get_url()
            == f"https://ads.vk.com/hq/pixels/{pixel_id}/tags"
        )

    def test_click_access(self, create_pixel_go_settings: SitePage):
        site_page = create_pixel_go_settings
        pixel_id = site_page.current_id()
        site_page.click_access()
        # TODO
        assert (
            site_page.get_url()
            == f"https://ads.vk.com/hq/pixels/{pixel_id}/pixel_access"
        )

    def test_event_empty_category(self, create_pixel_go_settings: SitePage):
        site_page = create_pixel_go_settings
        site_page.click_events()
        site_page.click_add_event()
        site_page.click_add_event_modal()

        assert site_page.is_on_site_text(ERR_TEXT.empty_field_err)

    def test_event_max_size_name(self, create_pixel_go_settings: SitePage):
        site_page = create_pixel_go_settings
        site_page.click_events()
        site_page.click_add_event()
        site_page.click_add_event_modal().select_manual()
        site_page.input_event_name(INPUT_TEXT.string_256_symbols)
        site_page.select_event_category().select_event_condition()

        site_page.input_text_url(
            URLS.domen_vk_link).click_add_event_modal()

        assert site_page.is_on_site_text(
            ERR_TEXT.len_err_site
        )

    def test_click_tags_name(self, create_pixel_go_settings: SitePage):
        site_page = create_pixel_go_settings
        site_page.click_tags().click_add_tag()
        site_page.input_name_tag(INPUT_TEXT.string_256_symbols)

        assert not site_page.is_on_site_text(INPUT_TEXT.string_256_symbols)