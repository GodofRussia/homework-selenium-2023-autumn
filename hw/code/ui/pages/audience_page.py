import re

from selenium.webdriver.support.wait import WebDriverWait
from ui.pages.base_page import BasePage

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from ui.locators.audience import AudienceLocators
from selenium.common.exceptions import TimeoutException

from ui.pages.consts import BASE_POSITIONS, POSITIONS_AUDIENCE, URLS, WaitTime


class AudiencePage(BasePage):
    url = URLS.audience_url
    locators = AudienceLocators

    def click_create_button(self):
        self.search_action_click(self.locators.CREATE_BUTTON)
        return self

    def write_text_to_name(self, text):
        field = WebDriverWait(self.driver, WaitTime.MEDIUM_WAIT).until(
            EC.element_to_be_clickable(self.locators.CREATION_NAME_AUDITORY)
        )
        field.clear()
        field.send_keys(text, Keys.RETURN)
        return self

    def click_add_source(self):
        self.search_action_click(self.locators.ADD_SOURCE)
        return self

    def select_lead_region(self):
        self.search_action_click(self.locators.LEAD_REGION)
        return self

    def click_lead_input(self):
        self.search_action_click(self.locators.LEAD_INPUT)
        return self

    def select_lead_option(self, what_option=BASE_POSITIONS.first_search_pos):
        self.search_action_click(self.locators.LEAD_OPTIONS, what_option)
        return self

    def click_checkbox_lead(self,
                            what_checkbox=BASE_POSITIONS.first_search_pos):
        self.search_action_click(self.locators.LEAD_CHECKBOXES, what_checkbox)
        return self

    def remove_symbols_from_el(self, el, len: int):
        for i in range(len):
            el.send_keys(Keys.BACKSPACE)
        return self

    def write_to_from_field(self, form_days: int):
        input = self.multiple_find(self.locators.LEAD_INPUT_DAYS)
        from_input = input[POSITIONS_AUDIENCE.from_input_days]
        self.remove_symbols_from_el(
            from_input, len(str(self.get_from_value()))
        )

        from_input.send_keys(form_days, Keys.RETURN)
        return self

    def write_to_to_field(self, form_days: int):
        input = self.multiple_find(self.locators.LEAD_INPUT_DAYS)
        from_input = input[POSITIONS_AUDIENCE.to_input_days]
        self.remove_symbols_from_el(from_input, len(str(self.get_to_value())))

        from_input.send_keys(form_days, Keys.RETURN)
        return self

    def get_from_value(self) -> int:
        input = self.multiple_find(self.locators.LEAD_INPUT_DAYS)
        return int(
            input[POSITIONS_AUDIENCE.from_input_days].get_attribute("value"))

    def get_to_value(self) -> int:
        input = self.multiple_find(self.locators.LEAD_INPUT_DAYS)
        return int(
            input[POSITIONS_AUDIENCE.to_input_days].get_attribute("value"))

    def select_key_phrases_region(self):
        self.search_action_click(self.locators.KEY_PHRASES_REGION)
        return self

    def write_to_period(self, period: int):
        period_field = self.find(self.locators.KEY_DAYS_PERIOD)

        self.remove_symbols_from_el(
            period_field, len(str(self.get_period_value()))
        )

        period_field.send_keys(period, Keys.RETURN)

        return self

    def get_period_value(self) -> int:
        period_field = self.find(self.locators.KEY_DAYS_PERIOD)
        return int(period_field.get_attribute("value"))

    def click_save_button(self):
        self.search_action_click(self.locators.SAVE_BUTTON)
        return self

    def click_save_button_modal(self):
        self.search_action_click(
            self.locators.SAVE_BUTTON, POSITIONS_AUDIENCE.save_button_modal)
        return self

    def click_user_list(self):
        self.search_action_click(
            self.locators.USER_LIST, POSITIONS_AUDIENCE.user_list)
        return

    def is_user_list_url(self) -> bool:
        return (
            URLS.user_url
            == self.driver.current_url
        )

    def select_vk_group_region(self):
        self.search_action_click(self.locators.VK_GROUP_REGION)
        return self

    def write_to_vk_group(self, text: str):
        input = self.find(self.locators.VK_GROUP_INPUT)
        input.clear()
        input.send_keys(text, Keys.RETURN)
        return self

    def select_vk_group(self):
        self.search_action_click(self.locators.VK_GROUPS)
        self.search_action_click(self.locators.VK_GROUPS_OPTIONS)

        self.empty_click()
        return self

    def empty_click(self):
        self.search_action_click(self.locators.VK_GROUP_TEXT)
        return self

    def get_name_audience(self) -> str:
        return self.find(self.locators.CREATION_NAME_AUDITORY).get_attribute(
            "value"
        )

    def select_vk_group_filter(self):
        self.filter_click()

        self.search_action_click(self.locators.SUBSCRIBER_VK_GROUP)
        self.search_action_click(self.locators.APPLY_BUTTON)

        return self

    def delte_source(self, what_source=BASE_POSITIONS.first_search_pos):
        self.search_action_click(
            self.locators.SOURCE_BUTTONS, what_source * 2 + 1
        )

        self.search_action_click_not_clickable(
            self.locators.DELETE_BUTTON, POSITIONS_AUDIENCE.delete_source_btn
        )

        return self

    def wait_for_dropdown_filter(self, filter_btn) -> bool:
        try:
            self.action_click(filter_btn)
            WebDriverWait(self.driver, WaitTime.SUPER_SHORT_WAIT).until(
                EC.presence_of_element_located(
                    self.locators.FILTER_DROPDOWN_EXIST
                )
            )
            return True
        except TimeoutException:
            pass

        return False

    def filter_click(self):
        filter_btn = self.multiple_find(self.locators.FILTER_BUTTON)[
            POSITIONS_AUDIENCE.filter_btn]
        WebDriverWait(self.driver, WaitTime.LONG_WAIT).until(
            lambda _: self.wait_for_dropdown_filter(filter_btn)
        )

        return self

    def is_value_equal(self, locator, what_element, value):
        try:
            el = self.multiple_find(locator)[what_element]
            return el.get_attribute("value") == str(value)
        except TimeoutException:
            pass

        return False

    def wait_until_value_equal(self, locator, what_element, old_value):
        WebDriverWait(self.driver, WaitTime.LONG_WAIT).until(
            lambda _: self.is_value_equal(locator, what_element, old_value)
        )

        return self

    def wait_to_filed_equal(self, value):
        self.wait_until_value_equal(
            self.locators.LEAD_INPUT_DAYS,
            POSITIONS_AUDIENCE.from_input_days,
            value)
        return self

    def wait_from_filed_equal(self, value):
        self.wait_until_value_equal(
            self.locators.LEAD_INPUT_DAYS,
            POSITIONS_AUDIENCE.to_input_days,
            value)
        return self

    def wait_period_filed_equal(self, value):
        self.wait_until_value_equal(
            self.locators.KEY_DAYS_PERIOD,
            POSITIONS_AUDIENCE.period_pos,
            value)
        return self
