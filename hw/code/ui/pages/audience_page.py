import time
import re

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from ui.locators.adv import AdvLocators
from ui.pages.base_page import BasePage
from ui.pages.group_adv_page import GroupAdvPage

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from ui.locators.audience import AudienceLocators


class AudiencePage(BasePage):
    url = "https://ads.vk.com/hq/audience"
    locators = AudienceLocators

    def click_create_button(self):
        btn = self.find(self.locators.CREATE_BUTTON)
        self.action_click(btn)

        return self

    def is_on_site_text(self, text: str, timeout: int = 5):
        returnVal = False
        try:
            returnVal = self.wait(timeout).until(
                EC.presence_of_element_located(
                    (By.XPATH, f"//*[contains(text(), '{text}')]")
                )
            )
        except Exception as e:
            returnVal = False

        return returnVal

    def write_text_to_name(self, text):
        field = self.find(self.locators.CREATION_NAME_AUDITORY)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.locators.CREATION_NAME_AUDITORY)
        )
        field.clear()
        field.send_keys(text, Keys.RETURN)
        return self

    def click_add_source(self):
        btn = self.find(self.locators.ADD_SOURCE)
        self.action_click(btn)
        return self

    def select_lead_region(self):
        region = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.locators.LEAD_REGION)
        )
        self.action_click(region)
        return self

    def click_lead_input(self):
        input = self.find(self.locators.LEAD_INPUT)
        self.action_click(input)
        return self

    def select_lead_option(self, what_option=0):
        options = self.multiple_find(self.locators.LEAD_OPTIONS)
        self.action_click(options[what_option])
        return self

    def click_checkbox_lead(self, what_checkbox=0):
        checkboxes = self.multiple_find(self.locators.LEAD_CHECKBOXES)

        self.action_click(checkboxes[what_checkbox])
        return self

    def write_to_from_field(self, form_days: int):
        input = self.multiple_find(self.locators.LEAD_INPUT_DAYS)
        from_input = input[0]

        for i in range(len(str(self.get_from_value()))):
            from_input.send_keys(Keys.BACKSPACE)

        from_input.send_keys(form_days, Keys.RETURN)

        return self

    def write_to_to_field(self, form_days: int):
        input = self.multiple_find(self.locators.LEAD_INPUT_DAYS)
        from_input = input[1]

        for i in range(len(str(self.get_to_value()))):
            from_input.send_keys(Keys.BACKSPACE)

        from_input.send_keys(form_days, Keys.RETURN)

        return self

    def get_from_value(self) -> int:
        input = self.multiple_find(self.locators.LEAD_INPUT_DAYS)
        return int(input[0].get_attribute("value"))

    def get_to_value(self) -> int:
        input = self.multiple_find(self.locators.LEAD_INPUT_DAYS)
        return int(input[1].get_attribute("value"))

    def select_key_phrases_region(self):
        region = self.find(self.locators.KEY_PHRASES_REGION)
        self.action_click(region)
        return self

    def write_to_period(self, period: int):
        period_field = self.find(self.locators.KEY_DAYS_PERIOD)

        for i in range(len(str(self.get_period_value()))):
            period_field.send_keys(Keys.BACKSPACE)

        period_field.send_keys(period, Keys.RETURN)

        return self

    def get_period_value(self) -> int:
        period_field = self.find(self.locators.KEY_DAYS_PERIOD)
        return int(period_field.get_attribute("value"))

    def click_save_button(self):
        self.action_click(self.find(self.locators.SAVE_BUTTON))
        return self

    def click_save_button_modal(self):
        self.action_click(self.multiple_find(self.locators.SAVE_BUTTON)[1])
        return self

    def click_user_list(self):
        self.action_click(self.multiple_find(self.locators.USER_LIST)[1])
        return

    def is_user_list_url(self) -> bool:
        return "https://ads.vk.com/hq/audience/user_lists" == self.driver.current_url

    def select_vk_group_region(self):
        region = self.find(self.locators.VK_GROUP_REGION)
        self.action_click(region)
        return self

    def write_to_vk_group(self, text: str):
        input = self.find(self.locators.VK_GROUP_INPUT)
        input.clear()
        input.send_keys(text, Keys.RETURN)
        return self

    def select_vk_group(self):
        self.action_click(self.find(self.locators.VK_GROUPS))
        self.action_click(self.multiple_find(self.locators.VK_GROUPS_OPTIONS)[0])

        self.empty_click()
        return self

    def empty_click(self):
        self.action_click(self.find(self.locators.VK_GROUP_TEXT))
        return self

    def get_name_audience(self) -> str:
        return self.find(self.locators.CREATION_NAME_AUDITORY).get_attribute("value")

    def select_vk_group_filter(self):
        filter_btn = self.multiple_find(self.locators.FILTER_BUTTON)[1]

        self.action_click(filter_btn)
        self.action_click(filter_btn)

        subscribers_btn = self.find(self.locators.SUBSCRIBER_VK_GROUP)
        self.action_click(subscribers_btn)

        apply_btn = self.find(self.locators.APPLY_BUTTON)
        self.action_click(apply_btn)

        return self

    def delte_source(self, what_source=0):
        sources = self.multiple_find(self.locators.SOURCE_BUTTONS)
        self.action_click(sources[what_source * 2 + 1])

        self.action_click(self.find(self.locators.DELETE_BUTTON))

        return self
