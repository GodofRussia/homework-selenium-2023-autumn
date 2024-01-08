import pytest

from tests.base_case import BaseCase, cookies_and_local_storage, credentials

from ui.pages.adv_page import AdvPage


class TestAdv(BaseCase):
    authorize = True

    @pytest.fixture(scope="function")
    def get_page(self, adv_page: AdvPage):
        yield adv_page.get_page()

    def test_empty_fields(self, get_page: AdvPage):
        get_page.click_continue_button()

        assert get_page.is_on_site_text("ошибк")

    def test_more_chars_than_max(self, get_page: AdvPage):
        max_size = get_page.get_title_max()

        get_page.send_text_to_title(
            "слово" * (max_size // 5 + 1)
        ).click_continue_button()

        assert get_page.is_on_site_text("Превышена максимальная длина поля")

    def test_latin_symbols(self, get_page: AdvPage):
        get_page.send_text_to_title("word")

        assert get_page.is_on_site_text(
            "Используйте латиницу только там, где без неё не обойтись"
        )

    def test_wrong_site(self, get_page: AdvPage):
        get_page.send_url("https://labudiduba.com/")

        assert get_page.is_on_site_text(
            "Ссылка содержит запрещённый редирект на домен"
        )

    @pytest.fixture
    def upload_logo(self, get_page: AdvPage):
        get_page.upload_logo().wait_logo_dissapper()
        yield get_page

    def test_after_create_company(self, upload_logo: AdvPage):
        upload_logo.select_logo(0).write_to_inputs(
            "https://vk.com/"
        ).write_to_textarea("https://vk.com/")
        name = upload_logo.get_company_name()

        upload_logo.click_media_upload().select_media_options()
        upload_logo.add_media_option()
        upload_logo.click_continue_until_modal().click_send_button()

        assert upload_logo.is_on_site_text(name, 5)
