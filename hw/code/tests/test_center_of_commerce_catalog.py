from datetime import datetime, timezone, timedelta
import os
import pytest
import time
from tests.base_case import BaseCase
from ui.fixtures import download_directory
from ui.pages.center_of_commerce import CenterOfCommercePage
from time import gmtime, strftime

from ui.pages.consts import CatalogTabs, CosmeticProducts, Product, TopCosmeticProduct

TIMEOUT = 30
SHORT_TIMEOUT = 5
PRODUCTS_LOADING_TIMEOUT = 150
strftime("%Y-%m-%d %H:%M:%S", gmtime())


class TestCenterOfCommerceCatalog(BaseCase):
    authorize = True

    @pytest.fixture(scope="session")
    def catalogs_fixture(
        self,
        mock_files,
        center_of_commerce_page_session: CenterOfCommercePage,
        cookies_and_local_storage,
    ):
        center_of_commerce_page_session.set_cookie(cookies_and_local_storage)
        catalog_paramertries = [
            ("feed", "https://vk.com/luxvisage_cosmetics", "fff"),
            ("feed", "https://vk.com/market-204475787", "dddsdsd"),
            ("feed", "https://vk.com/voentorg_chipok", "Тачки"),
        ]

        for catalog_params in catalog_paramertries:
            second_field = catalog_params[1]
            if (
                catalog_params[0]
                == center_of_commerce_page_session.TABS.MANUAL
            ):
                second_field = os.path.join(mock_files, catalog_params[1])

            center_of_commerce_page_session.go_to_create_catalog(
                catalog_params[0],
                second_field,
                catalog_params[2],
                TIMEOUT,
            )
            center_of_commerce_page_session.create_catalog_finish(TIMEOUT)

            assert (
                center_of_commerce_page_session.find_catalog_tabs(TIMEOUT)
                is not None
            )
            assert (
                center_of_commerce_page_session.redirect_to_products_and_find_checkbox_select_products(
                    PRODUCTS_LOADING_TIMEOUT, SHORT_TIMEOUT
                )
                is not None
            )

            center_of_commerce_page_session = CenterOfCommercePage(
                center_of_commerce_page_session.driver
            )

        yield

        center_of_commerce_page_session = CenterOfCommercePage(
            center_of_commerce_page_session.driver
        )

        for catalog_params in catalog_paramertries:
            assert center_of_commerce_page_session.remove_catalog_by_title(
                "Товары – " + catalog_params[2], TIMEOUT
            )

            center_of_commerce_page_session = CenterOfCommercePage(
                center_of_commerce_page_session.driver
            )

    @pytest.mark.parametrize(
        "from_what, to",
        [
            ("Товары – fff", "Товары – dddsdsd"),
            ("Товары – Тачки", "Товары – fff"),
        ],
    )
    def test_catalog_category_switch_works(
        self,
        from_what,
        to,
        center_of_commerce_page: CenterOfCommercePage,
        cookies_and_local_storage,
        catalogs_fixture,
    ):
        center_of_commerce_page.go_to_catalog(from_what, TIMEOUT)
        center_of_commerce_page.switch_catalog(to, TIMEOUT)

        assert (
            center_of_commerce_page.find_catalog_title(to, TIMEOUT) is not None
        )

    @pytest.mark.parametrize(
        "catalog, tab",
        [
            ("Тачки", CatalogTabs.PRODUCTS),
            ("Тачки", CatalogTabs.GROUPS),
            ("Тачки", CatalogTabs.DIAGNOSTIC),
            ("Тачки", CatalogTabs.EVENTS),
            ("Тачки", CatalogTabs.DOWNLOADS_HISTORY),
            ("Товары – fff",CatalogTabs.DOWNLOADS_HISTORY),
            (
                "Товары – fff",
                CatalogTabs.DIAGNOSTIC
            ),
            (
                "Товары – fff",
                CatalogTabs.EVENTS,
            ),
        ],
    )
    def test_catalog_category_tabs_redirecting(
        self,
        catalog,
        tab,
        center_of_commerce_page: CenterOfCommercePage,
        cookies_and_local_storage,
        catalogs_fixture,
    ):
        center_of_commerce_page.go_to_catalog(catalog, TIMEOUT)
        center_of_commerce_page.switch_catalog_tab(tab, TIMEOUT)

        assert (
            center_of_commerce_page.check_catalog_tab_switched(tab, TIMEOUT)
            is not None
        )

    @pytest.mark.parametrize(
        "catalog, tab_id",
        [
            ("Тачки", CatalogTabs.PRODUCTS),
            ("Товары – fff", CatalogTabs.PRODUCTS),
        ],
    )
    def test_catalog_products_promote_works(
        self,
        catalog,
        tab,
        center_of_commerce_page: CenterOfCommercePage,
        cookies_and_local_storage,
        catalogs_fixture,
    ):
        center_of_commerce_page.go_to_catalog(catalog, TIMEOUT)
        center_of_commerce_page.switch_catalog_tab(tab, TIMEOUT)
        center_of_commerce_page.click_on_promote_button(TIMEOUT)

        assert center_of_commerce_page.find_promote_title(TIMEOUT) is not None

    @pytest.mark.parametrize(
        "catalog, product_id, title",
        [
            (
                "Товары – fff",
                CosmeticProducts[0],
            ),
            (
                "Товары – fff",
                CosmeticProducts[4],
            ),
        ],
    )
    def test_catalog_products_search(
        self,
        catalog,
        product: Product,
        center_of_commerce_page: CenterOfCommercePage,
        cookies_and_local_storage,
        catalogs_fixture,
    ):
        center_of_commerce_page.go_to_catalog(catalog, TIMEOUT)
        center_of_commerce_page.search_product(product.product_id, TIMEOUT)

        assert (
            center_of_commerce_page.find_product_by_title(product.title, TIMEOUT)
            is not None
        )

    @pytest.mark.parametrize("catalog", ["Товары – fff", "Товары – Тачки"])
    def test_catalog_products_table_settings_widget(
        self,
        catalog,
        center_of_commerce_page: CenterOfCommercePage,
        cookies_and_local_storage,
        catalogs_fixture,
    ):
        center_of_commerce_page.go_to_catalog(catalog, TIMEOUT)
        center_of_commerce_page.click_product_table_settings(TIMEOUT)

        assert (
            center_of_commerce_page.find_table_settings_title(TIMEOUT)
            is not None
        )

    @pytest.mark.parametrize(
        "catalog, product",
        [
            (
                "Товары – fff",
               CosmeticProducts[0]
            ),
            (
                "Товары – fff",
                CosmeticProducts[1]
            ),
        ],
    )
    def test_catalog_product_widget(
        self,
        catalog,
        product: Product,
        center_of_commerce_page: CenterOfCommercePage,
        cookies_and_local_storage,
        catalogs_fixture,
    ):
        center_of_commerce_page.go_to_catalog(catalog, TIMEOUT)
        center_of_commerce_page.go_to_catalog_product(
            product.product_id, product.title, TIMEOUT
        )

        assert (
            center_of_commerce_page.find_product_widget_by_title(product.title, TIMEOUT)
            is not None
        )

    @pytest.mark.parametrize(
        "catalog, product", [("Товары – fff", TopCosmeticProduct)]
    )
    def test_catalog_product_sort(
        self,
        catalog,
        product: Product,
        center_of_commerce_page: CenterOfCommercePage,
        cookies_and_local_storage,
    ):
        center_of_commerce_page.go_to_catalog(catalog, TIMEOUT)
        center_of_commerce_page.click_on_sort_products(TIMEOUT)

        assert (
            center_of_commerce_page.find_product_by_id(product.product_id, TIMEOUT)
            is not None
        )

    @pytest.mark.parametrize(
        "catalog, redirected_tab", [("Товары – fff", "Диагностика")]
    )
    def test_catalog_warning_button(
        self,
        catalog,
        redirected_tab,
        center_of_commerce_page: CenterOfCommercePage,
        cookies_and_local_storage,
        catalogs_fixture,
    ):
        center_of_commerce_page.go_to_catalog(catalog, TIMEOUT)
        center_of_commerce_page.click_on_warning_button(TIMEOUT)

        assert center_of_commerce_page.check_catalog_tab_switched(
            redirected_tab, TIMEOUT
        )
