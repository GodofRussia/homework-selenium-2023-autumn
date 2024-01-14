import time
from ui.pages.consts import (
    BASE_POSITIONS,
    INPUT_TEXT,
    LABELS,
    PLACE,
    POSITIONS_GROUP,
    URLS,
    WaitTime
)

from ui.pages.consts import GROUP_ADV_INVALID_UTM
from ui.pages.base_page import BasePage
from ui.locators.group_adv import GroupAdvLocators

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from ui.pages.new_company_page import NewCompanyPage
from selenium.common.exceptions import TimeoutException


class GroupAdvPage(BasePage):
    url = URLS.ad_plan_url
    locators = GroupAdvLocators

    def site_region_click(self):
        self.click(self.locators.SEARCH_INPUT, WaitTime.MEDIUM_WAIT)
        el = self.find(self.locators.SEARCH_INPUT)
        self.send_keys_with_enter(el, PLACE)

        self.click(self.locators.REGION_VARIANTS)
        return self

    def remove_selected_region(self):
        self.click(self.locators.SELECTED_RUSSIA)
        return self

    def get_selected_region(self):
        try:
            return self.find(self.locators.SELECTED_RUSSIA)
        except TimeoutException:
            return None

    def get_page(self):
        page = NewCompanyPage.__new__(NewCompanyPage)
        page.driver = self.driver
        page.get_to_next()

        return self

    def select_demograpy(self):
        self.search_action_click_not_clickable(self.locators.DEMOGRAPHY_REGION)
        return self

    def select_bottom_age(self, age: int):
        el = self.multiple_find(self.locators.AGE_FIELD)[
            POSITIONS_GROUP.bottom_age]

        self.action_click_not_clickable(el)
        el.send_keys(age, Keys.RETURN)

        return self

    def select_upper_age(self, age: int):
        el = self.multiple_find(locator=self.locators.AGE_FIELD)[
            POSITIONS_GROUP.upper_age]
        self.action_click_not_clickable(el)
        el.send_keys(age, Keys.RETURN)

        return self

    def get_upper_age(self):
        el = self.multiple_find(self.locators.AGE_FIELD)[
            POSITIONS_GROUP.upper_age]
        return el.get_attribute("value")

    def get_lower_age(self):
        el = self.multiple_find(self.locators.AGE_FIELD)[
            POSITIONS_GROUP.bottom_age]
        return el.get_attribute("value")

    def click_continue_button(self):
        self.search_action_click_not_clickable(
            self.locators.FOOTER_BUTTONS,
            POSITIONS_GROUP.continue_btn
        )

        return self

    def wait_load_page(self):
        self.search_action_click_not_clickable(
            self.locators.SAVE_TEXT, POSITIONS_GROUP.save_btn, WaitTime.SUPER_LONG_WAIT)
        return self

    def click_interest_region(self, timeout=WaitTime.MEDIUM_WAIT):
        self.search_action_click_not_clickable(
            self.locators.INTEREST_REGION,
            POSITIONS_GROUP.interest_region,
            timeout)
        return self

    def click_key_phrases(self, timeout=WaitTime.MEDIUM_WAIT):
        self.search_action_click_not_clickable(
            locator=self.locators.KEY_PHRASES, timeout=timeout)

        return self

    def send_key_phrases(self, text: str, timeout=WaitTime.LONG_WAIT):
        el = self.wait(timeout).until(
            EC.element_to_be_clickable(self.locators.KEY_PHRASE_INPUTS)
        )

        self.send_keys_with_enter(el, text)

        return self

    def send_keys_phrases_minus(self, text):
        el = self.multiple_find(
            self.locators.KEY_PHRASE_INPUTS, WaitTime.LONG_WAIT
        )[POSITIONS_GROUP.key_phrase_minus_input]

        self.send_keys_with_enter(el, text)

        return self

    def click_device_region(self):
        self.search_action_click_not_clickable(self.locators.DEVICES)
        return self

    def remove_device(self, what_device: int):
        self.search_action_click_not_clickable(
            self.locators.DEVICES_OPTIONS, what_device)
        return self

    def is_disabled_and_checked_device(self, what_device: int):
        el = self.multiple_find(self.locators.DEVICES_OPTIONS)[what_device]

        disalbed_att = el.get_attribute("disabled")
        checked_att = el.get_attribute("checked")

        return disalbed_att and checked_att

    def click_url_region(self):
        self.search_action_click_not_clickable(
            self.locators.URL_PARAMETER_REGION)
        return self

    def select_utm(self):
        self.search_action_click(
            self.locators.URL_OPTIONS, POSITIONS_GROUP.utm)
        return self

    def send_text_url(self, text: str):
        el = self.find(self.locators.URL_INPUT)

        self.send_keys_with_enter(el, text)
        return self

    def is_checkbox_checked(self):
        try:
            el = self.multiple_find(
                self.locators.URL_CHECBOXES,
                WaitTime.SHORT_WAIT)[POSITIONS_GROUP.checkbox]

            return el.get_attribute("checked")
        except TimeoutException:
            pass

        return False

    def wait_for_checkbox_load(self):
        self.wait(WaitTime.SHORT_WAIT).until(
            lambda _: self.is_checkbox_checked())

        return self

    def _is_utm_renders(self):
        try:
            el = self.wait(WaitTime.SUPER_SHORT_WAIT).until(
                EC.visibility_of_all_elements_located(
                    self.locators.URL_OPTIONS)
            )

            return (
                len(el) == INPUT_TEXT.URL_OPTIONS_LEN and el[1].is_displayed()
            )
        except TimeoutException:
            pass

        return False

    def wait_for_utm_render(self):
        self.wait(WaitTime.SHORT_WAIT).until(
            lambda _: self._is_utm_renders())

        return self

    def is_utm_not_correct(self):
        return GROUP_ADV_INVALID_UTM in self.driver.page_source

    def get_to_next(self):
        self.get_page().site_region_click().click_until_next_page()
        return self

    def wait_for_adv_page(self, filter_btn) -> bool:
        try:
            self.action_click(filter_btn)
            self.wait(WaitTime.SUPER_SHORT_WAIT).until(
                lambda _: self.is_on_site_text(LABELS.preview))

            return True
        except TimeoutException:
            pass

        return False

    def _is_region_visible(self):
        try:
            el = self.multiple_find(self.locators.KEY_PHRASES_REGION)[
                POSITIONS_GROUP.key_phrase_minus_input]

            return el.get_attribute("aria-hidden").lower() == "false"
        except TimeoutException:
            pass

        return False

    def wait_key_phrase_render(self):
        self.wait(WaitTime.MEDIUM_WAIT).until(
            lambda _: self._is_region_visible())

        return self

    def click_until_next_page(self):
        btn_to_click = self.multiple_find(self.locators.CONTINUE_BUTTON)[
            BASE_POSITIONS.last_search_pos]

        self.wait(WaitTime.SUPER_LONG_WAIT).until(
            lambda _: self.wait_for_adv_page(btn_to_click))

        return self
