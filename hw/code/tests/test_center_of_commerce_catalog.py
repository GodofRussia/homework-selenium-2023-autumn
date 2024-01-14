from datetime import datetime, timezone, timedelta
import os
import pytest
import time
from tests.base_case import BaseCase
from ui.fixtures import download_directory
from ui.pages.center_of_commerce import CenterOfCommercePage
from time import gmtime, strftime

from ui.pages.consts import CatalogTabs, CosmeticProducts, Product, TopCosmeticProduct, CatalogsToBeCreated

TIMEOUT = 30
SHORT_TIMEOUT = 5
PRODUCTS_LOADING_TIMEOUT = 150
strftime("%Y-%m-%d %H:%M:%S", gmtime())

# TODO:
    # конфликты
    # проверить принты и слипы

class TestCenterOfCommerceCatalog(BaseCase):
    authorize = True

    @pytest.fixture(scope="session")
    def setup_catalogs(
        self,
        mock_files,
        center_of_commerce_page_session: CenterOfCommercePage,
        cookies_and_local_storage,
    ):
        center_of_commerce_page_session.set_cookie(cookies_and_local_storage)

        for catalog in CatalogsToBeCreated:
            field = catalog.url
            if (
                catalog.tab
                == center_of_commerce_page_session.TABS.MANUAL
            ):
                field = os.path.join(mock_files, field)

            center_of_commerce_page_session.go_to_create_catalog(
                catalog.tab,
                field,
                catalog.title,
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

        center_of_commerce_page_session.set_cookie(cookies_and_local_storage)

        for catalog in CatalogsToBeCreated:
            assert center_of_commerce_page_session.remove_catalog_by_title(
                catalog.title, TIMEOUT
            )

            center_of_commerce_page_session = CenterOfCommercePage(
                center_of_commerce_page_session.driver
            )


    @pytest.mark.parametrize(
        "from_what, to",
        [
            (CatalogsToBeCreated[0].title, CatalogsToBeCreated[1].title),
            (CatalogsToBeCreated[1].title, CatalogsToBeCreated[0].title),
        ],
    )
    def test_catalog_category_switch_works(
        self,
        from_what,
        to,
        center_of_commerce_page: CenterOfCommercePage,
        cookies_and_local_storage,
        setup_catalogs,
    ):
        center_of_commerce_page.go_to_catalog(from_what, TIMEOUT)
        center_of_commerce_page.switch_catalog(to, SHORT_TIMEOUT)

        assert (
            center_of_commerce_page.find_catalog_title(to, SHORT_TIMEOUT) is not None
        )


    @pytest.mark.parametrize(
        "catalog, tab",
        [
            (CatalogsToBeCreated[2].title, CatalogTabs.PRODUCTS),
            (CatalogsToBeCreated[2].title, CatalogTabs.DOWNLOADS_HISTORY),
        ],
    )
    def test_catalog_category_tabs_redirecting(
        self,
        catalog,
        tab,
        center_of_commerce_page: CenterOfCommercePage,
        cookies_and_local_storage,
        setup_catalogs,
    ):
        center_of_commerce_page.go_to_catalog(catalog, TIMEOUT)
        center_of_commerce_page.switch_catalog_tab(tab, TIMEOUT)

        assert (
            center_of_commerce_page.check_catalog_tab_switched(tab, TIMEOUT)
            is not None
        )

    @pytest.mark.parametrize(
        "catalog",
        [
            (CatalogsToBeCreated[2].title),
            (CatalogsToBeCreated[0].title),
        ],
    )
    def test_catalog_products_promote_works(
        self,
        catalog,
        center_of_commerce_page: CenterOfCommercePage,
        cookies_and_local_storage,
        setup_catalogs,
    ):
        tab = CatalogTabs.PRODUCTS

        center_of_commerce_page.go_to_catalog(catalog, TIMEOUT)
        center_of_commerce_page.switch_catalog_tab(tab, TIMEOUT)
        center_of_commerce_page.click_on_promote_button(TIMEOUT)

        assert center_of_commerce_page.find_promote_title(TIMEOUT) is not None

    @pytest.mark.parametrize(
        "catalog, product",
        [
            (
                CatalogsToBeCreated[0].title,
                CosmeticProducts[0],
            ),
            (
                CatalogsToBeCreated[0].title,
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
        setup_catalogs,
    ):
        center_of_commerce_page.go_to_catalog(catalog, TIMEOUT)
        center_of_commerce_page.search_product(product.product_id, TIMEOUT)

        assert (
            center_of_commerce_page.find_product_by_title(product.title, TIMEOUT)
            is not None
        )

    @pytest.mark.parametrize("catalog", [CatalogsToBeCreated[0].title, CatalogsToBeCreated[2].title])
    def test_catalog_products_table_settings_widget(
        self,
        catalog,
        center_of_commerce_page: CenterOfCommercePage,
        cookies_and_local_storage,
        setup_catalogs,
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
                CatalogsToBeCreated[0].title,
                CosmeticProducts[0]
            ),
            (
                CatalogsToBeCreated[0].title,
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
        setup_catalogs,
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
        "catalog, product", [(CatalogsToBeCreated[0].title, TopCosmeticProduct)]
    )
    def test_catalog_product_sort(
        self,
        catalog,
        product: Product,
        center_of_commerce_page: CenterOfCommercePage,
        cookies_and_local_storage,
        setup_catalogs,
    ):
        center_of_commerce_page.go_to_catalog(catalog, TIMEOUT)
        center_of_commerce_page.click_on_sort_products(TIMEOUT)

        assert (
            center_of_commerce_page.find_product_by_id(product.product_id, TIMEOUT)
            is not None
        )

    @pytest.mark.parametrize(
        "catalog, redirected_tab", [(CatalogsToBeCreated[0].title, CatalogTabs.DIAGNOSTIC)]
    )
    def test_catalog_warning_button(
        self,
        catalog,
        redirected_tab,
        center_of_commerce_page: CenterOfCommercePage,
        cookies_and_local_storage,
        setup_catalogs,
    ):
        center_of_commerce_page.go_to_catalog(catalog, TIMEOUT)
        center_of_commerce_page.click_on_warning_button(TIMEOUT)

        assert center_of_commerce_page.check_catalog_tab_switched(
            redirected_tab, TIMEOUT
        )
