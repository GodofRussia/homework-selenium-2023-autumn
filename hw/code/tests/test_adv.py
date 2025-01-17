import os
import pytest

from tests.base_case import BaseCase

from ui.pages.adv_page import AdvPage
from ui.pages.consts import (
    TEST_FILE_ADV_PAGE_NAME,
    URLS,
    ERR_TEXT,
    INPUT_TEXT,
    WaitTime,
)


class TestAdv(BaseCase):
    authorize = True

    @pytest.fixture(scope="function")
    def get_page(self, adv_page: AdvPage):
        yield adv_page.get_page()

    def test_empty_fields(self, get_page: AdvPage):
        get_page.click_continue_button()

        assert get_page.is_on_site_text(ERR_TEXT.err_text)

    def test_more_chars_than_max(self, get_page: AdvPage):
        max_size = get_page.get_title_max()

        get_page.send_text_to_title(
            INPUT_TEXT.text_to_max_size
            * (max_size // len(INPUT_TEXT.text_to_max_size) + 1)
        ).click_continue_button()

        assert get_page.is_on_site_text(ERR_TEXT.len_err_text)

    def test_latin_symbols(self, get_page: AdvPage):
        get_page.send_text_to_title(INPUT_TEXT.title_text)

        assert get_page.is_on_site_text(ERR_TEXT.latin_err_text)

    def test_wrong_site(self, get_page: AdvPage):
        get_page.send_url(URLS.banned_url)
        get_page.click_continue_button()

        assert get_page.is_on_site_text(
            URLS.redirect_url_err, WaitTime.LONG_WAIT
        )

    @pytest.fixture
    def upload_logo(self, get_page: AdvPage, mock_files):
        get_page.upload_logo(
            os.path.join(mock_files, TEST_FILE_ADV_PAGE_NAME)
        ).wait_logo_dissapper()
        yield get_page

    def test_after_create_company(self, upload_logo: AdvPage):
        upload_logo.select_logo().write_to_inputs(
            URLS.correct_url_text
        ).write_to_textarea(URLS.correct_url_text)
        name = upload_logo.get_company_name()

        upload_logo.click_media_upload().wait_load_upload_modal()
        upload_logo.select_media_options()
        upload_logo.add_media_option()
        upload_logo.click_continue_until_modal().click_send_button()

        assert upload_logo.is_on_site_text(name, 5)
