import re

from ui.pages.consts import (
    BASE_POSITIONS,
    LABELS,
    POSITIONS_SITE,
    URLS,
    WaitTime,
    get_access_url,
    get_events_url,
    get_tags_url,
)

from ui.pages.base_page import BasePage

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from ui.locators.site import SiteLocators
from selenium.common.exceptions import TimeoutException


class SitePage(BasePage):
    url = URLS.site_url
    locators = SiteLocators

    def click_add_button(self):
        self.click(self.locators.ADD_PIXEL_BUTTON, WaitTime.MEDIUM_WAIT)
        return self

    def is_domen_input_exist(self):
        return bool(self.find(self.locators.INPUT_DOMEN))

    def create_pixel(self, site=URLS.test_site):
        self.click_add_button()

        input = self.find(self.locators.INPUT_DOMEN)
        self.send_keys_with_enter(input, site)

        self.search_action_click(self.locators.ADD_BUTTON_MODAL)
        if self.is_on_site_text(LABELS.pixel_found, WaitTime.SUPER_LONG_WAIT):
            self.search_action_click(self.locators.CREATE_NEW_PIXEL_REGION)

        value = self.find(self.locators.PIXEL_ID, WaitTime.LONG_WAIT)
        self.search_action_click(self.locators.CLOSE_BUTTON)

        match = re.search(r'\d+', value.text)
        if match:
            return match.group()
        else:
            return 0

    def wait_for_pixel(self, id: str):
        self.is_on_site_text(id, WaitTime.MEDIUM_WAIT)
        return self

    def select_collection_checkbox(self):
        self.search_action_click(self.locators.CHECBOX_SETTINGS)
        return self

    def input_collection_data(self, text: str, timeout=None):
        input = self.find(self.locators.DATA_INPUT, timeout)
        self.send_keys_with_enter(input, text)

        return self

    def is_error_on_page(self, text):
        try:
            self.is_on_site_text(text)

            return True
        except TimeoutException:
            return False

    def click_events(self):
        self.search_action_click(self.locators.EVENTS_REG)
        return self

    def current_id(self):
        match = re.search(r"/(\d+)/code$", self.driver.current_url)
        if match:
            return match.group(1)
        else:
            return None

    def click_tags(self):
        self.search_action_click(self.locators.AUDIENCE_TAGS_REG)
        return self

    def click_access(self):
        self.search_action_click(self.locators.ACCESSABLE_REG)
        return self

    def click_add_event(self):
        self.search_action_click(self.locators.ADD_EVENT)
        return self

    def click_add_event_modal(self):
        self.search_action_click(self.locators.ADD_EVENT_MODAL)
        return self

    def select_manual(self):
        self.search_action_click(self.locators.SELECT_EVENT_NAME)
        return self

    def input_event_name(self, text: str):
        input = self.find(self.locators.INPUT_EVENT_NAME)

        self.send_keys_with_enter(input, text)

        return self

    def select_event_category(self):
        self.search_action_click(
            self.locators.EVENT_SELECTOR, POSITIONS_SITE.category_event)
        self.search_action_click(self.locators.CATEGORY_BUY_OPTION)

        return self

    def select_event_condition(self):
        self.search_action_click(
            self.locators.EVENT_SELECTOR, POSITIONS_SITE.event_condition)
        self.search_action_click(self.locators.CONDITION_OPTION)

        return self

    def input_text_url(self, text: str):
        input = self.multiple_find(self.locators.URL_INPUT)[
            POSITIONS_SITE.text_url_pos]
        self.send_keys_with_enter(input, text)

        return self

    def click_add_tag(self):
        self.search_action_click(self.locators.ADD_TAG)
        return self

    def input_name_tag(self, text: str):
        input = self.find(self.locators.INPUT_NAME_TAG)
        self.send_keys_with_enter(input, text)

        return self

    def delete_pixel(self, what_delete: int = BASE_POSITIONS.first_search_pos):
        element = self.multiple_find(self.locators.MORE_OPTIONS)[what_delete]
        self.js_click(element)

        self.search_action_click(
            self.locators.DELETE_OPTION,
            POSITIONS_SITE.delete_btn_pop_up,
            WaitTime.SHORT_WAIT)

        delete_button = self.multiple_find(self.locators.MODAL_BUTTONS)[
            POSITIONS_SITE.delete_modal_btn]
        self.action_click(delete_button)

        self.wait(WaitTime.MEDIUM_WAIT).until(
            EC.staleness_of(delete_button))
        return self

    def _wait_for_settings(self, locator, what_element) -> bool:
        try:
            self.search_action_click(locator, what_element)
            self.wait(WaitTime.SHORT_WAIT).until(
                EC.presence_of_element_located(
                    self.locators.SETTINGS_PAGE_ELEMENT)
            )

            return True
        except TimeoutException:
            pass

        return False

    def click_settings_until_change(self, what_element=0):
        self.wait(WaitTime.LONG_WAIT).until(
            lambda _: self._wait_for_settings(
                self.locators.SETTINGS,
                what_element)
        )

        return self

    def delete_all_pixels(self):
        while True:
            try:
                self.delete_pixel()
            except TimeoutException as e:
                break

        return self

    def is_events_page(self, pixel_id):
        return (
            self.driver.current_url
            == get_events_url(pixel_id)
        )

    def is_tags_page(self, pixel_id):
        return (
            self.driver.current_url
            == get_tags_url(pixel_id)
        )

    def is_access_page(self, pixel_id):
        return (
            self.driver.current_url
            == get_access_url(pixel_id)
        )
