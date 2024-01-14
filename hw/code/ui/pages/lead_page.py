import time
from ui.pages.consts import INPUT_TEXT, POSITIONS_SITE, URLS, WaitTime
from ui.pages.base_page import BasePage
from ui.locators.lead import LeadPageLocators
from urllib.parse import urlparse

from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class LeadPage(BasePage):
    url = URLS.lead_url
    locators = LeadPageLocators

    def create_lead(self, lead_info=INPUT_TEXT.lead_info):
        self.search_action_click(self.locators.CREATE_BUTTON)

        self.select_logo()

        self.write_to_inputs(lead_info, 1)

        self.click_continue_new_form()
        self.click_continue_question_form()
        self.click_continue_result_form()

        self.write_to_inputs(lead_info, 0, 2)

        self.search_action_click(locator=self.locators.SAVE_BUTTON)
        self.wait_for_modal_dissappear()

        return self

    def select_logo(self):
        self.search_action_click(self.locators.UPLOAD_LOGO)
        self.search_action_click(self.locators.MEDIA_OPTIONS, 0)
        return self

    def write_to_inputs(self, text: str, from_pos=0, to_pos=-1):
        inputs = self.multiple_find(self.locators.INPUTS)
        if to_pos == -1:
            to_pos = len(inputs) - 1

        for i in range(from_pos, to_pos):
            el = inputs[i]
            el.clear()
            el.send_keys(text)

        return self

    def is_question_form(self):
        try:
            self.search_action_click(self.locators.CONTINUE_BUTTON)
            self.multiple_find(self.locators.CONTACT_INFO, WaitTime.SHORT_WAIT)

            return True
        except TimeoutException:
            pass

        return False

    def is_results_form(self):
        try:
            self.search_action_click(self.locators.CONTINUE_BUTTON)
            self.multiple_find(self.locators.ADD_SITE, WaitTime.SHORT_WAIT)

            return True
        except TimeoutException:
            pass

        return False

    def is_settings_form(self):
        try:
            self.search_action_click(self.locators.CONTINUE_BUTTON)
            self.multiple_find(self.locators.SAVE_BUTTON, WaitTime.SHORT_WAIT)

            return True
        except TimeoutException:
            pass

        return False

    def click_continue_new_form(self):
        self.wait(WaitTime.LONG_WAIT).until(lambda _: self.is_question_form())
        return self

    def click_continue_question_form(self):
        self.wait(WaitTime.LONG_WAIT).until(lambda _: self.is_results_form())
        return self

    def click_continue_result_form(self):
        self.wait(WaitTime.LONG_WAIT).until(lambda _: self.is_settings_form())
        return self

    def wait_for_modal_dissappear(self):
        self.wait(WaitTime.MEDIUM_WAIT).until_not(
            EC.presence_of_element_located(self.locators.MODAL))
        return self

    def _wait_until_func_true(self, func, timeout=WaitTime.LONG_WAIT):
        self.wait(timeout).until(func)
        return self

    def delete_leads(self):
        try:
            el = self.find(self.locators.ALL_LEAD_CHECKBOX)
            self.js_click(el)

            self.search_action_click(self.locators.SELECTORS, 1)
            self.search_action_click(self.locators.DELETE_LABELS)

            delete_button = self.multiple_find(self.locators.MODAL_BUTTONS)[  # type: ignore
                POSITIONS_SITE.delete_modal_btn]
            self.action_click(delete_button)

            self.wait(WaitTime.MEDIUM_WAIT).until(
                EC.staleness_of(delete_button))
        except TimeoutException:
            pass

        return self
