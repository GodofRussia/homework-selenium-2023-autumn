import os
import time
from typing import List

from ui.pages.base_page import BasePage
from ui.locators.center_of_commerce import CenterOfCommerceLocators

from ui.pages.consts import (
    HOVER,
    CenterOfCommerceTabs,
    CatalogPeriods,
    CatalogTabs,
    CENTER_OF_COMMERCE_TABLE_SETTINGS,
    INVALID_API_KEY_ENCODING_ERROR,
    INVALID_API_KEY_ERROR,
    CENTER_OF_COMMERCE_CLIENT_ID_INPUT_TXT,
    CENTER_OF_COMMERCE_VK_PRODUCT_HREF,
    SEARCH_PRODUCT_CLASS,
    TITLE_CLASS,
    INVALID_MARKETPLACE_URL,
    SEARCH_CATALOG_CLASS,
    CONTENT_CLASS,
    WARNING_PROTOCOL_REQUIRED,
    REQUIRED_FIELD,
    NEW_CATALOG_TITLE,
    PRODUCTS_TAB_ID,
    SPAN,
    INPUT,
    DIV,
    H2,
    HREF,
    CATALOG_TITLE_PREFIX,
)

from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoAlertPresentException


class NoSuchPeriodException(Exception):
    pass


class CenterOfCommercePage(BasePage):
    url = "https://ads.vk.com/hq/ecomm/catalogs"
    locators = CenterOfCommerceLocators

    TABS = CenterOfCommerceTabs
    PERIODS = CatalogPeriods
    CATALOG_TABS = CatalogTabs

    # find methods
    def find_https_error(self, timeout=None):
        return self.find_with_text(DIV, WARNING_PROTOCOL_REQUIRED, timeout)

    def find_necessary_field_error(self, tab, timeout=None):
        element = SPAN if tab == self.TABS.MANUAL else DIV
        return self.find_with_text(element, REQUIRED_FIELD, timeout)

    def find_necessary_field_error_while_creation(self, timeout=None):
        return self.find_with_text(DIV, REQUIRED_FIELD, timeout)

    def find_incorrect_marketplace_url_error(self, timeout=None):
        return self.find_with_text(
            DIV,
            INVALID_MARKETPLACE_URL,
            timeout,
        )

    def find_new_catalog_title(self, timeout=None):
        return self.find_with_text(H2, NEW_CATALOG_TITLE, timeout)

    def find_not_enough_products_banner(self, timeout=None) -> WebElement:
        return self.find(
            self.locators.CATALOG_ERROR_WITH_MINIMUM_THREE_PRODUCTS, timeout
        )

    def find_clear_utm_checkbox(self, timeout=None) -> WebElement:
        return self.find(self.locators.CATALOG_CLEAR_UTM_CHECKBOX_OFF, timeout)

    def find_api_key_input(self, placeholder, timeout=None) -> WebElement:
        return self.find_with_text(INPUT, placeholder, timeout)

    def find_element_with_text(self, element, text, timeout=None):
        return self.find_with_text(element, text, timeout)

    def find_invalid_apikey_error(self, timeout=None):
        return self.find_with_text(DIV, INVALID_API_KEY_ERROR, timeout)

    def find_invalid_apikey_string_encoding_error(self, timeout=None):
        return self.find_with_text(
            DIV, INVALID_API_KEY_ENCODING_ERROR, timeout
        )

    def find_category_on_download(self, category, timeout=None):
        return self.find(
            self.locators.CATALOG_CATEGORY_ON_DOWNLOAD(category), timeout
        )

    def find_file_downloading_error(self, timeout=None):
        return self.find(
            self.locators.FILE_DOWNLOADING_ERROR_NOTIFICATION, timeout
        )

    def find_downloaded_file(self, timeout=None):
        return self.find(self.locators.DOWNLOADED_FILE, timeout)

    def find_catalog_tabs(self, timeout=None):
        return self.find(self.locators.CATALOG_TABS, timeout)

    def find_catalog_title(self, title, timeout=None) -> WebElement:
        title = self.to_page_catalog_title(title)
        self.click(self.locators.CHOOOSE_CATALOG, timeout)
        return self.find(self.locators.CATALOG_TITLE(title), timeout)

    def find_promote_title(self, timeout=None) -> WebElement:
        return self.find(self.locators.COMPANY_SETTING, timeout)

    def find_product_widget_by_title(self, title, timeout=None) -> WebElement:
        return self.find_h2_with_text(title, timeout)

    def find_table_settings_title(self, timeout=None) -> WebElement:
        return self.find_with_text(
            SPAN, CENTER_OF_COMMERCE_TABLE_SETTINGS, timeout
        )

    def find_h2_with_text(self, text, timeout=None) -> WebElement:
        return self.find(self.locators.H2_WITH_TEXT(text), timeout)

    def find_product_by_title(self, text, timeout=None) -> WebElement:
        return self.find_with_text_and_class(SPAN, text, TITLE_CLASS, timeout)

    def find_product_by_id(self, product_id, timeout=None) -> WebElement:
        return self.find(self.locators.PRODUCT_ID_SVG(product_id), timeout)

    def find_catalog_by_title(self, title, timeout=None):
        return self.find_element_with_text("span", title, timeout)

    def redirect_to_products_and_find_checkbox_select_products(
        self, timeout, short_timeout=None
    ) -> WebElement | None:
        self.try_close_study_banner(short_timeout)
        self.switch_catalog_tab(CatalogTabs.PRODUCTS, timeout)

        return self.find_element_with_refresh(
            self.locators.PRODUCTS_SELECT_ALL_CHECKBOX_SVG,
            timeout,
            short_timeout,
        )

    def find_element_with_refresh(
        self, locator, timeout, short_timeout=None
    ) -> WebElement | None:
        element = None
        while timeout > 0:
            try:
                element = self.find(locator, short_timeout)
                break
            except TimeoutException:
                self.driver.refresh()
                timeout -= short_timeout if short_timeout is not None else 5

        return element

    def _period_selector(self, catalog):
        match catalog:
            case self.PERIODS.EVERYDAY:
                return "Ежедневно"
            case self.PERIODS.ONE_HOUR:
                return "1 час"
            case self.PERIODS.FOUR_HOURS:
                return "4 часа"
            case self.PERIODS.EIGHT_HOURS:
                return "8 часов"
            case _:
                raise NoSuchPeriodException()

    def find_by_period(self, period, timeout=None):
        return self.find_with_text(
            "span", self._period_selector(period), timeout
        )

    # fill methods

    def fill_title_input(self, title, timeout=None):
        self.fill(self.locators.CATALOG_TITLE_INPUT, title, timeout)

    def fill_url_input(self, url, timeout=None):
        self.fill(self.locators.CATALOG_URL_UNPUT, url, timeout)

    def fill_client_id_input(
        self, client_id, timeout=None
    ) -> WebElement | None:
        if client_id:
            return self.fill_input_with_placeholder(
                CENTER_OF_COMMERCE_CLIENT_ID_INPUT_TXT, client_id, timeout
            )

    def fill_api_key_input(
        self, placeholder, apikey, timeout=None
    ) -> WebElement:
        return self.fill_input_with_placeholder(placeholder, apikey, timeout)

    def fill_file_input(self, file_path, timeout=None):
        return self.fill(self.locators.MANUAL_FILE_INPUT, file_path, timeout)

    # clear methods

    def clear_url_input(self, timeout=None):
        self.clear(self.locators.CATALOG_URL_UNPUT, timeout)

    def clear_catalog_title(self, timeout=None):
        self.create_catalog_finish()
        self.clear_with_validation(
            self.locators.CATALOG_TITLE_INPUT, timeout=timeout
        )

    def clear_title_input(self, timeout=None):
        self.clear(self.locators.CATALOG_TITLE_INPUT, timeout)

    # click methods

    def click_on_tab(self, type: str, timeout=None):
        match type:
            case self.TABS.FEED:
                self.click(self.locators.FEED_TAB, timeout)
            case self.TABS.MARKETPLACE:
                self.click(self.locators.MARKET_TAB, timeout)
            case self.TABS.MANUAL:
                self.click(self.locators.MANUAL_TAB, timeout)

    def click_on_clear_utm_checkbox(self, timeout=None):
        if self.is_checkbox_checked(
            self.locators.CATALOG_CLEAR_UTM_CHECKBOX, timeout
        ):
            self.click(self.locators.CATALOG_CLEAR_UTM_CHECKBOX_ON, timeout)
        else:
            self.click(self.locators.CATALOG_CLEAR_UTM_CHECKBOX_OFF, timeout)

    def click_on_category_to_download(self, category, timeout=None):
        return self.click(
            self.locators.CATALOG_CATEGORY_ON_DOWNLOAD(category), timeout
        )

    def click_on_element_with_text(self, element, text, timeout=None):
        self.click_element_with_text(element, text, timeout)

    def click_on_promote_button(self, timeout=None):
        self.click(self.locators.PROMOTE_BUTTON, timeout)

    def click_product_table_settings(self, timeout=None):
        self.click(self.locators.PRODUCTS_TABLE_SETTINGS_BUTTON, timeout)

    def click_on_product_by_title(self, title, timeout=None) -> WebElement:
        return self.click_element_with_text_and_class(
            SPAN, title, TITLE_CLASS, timeout
        )

    def click_on_sort_products(self, timeout=None) -> WebElement:
        self.hover_on_element(self.locators.PRODUCT_TABLE_HEADER, timeout)
        return self.click(self.locators.SORT_INDICATOR_PRODUCT, timeout)

    def click_on_warning_button(self, timeout=None):
        self.click(self.locators.WARNING_SVG, timeout)

    # custom methods

    def try_close_study_banner(self, timeout=None):
        try:
            elem = self.multiple_find(
                self.locators.CLOSE_STUDY_BUTTON, timeout
            )[0]
            self.action_click(elem)
        except TimeoutException:
            pass

    def start_creating_catalog(self, timeout=None):
        self.click(self.locators.START_CREATING_CATALOG, timeout=timeout)

    def go_to_create_feed_catalog(self, timeout=None):
        self.close_banner()
        self.start_creating_catalog(timeout)
        self.click_on_tab(self.TABS.FEED, timeout)

    def go_to_create_marketplace_catalog(self, timeout=None):
        self.close_banner()
        self.start_creating_catalog(timeout)
        self.click_on_tab(self.TABS.MARKETPLACE, timeout)

    def go_to_create_manual_catalog(self, timeout=None):
        self.close_banner()
        self.start_creating_catalog(timeout)
        self.click_on_tab(self.TABS.MANUAL, timeout)

    def go_to_create_catalog(
        self, tab, second_field, title="", timeout=None, **kwargs
    ):
        match tab:
            case self.TABS.FEED:
                self.go_to_create_feed_catalog(timeout)
                self.fill_url_input(second_field, timeout)
                self.fill_title_input(title, timeout)
            case self.TABS.MARKETPLACE:
                self.go_to_create_marketplace_catalog(timeout)
                self.fill_url_input(second_field, timeout)
                self.fill_title_input(title, timeout)
            case self.TABS.MANUAL:
                self.go_to_create_manual_catalog(timeout)
                self.fill_file_input(second_field, timeout)
                self.fill_title_input(title, timeout)

    @staticmethod
    def to_page_catalog_title(title):
        return f"{CATALOG_TITLE_PREFIX}{title}"

    def go_to_catalog(self, title, timeout=None):
        title = self.to_page_catalog_title(title)
        self.close_banner()
        self.search_catalog(title, timeout)
        self.click_on_element_with_text(SPAN, title, timeout)

    def go_to_catalog_product(self, product_id, product_title, timeout=None):
        self.search_catalog(product_id, timeout)
        self.click_on_product_by_title(product_title, timeout)

    def search_catalog(self, query, timeout=None):
        self.search(self.locators.SEARCH_CATALOG_FIELD, query, timeout)

    def search_product(self, product_id: int, timeout=None):
        self.search(
            self.locators.SEARCH_CATALOG_BY_CLASS(SEARCH_PRODUCT_CLASS),
            str(product_id),
            timeout,
        )

    def set_refresh_period(self, period: str, timeout=None):
        self.click(self.locators.CATALOG_SELECT_TITLE, timeout)
        match period:
            case self.PERIODS.EVERYDAY:
                self.click(self.locators.CATALOG_PERIOD_EVERYDAY, timeout)
            case self.PERIODS.ONE_HOUR:
                self.click(self.locators.CATALOG_PERIOD_EVERYHOUR, timeout)
            case self.PERIODS.FOUR_HOURS:
                self.click(self.locators.CATALOG_PERIOD_EVERY4HOURS, timeout)
            case self.PERIODS.EIGHT_HOURS:
                self.click(self.locators.CATALOG_PERIOD_EVERY8HOURS, timeout)

    def set_category(self, category: str, timeout=None):
        self.click(self.locators.CATALOG_SELECT_TITLE)
        if category != "Товары":
            self.click(self.locators.CATALOG_CATEGORY(category), timeout)

    def create_catalog_finish(self, timeout=None):
        self.slow_click(self.locators.CATALOG_CREATE_BUTTON, 2, timeout)

    def check_clear_utm_checkbox_is_checked(self, timeout=None) -> bool:
        return self.is_checkbox_checked(
            self.locators.CATALOG_CLEAR_UTM_CHECKBOX, timeout
        )

    def hover_on_utm_label(self, timeout=None) -> WebElement:
        return self.hover_on_element(
            self.locators.CATALOG_CHECKBOX_UTM_LABEL, timeout
        )

    def hover_on_catalog_cell(self, title, timeout=None) -> WebElement:
        return self.find(self.locators.CATALOG_CELL(title), timeout)

    def switch_catalog(self, title, timeout=None) -> WebElement:
        title = self.to_page_catalog_title(title)

        self.click(self.locators.CHOOOSE_CATALOG, timeout)
        self.search(
            self.locators.SEARCH_CATALOG_BY_CLASS(SEARCH_CATALOG_CLASS),
            title,
            timeout,
        )
        return self.click_element_with_text_and_class(
            SPAN, title, CONTENT_CLASS, timeout
        )

    def switch_catalog_tab(self, tab, timeout=None) -> WebElement:
        elem = self.find(
            self.locators.TAB_BY_ID(self.CATALOG_TABS[tab]), timeout
        )
        if elem.get_attribute("aria-selected") == "true":
            return elem

        return self.click(elem, timeout)

    def check_catalog_tab_switched(self, tab, timeout=None) -> bool:
        match tab:
            case self.CATALOG_TABS.PRODUCTS:
                return (
                    self.find(self.locators.PROMOTE_BUTTON, timeout)
                    is not None
                )
            case self.CATALOG_TABS.GROUPS:
                return (
                    self.find(self.locators.CREATE_GROUP_BUTTON, timeout)
                    is not None
                )
            case self.CATALOG_TABS.DIAGNOSTIC:
                try:
                    self.find(
                        self.locators.FEED_DOWNLOADING_ON_DIAGNOSTIC, timeout
                    )
                    return True
                except TimeoutException:
                    try:
                        self.find(self.locators.DOWNLOAD_FULL_REPORT_BUTTON)
                        return True
                    except TimeoutException:
                        return False
            case self.CATALOG_TABS.EVENTS:
                try:
                    self.find(self.locators.CONNECT_DATA_SOURCE_BUTTON)
                    return True
                except TimeoutException:
                    try:
                        self.find(
                            self.locators.TAB_WITH_EVENTS_NOT_ACCESSED_SOON_SVG
                        )
                        return True
                    except TimeoutException:
                        return False
            case self.CATALOG_TABS.DOWNLOADS_HISTORY:
                try:
                    self.find(self.locators.FEED_DOWNLOADING)
                    return True
                except TimeoutException:
                    try:
                        self.find(self.locators.DOWNLOADING_HISTORY_ICON)
                        return True
                    except TimeoutException:
                        return False

        return False

    def check_vk_product_found(self, product_title, timeout=None) -> bool:
        link = self.find_link_with_href(
            CENTER_OF_COMMERCE_VK_PRODUCT_HREF, timeout
        )
        attribute = link.get_attribute(HREF)
        assert attribute

        self.driver.get(attribute)
        try:
            alert = self.driver.switch_to.alert
            alert.accept()
        except NoAlertPresentException:
            pass

        found_title = (
            self.find(self.locators.H1_WITH_TEXT(product_title)) is not None
        )
        self.open()

        return found_title

    def check_utm_hover(self, timeout):
        utm_label_class = self.hover_on_utm_label(timeout).get_attribute(
            "class"
        )

        assert utm_label_class

        return HOVER in utm_label_class

    def remove_catalog_by_title(self, title, timeout=None):
        title = self.to_page_catalog_title(title)
        try:
            alert = self.driver.switch_to.alert
            alert.accept()
        except NoAlertPresentException:
            pass
        self.search_catalog(title, timeout)
        element = self.hover_on_catalog_cell(title, timeout)
        self.js_click(element)

        self.click_element_with_text(SPAN, "Удалить каталог", timeout)

        return self.click_element_with_text(SPAN, "Удалить", timeout)
