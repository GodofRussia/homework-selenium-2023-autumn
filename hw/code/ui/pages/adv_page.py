import os
import re

from selenium.webdriver.support.wait import WebDriverWait
from ui.locators.adv import AdvLocators
from ui.pages.base_page import BasePage
from ui.pages.group_adv_page import GroupAdvPage

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from ui.pages.consts import WaitTime

class AdvPage(BasePage):
    url = "https://ads.vk.com/hq/new_create/ad_plan"
    locators = AdvLocators

    def get_page(self):
        page = GroupAdvPage.__new__(GroupAdvPage)
        page.driver = self.driver
        page.get_to_next()

        return self

    def click_continue_button(self):
        buttons = self.multiple_find(self.locators.FOOTER_BUTTONS)
        el = buttons[-1]
        self.action_click(el)
        return self

    def send_text_to_title(self, text: str):
        el = self.multiple_find(self.locators.INPUT_TITLE)[0]
        el.clear()
        el.send_keys(text, Keys.RETURN)

        return self

    def get_title_max(self) -> int:
        el = self.multiple_find(self.locators.COUNTS_CHARS)[0]
        text = el.text

        matches = re.search(r"\d+ / (\d+)", text)
        count_chars_value = 0
        if matches:
            count_chars_value = int(matches.group(1))

        return count_chars_value

    def send_url(self, url: str):
        el = self.find(self.locators.URL_INPUT)
        el.clear()
        el.send_keys(url, Keys.RETURN)

        return self

    def select_logo(self, number_of_logo: int):
        self.action_click(self.find(self.locators.LOGO_INPUT))
        el = self.multiple_find(self.locators.LOG_VARIANTS)[number_of_logo]

        self.action_click(el)
        return self

    def write_to_inputs(self, text: str):
        inputs = self.multiple_find(self.locators.TEXT_INPUTS)

        for i in inputs:
            i.clear()
            i.send_keys(text, Keys.RETURN)

        return self

    def write_to_textarea(self, text: str):
        areas = self.multiple_find(self.locators.AREA_INPUTS)
        for i in areas:
            i.clear()
            i.send_keys(text, Keys.RETURN)

        return self

    def get_company_name(self):
        return self.find(self.locators.COMPANY_NAME).text

    def click_send_button(self, timeout=WaitTime.MEDIUM_WAIT):
        self.action_click(self.find(self.locators.SEND_BUTTON, timeout))
        return self

    # Return name of company, that was created
    def create_company(self) -> str:
        self.get_page()
        self.select_logo(0).write_to_inputs(
            "https://vk.com/"
        ).write_to_textarea("https://vk.com/")
        name = self.get_company_name()

        self.click_media_upload().select_media_options().add_media_option()
        self.click_continue_button().click_send_button()

        return name

    def click_media_upload(self):
        self.action_click(self.find(self.locators.CHOOSE_MEDIA))
        return self

    def select_media_options(self, options=0):
        elements = self.multiple_find(self.locators.MEDIA_OPTIONS)
        WebDriverWait(self.driver, WaitTime.SHORT_WAIT).until(
            EC.visibility_of_element_located(self.locators.MEDIA_OPTIONS)
        )
        self.driver.execute_script(
            "arguments[0].scrollIntoView(true);", elements[options]
        )
        self.action_click(elements[options])
        return self

    def add_media_option(self):
        el = self.find(self.locators.ADD_MEDIA)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", el)
        el = WebDriverWait(self.driver, WaitTime.MEDIUM_WAIT).until(
            EC.visibility_of_element_located(self.locators.ADD_MEDIA)
        )

        self.action_click(el)
        return self

    def upload_logo(self):
        self.action_click(self.find(self.locators.LOGO_INPUT, WaitTime.LONG_WAIT))
        file_input = self.find(self.locators.LOGO_INPUT_FILE)

        current_directory = os.getcwd()
        download_directory = os.path.join(current_directory, "test.jpg")

        file_input.clear()
        file_input.send_keys(download_directory)

        el = self.find(self.locators.LOADING_IMG)
        WebDriverWait(self.driver, WaitTime.LONG_WAIT).until(EC.staleness_of(el))

        self.action_click(self.find(self.locators.CLOSE_MODAL))
        return self
