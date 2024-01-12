import time
from ui.pages.consts import WaitTime

from selenium.webdriver.support.wait import WebDriverWait
from ui.pages.base_page import BasePage
from ui.locators.group_adv import GroupAdvLocators

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from ui.pages.new_company_page import NewCompanyPage
from selenium.common.exceptions import TimeoutException


class GroupAdvPage(BasePage):
    url = "https://ads.vk.com/hq/new_create/ad_plan"
    locators = GroupAdvLocators

    def site_region_click(self):
        self.click(self.locators.SEARCH_INPUT, WaitTime.MEDIUM_WAIT)
        el = self.find(self.locators.SEARCH_INPUT)
        el.send_keys("Россия", Keys.RETURN)

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
        el = self.multiple_find(self.locators.AGE_FIELD)[0]

        self.action_click_not_clickable(el)
        el.send_keys(age, Keys.RETURN)

        return self

    def select_upper_age(self, age: int):
        el = self.multiple_find(locator=self.locators.AGE_FIELD)[1]
        self.action_click_not_clickable(el)
        el.send_keys(age, Keys.RETURN)

        return self

    def get_upper_age(self):
        el = self.multiple_find(self.locators.AGE_FIELD)[1]
        return el.get_attribute("value")

    def get_lower_age(self):
        el = self.multiple_find(self.locators.AGE_FIELD)[0]
        return el.get_attribute("value")

    def click_continue_button(self):
        self.search_action_click_not_clickable(self.locators.FOOTER_BUTTONS, 1)
        return self

    def wait_load_page(self):
        self.search_action_click_not_clickable(self.locators.SAVE_TEXT, 0)
        return self

    def click_interest_region(self, timeout=WaitTime.MEDIUM_WAIT):
        self.search_action_click_not_clickable(
            self.locators.INTEREST_REGION, 0, timeout)
        return self

    def click_key_phrases(self, timeout=WaitTime.MEDIUM_WAIT):
        self.search_action_click_not_clickable(
            locator=self.locators.KEY_PHRASES, timeout=timeout)

        return self

    def send_key_phrases(self, text: str, timeout=WaitTime.LONG_WAIT):
        el = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(self.locators.KEY_PHRASE_INPUTS)
        )

        el.clear()
        el.send_keys(text, Keys.RETURN)

        return self

    def send_keys_phrases_minus(self, text):
        el = self.multiple_find(
            self.locators.KEY_PHRASE_INPUTS, WaitTime.LONG_WAIT)[1]

        el.clear()
        el.send_keys(text, Keys.RETURN)

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
        self.search_action_click(self.locators.URL_OPTIONS, 1)
        return self

    def send_text_url(self, text: str):
        el = self.find(self.locators.URL_INPUT)
        print("ELEMENT : ", el)
        el.clear()
        el.send_keys(text, Keys.RETURN)
        return self

    def is_checkbox_checked(self):
        try:
            el = self.multiple_find(
                self.locators.URL_CHECBOXES, WaitTime.SHORT_WAIT)[1]
            return el.get_attribute("checked")
        except TimeoutException:
            pass
        return False

    def wait_for_checkbox_load(self):
        WebDriverWait(self.driver, WaitTime.SHORT_WAIT).until(
            lambda _: self.is_checkbox_checked())

        return self

    def is_utm_renders(self):
        try:
            el = WebDriverWait(self.driver, WaitTime.SUPER_SHORT_WAIT).until(
                EC.visibility_of_all_elements_located(
                    self.locators.URL_OPTIONS)
            )

            return len(el) == 3 and el[1].is_displayed()
        except TimeoutException:
            pass
        return False

    def wait_for_utm_render(self):
        WebDriverWait(self.driver, WaitTime.SHORT_WAIT).until(
            lambda _: self.is_utm_renders())

        return self

    def is_utm_not_correct(self):
        return "Неверный формат utm-метки" in self.driver.page_source

    def get_to_next(self):
        self.get_page().site_region_click().click_until_next_page()
        return self

    def wait_for_adv_page(self, filter_btn) -> bool:
        try:
            self.action_click(filter_btn)
            WebDriverWait(self.driver, WaitTime.SUPER_SHORT_WAIT).until(
                lambda _: self.is_on_site_text('Предпросмотр'))
            return True
        except TimeoutException:
            pass

        return False

    def is_region_visible(self):
        try:
            el = self.multiple_find(self.locators.KEY_PHRASES_REGION)[1]
            return el.get_attribute("aria-hidden").lower() == "false"
        except TimeoutException:
            pass
        return False

    def wait_key_phrase_render(self):
        WebDriverWait(self.driver, WaitTime.MEDIUM_WAIT).until(
            lambda _: self.is_region_visible())

        return self

    def click_until_next_page(self):
        btn_to_click = self.multiple_find(self.locators.CONTINUE_BUTTON)[-1]
        WebDriverWait(self.driver, WaitTime.MEDIUM_WAIT).until(
            lambda _: self.wait_for_adv_page(btn_to_click))

        return self
