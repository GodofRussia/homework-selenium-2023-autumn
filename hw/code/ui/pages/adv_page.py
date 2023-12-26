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


class AdvPage(BasePage):
    url = "https://ads.vk.com/hq/new_create/ad_plan/"
    locators = AdvLocators

    def multiple_find(self, locator):
        return WebDriverWait(self.driver, 15).until(
            EC.presence_of_all_elements_located(locator)
        )

    def action_click(self, element):
        actions = ActionChains(self.driver, 500)
        actions.move_to_element(element)
        actions.click(element)
        actions.perform()
        return self

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

    def is_on_site_text(self, text: str, timeout: int = 10):
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

    def click_send_button(self, timeout=10):
        self.action_click(self.find(self.locators.SEND_BUTTON, timeout))
        return self

    # Return name of company, that was created
    def create_company(self) -> str:
        self.get_page()
        self.select_logo(0).write_to_inputs("https://vk.com/").write_to_textarea(
            "https://vk.com/"
        )
        name = self.get_company_name()

        self.click_media_upload().select_media_options().add_media_option()
        self.click_continue_button().click_send_button(10)

        return name

    def click_media_upload(self):
        self.action_click(self.find(self.locators.CHOOSE_MEDIA))
        return self

    def select_media_options(self, options=0):
        elements = self.multiple_find(self.locators.MEDIA_OPTIONS)
        WebDriverWait(self.driver, 10).until(
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
        el = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.locators.ADD_MEDIA)
        )

        self.action_click(el)
        return self
