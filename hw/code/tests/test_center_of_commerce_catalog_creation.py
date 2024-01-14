import pytest
import time
from tests.base_case import BaseCase
from ui.pages.center_of_commerce import CenterOfCommercePage
from time import gmtime, strftime
import os
from selenium.common.exceptions import TimeoutException

from ui.pages.consts import (
    CatalogPeriods,
    CenterOfCommerceTabs as TABS,
    MarketPlaceApiInput,
)

TIMEOUT = 30

strftime("%Y-%m-%d %H:%M:%S", gmtime())


class TestCenterOfCommerceCatalogCreation(BaseCase):
    authorize = True

    def test_creation_catalog_started(
        self,
        center_of_commerce_page: CenterOfCommercePage,
        cookies_and_local_storage,
    ):
        center_of_commerce_page.close_banner()
        center_of_commerce_page.start_creating_catalog(TIMEOUT)

        assert (
            center_of_commerce_page.find_new_catalog_title(TIMEOUT) is not None
        )

    def test_creation_title_name_required_message(
        self,
        center_of_commerce_page: CenterOfCommercePage,
        cookies_and_local_storage,
    ):
        center_of_commerce_page.close_banner()
        center_of_commerce_page.start_creating_catalog(TIMEOUT)
        center_of_commerce_page.clear_catalog_title(TIMEOUT)
        center_of_commerce_page.create_catalog_finish(TIMEOUT)

        assert (
            center_of_commerce_page.find_necessary_field_error_while_creation(
                TIMEOUT
            )
            is not None
        )

    @pytest.mark.parametrize(
        "tab",
        [(TABS.FEED), (TABS.MARKETPLACE), (TABS.MANUAL)],
    )
    def test_url_field_error_message(
        self,
        tab,
        center_of_commerce_page: CenterOfCommercePage,
        cookies_and_local_storage,
    ):
        center_of_commerce_page.close_banner()
        center_of_commerce_page.start_creating_catalog(TIMEOUT)
        center_of_commerce_page.click_on_tab(tab, TIMEOUT)
        center_of_commerce_page.create_catalog_finish(TIMEOUT)

        assert (
            center_of_commerce_page.find_necessary_field_error(tab, TIMEOUT)
            is not None
        )

    @pytest.mark.parametrize(
        "tab,url", [(TABS.FEED, "ddd"), (TABS.MARKETPLACE, "dda")]
    )
    def test_creation_url_field_protocol_message(
        self,
        tab,
        url,
        center_of_commerce_page: CenterOfCommercePage,
        cookies_and_local_storage,
    ):
        center_of_commerce_page.close_banner()
        center_of_commerce_page.start_creating_catalog(TIMEOUT)
        center_of_commerce_page.click_on_tab(tab)
        center_of_commerce_page.fill_url_input(url)
        center_of_commerce_page.create_catalog_finish(TIMEOUT)

        assert center_of_commerce_page.find_https_error(TIMEOUT) is not None

    @pytest.mark.parametrize(
        "period",
        [
            (CatalogPeriods.EVERYDAY),
            (CatalogPeriods.ONE_HOUR),
            (CatalogPeriods.FOUR_HOURS),
            (CatalogPeriods.EIGHT_HOURS),
        ],
    )
    def test_creation_period_selector(
        self,
        period,
        center_of_commerce_page: CenterOfCommercePage,
        cookies_and_local_storage,
    ):
        center_of_commerce_page.go_to_create_feed_catalog(TIMEOUT)
        center_of_commerce_page.try_close_study_banner()
        center_of_commerce_page.set_refresh_period(period, TIMEOUT)

        assert (
            center_of_commerce_page.find_by_period(period, TIMEOUT) is not None
        )

    @pytest.mark.parametrize(
        "url", ["https://vk.com/fa_sales", "https://vk.com/motorprod"]
    )
    def test_creation_only_with_3andmore_products(
        self,
        url,
        center_of_commerce_page: CenterOfCommercePage,
        cookies_and_local_storage,
    ):
        center_of_commerce_page.go_to_create_feed_catalog(TIMEOUT)
        center_of_commerce_page.fill_url_input(url, TIMEOUT)

        assert (
            center_of_commerce_page.find_not_enough_products_banner(TIMEOUT)
            is not None
        )

    @pytest.mark.parametrize("url", ["https://vk.com/ninoauto"])
    def test_creation_clear_utm_working(
        self,
        url,
        center_of_commerce_page: CenterOfCommercePage,
        cookies_and_local_storage,
    ):
        center_of_commerce_page.go_to_create_feed_catalog(TIMEOUT)
        center_of_commerce_page.click_on_clear_utm_checkbox(TIMEOUT)
        center_of_commerce_page.fill_url_input(url, TIMEOUT)
        center_of_commerce_page.clear_url_input(TIMEOUT)

        assert (
            center_of_commerce_page.check_clear_utm_checkbox_is_checked(
                TIMEOUT
            )
            is True
        )

    def test_hover_on_checkbox_label_working(
        self,
        center_of_commerce_page: CenterOfCommercePage,
        cookies_and_local_storage,
    ):
        center_of_commerce_page.go_to_create_feed_catalog(TIMEOUT)
        center_of_commerce_page.try_close_study_banner()

        assert center_of_commerce_page.check_utm_hover(TIMEOUT)

    @pytest.mark.parametrize("url", ["https://vk.com/ninoauto"])
    def test_creation_marketplace_error_incorrect_url(
        self,
        url,
        center_of_commerce_page: CenterOfCommercePage,
        cookies_and_local_storage,
    ):
        center_of_commerce_page.go_to_create_marketplace_catalog(TIMEOUT)
        center_of_commerce_page.fill_url_input(url, TIMEOUT)
        center_of_commerce_page.create_catalog_finish(TIMEOUT)

        assert (
            center_of_commerce_page.find_incorrect_marketplace_url_error(
                TIMEOUT
            )
            is not None
        )

    @pytest.mark.parametrize(
        "url, href1, href2",
        [
            (
                "https://www.wildberries.ru/brands/crocs/all",
                "https://seller.wildberries.ru/login/",
                "https://openapi.wildberries.ru",
            ),
            (
                "https://www.ozon.ru/seller/qika-1210208/odezhda-obuv-i-aksessuary-7500/?miniapp=seller_1210208",
                "https://seller.ozon.ru/app/settings/api-keys",
                "https://seller-edu.ozon.ru/docs/api-ozon/how-to-api.html",
            ),
            (
                "https://aliexpress.ru/store/1102452055?g=y&page=1&spm=a2g2w.detail.0.0.56762b41CeVj0X",
                "https://business.aliexpress.ru/docs/api-token",
                "https://business.aliexpress.ru/docs/quick-start#heading-shagi-dlya-integratsii-s-lokalnim-api",
            ),
        ],
    )
    def test_creation_marketplace_hrefs_found(
        self,
        url,
        href1,
        href2,
        center_of_commerce_page: CenterOfCommercePage,
        cookies_and_local_storage,
    ):
        center_of_commerce_page.go_to_create_marketplace_catalog(TIMEOUT)
        center_of_commerce_page.fill_url_input(url, TIMEOUT)

        assert (
            center_of_commerce_page.find_link_with_href(href1, TIMEOUT)
            is not None
        )

        assert (
            center_of_commerce_page.find_link_with_href(href2, TIMEOUT)
            is not None
        )

    @pytest.mark.parametrize(
        "url, apikey, input_type, client_id",
        [
            (
                "https://www.wildberries.ru/brands/crocs/all",
                "eee",
                MarketPlaceApiInput.KEY,
                "",
            ),
            (
                "https://www.ozon.ru/seller/qika-1210208/odezhda-obuv-i-aksessuary-7500/?miniapp=seller_1210208",
                "aaa",
                MarketPlaceApiInput.KEY,
                "aa",
            ),
            (
                "https://aliexpress.ru/store/1102452055?g=y&page=1&spm=a2g2w.detail.0.0.56762b41CeVj0X",
                "bbb",
                MarketPlaceApiInput.TOKEN,
                "",
            ),
        ],
    )
    def test_creation_marketplace_invalid_api_key_error(
        self,
        url,
        apikey,
        input_type,
        client_id,
        center_of_commerce_page: CenterOfCommercePage,
        cookies_and_local_storage,
    ):
        center_of_commerce_page.go_to_create_marketplace_catalog(TIMEOUT)
        center_of_commerce_page.fill_url_input(url, TIMEOUT)
        center_of_commerce_page.fill_client_id_input(client_id, TIMEOUT)
        center_of_commerce_page.fill_api_key_input(input_type, apikey, TIMEOUT)
        center_of_commerce_page.create_catalog_finish(TIMEOUT)

        assert (
            center_of_commerce_page.find_validation_failed_notification(
                TIMEOUT
            )
            is not None
        )

        assert (
            center_of_commerce_page.find_invalid_apikey_error(TIMEOUT)
            is not None
        )

    @pytest.mark.parametrize(
        "url, apikey, input_type, client_id",
        [
            (
                "https://www.wildberries.ru/brands/crocs/all",
                "ааа",
                MarketPlaceApiInput.KEY,
                "",
            ),
            (
                "https://www.ozon.ru/seller/qika-1210208/odezhda-obuv-i-aksessuary-7500/?miniapp=seller_1210208",
                "ььь",
                MarketPlaceApiInput.KEY,
                "aa",
            ),
            (
                "https://aliexpress.ru/store/1102452055?g=y&page=1&spm=a2g2w.detail.0.0.56762b41CeVj0X",
                "ввв",
                MarketPlaceApiInput.TOKEN,
                "",
            ),
        ],
    )
    def test_creation_marketplace_encoding_api_key_error(
        self,
        url,
        apikey,
        input_type,
        client_id,
        center_of_commerce_page: CenterOfCommercePage,
        cookies_and_local_storage,
    ):
        center_of_commerce_page.go_to_create_marketplace_catalog(TIMEOUT)
        center_of_commerce_page.fill_url_input(url, TIMEOUT)
        center_of_commerce_page.fill_client_id_input(client_id, TIMEOUT)
        center_of_commerce_page.fill_api_key_input(input_type, apikey, TIMEOUT)
        center_of_commerce_page.create_catalog_finish(TIMEOUT)

        assert (
            center_of_commerce_page.find_validation_failed_notification(
                TIMEOUT
            )
            is not None
        )

        assert (
            center_of_commerce_page.find_invalid_apikey_string_encoding_error(
                TIMEOUT
            )
            is not None
        )

    @pytest.mark.parametrize(
        "category",
        ["Авто", "Авиарейсы", "Товары", "Гостиницы", "Недвижимость", "Услуги"],
    )
    def test_creation_manual_category_selector(
        self,
        category,
        center_of_commerce_page: CenterOfCommercePage,
        cookies_and_local_storage,
    ):
        center_of_commerce_page.go_to_create_manual_catalog(TIMEOUT)
        center_of_commerce_page.set_category(category, TIMEOUT)

        assert (
            center_of_commerce_page.find_category_on_download(
                category, TIMEOUT
            )
            is not None
        )

    @pytest.mark.parametrize(
        "category, file_path",
        [
            ("Авто", "catalog_auto_google.csv"),
            ("Авиарейсы", "feed_flight_google.csv"),
            ("Товары", "catalog_products.csv"),
            ("Гостиницы", "hotels_feed_example.csv"),
            ("Недвижимость", "catalog_realty.csv"),
            ("Услуги", "catalog_services.csv"),
        ],
    )
    def test_creation_manual_category_files_downloading(
        self,
        category,
        file_path,
        center_of_commerce_page: CenterOfCommercePage,
        cookies_and_local_storage,
        download_directory,
    ):
        center_of_commerce_page.go_to_create_manual_catalog(TIMEOUT)
        center_of_commerce_page.set_category(category, TIMEOUT)

        center_of_commerce_page.click_on_category_to_download(
            category, TIMEOUT
        )
        timeout = TIMEOUT

        file_path = os.path.join(download_directory, file_path)

        existence = center_of_commerce_page.wait_for_file_to_download(
            file_path
        )

        os.remove(file_path)

        assert existence

    @pytest.mark.parametrize(
        "category, file",
        [
            ("Авто", "catalog_auto_google.csv"),
            ("Авиарейсы", "feed_flight_google.csv"),
            ("Товары", "catalog_products.csv"),
            ("Гостиницы", "hotels_feed_example.csv"),
            ("Недвижимость", "catalog_realty.csv"),
            ("Услуги", "catalog_services.csv"),
        ],
    )
    def test_manual_creation_files_uploading(
        self,
        category,
        file,
        center_of_commerce_page: CenterOfCommercePage,
        cookies_and_local_storage,
        mock_files,
    ):
        center_of_commerce_page.go_to_create_manual_catalog(TIMEOUT)
        center_of_commerce_page.set_category(category, TIMEOUT)

        file_path = os.path.join(mock_files, file)
        center_of_commerce_page.fill_file_input(file_path, TIMEOUT)
        with pytest.raises(TimeoutException):
            center_of_commerce_page.find_file_downloading_error(10)

        assert (
            center_of_commerce_page.find_downloaded_file(TIMEOUT) is not None
        )
