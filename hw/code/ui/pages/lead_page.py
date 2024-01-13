from ui.pages.consts import INPUT_TEXT, URLS, WaitTime
from ui.pages.base_page import BasePage
from ui.locators.lead import LeadPageLocators
from urllib.parse import urlparse

from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class LeadPage(BasePage):
    url = URLS.lead_url
    locators = LeadPageLocators

    def create_lead(self):
        self.search_action_click(self.locators.CREATE_BUTTON)

        self.select_logo()

        self.write_to_inputs(INPUT_TEXT.lead_info, 1)
        self.search_action_click(self.locators.CONTINUE_BUTTON)

        self.wait_for_questions_page()
        self.search_action_click(self.locators.CONTINUE_BUTTON)

        self.wait_for_result_page()
        self.search_action_click(self.locators.CONTINUE_BUTTON)

        self.write_to_inputs(INPUT_TEXT.lead_info, 0, 2)
        self.search_action_click(self.locators.SAVE_BUTTON)

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

    def wait_for_result_page(self):
        self.multiple_find(self.locators.ADD_SITE)
        return self

    def wait_for_questions_page(self):
        self.multiple_find(self.locators.CONTACT_INFO, WaitTime.LONG_WAIT)
        return self

    def wait_for_modal_dissappear(self):
        self.wait(WaitTime.MEDIUM_WAIT).until_not(
            EC.presence_of_element_located(self.locators.MODAL))
        return self
