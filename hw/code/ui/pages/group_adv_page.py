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

    def action_click(self, element):
        self.driver.execute_script(
            "arguments[0].scrollIntoView(true);", element
        )
        actions = ActionChains(self.driver, WaitTime.LONG_WAIT)
        actions.move_to_element(element)
        actions.click(element)
        actions.perform()
        return self

    def site_region_click(self):
        self.click(self.locators.SEARCH_INPUT)
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
        self.action_click(self.find(self.locators.DEMOGRAPHY_REGION))
        return self

    def select_bottom_age(self, age: int):
        el = self.multiple_find(self.locators.AGE_FIELD)[0]

        self.action_click(el)
        el.send_keys(age, Keys.RETURN)

        return self

    def select_upper_age(self, age: int):
        el = self.multiple_find(locator=self.locators.AGE_FIELD)[1]
        self.action_click(el)
        el.send_keys(age, Keys.RETURN)

        return self

    def get_upper_age(self):
        el = self.multiple_find(self.locators.AGE_FIELD)[1]
        return el.get_attribute("value")

    def get_lower_age(self):
        el = self.multiple_find(self.locators.AGE_FIELD)[0]
        return el.get_attribute("value")

    def click_continue_button(self):
        el = self.multiple_find(self.locators.FOOTER_BUTTONS)[1]
        self.action_click(el)
        return self

    def wait_load_page(self):
        self.multiple_find(self.locators.SAVE_TEXT)[0]

        return self

    def click_interest_region(self, timeout=WaitTime.MEDIUM_WAIT):
        self.action_click(
            self.multiple_find(self.locators.INTEREST_REGION, timeout)[0]
        )
        return self

    def click_key_phrases(self, timeout=WaitTime.MEDIUM_WAIT):
        self.action_click(self.find(self.locators.KEY_PHRASES, timeout))

        return self

    def send_key_phrases(self, text: str, timeout=WaitTime.MEDIUM_WAIT):
        el = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(self.locators.KEY_PHRASE_INPUTS)
        )

        el.clear()
        el.send_keys(text, Keys.RETURN)

        return self

    def send_keys_phrases_minus(self, text):
        el = self.multiple_find(self.locators.KEY_PHRASE_INPUTS)[1]

        el.clear()
        el.send_keys(text, Keys.RETURN)

        return self

    def click_device_region(self):
        self.action_click(self.find(self.locators.DEVICES))
        return self

    def remove_device(self, what_device: int):
        self.action_click(
            self.multiple_find(self.locators.DEVICES_OPTIONS)[what_device]
        )
        return self

    def is_disabled_and_cheked_device(self, what_device: int):
        el = self.multiple_find(self.locators.DEVICES_OPTIONS)[what_device]
        disalbed_att = el.get_attribute("disabled")
        checked_att = el.get_attribute("checked")

        return disalbed_att and checked_att

    def click_url_region(self):
        self.action_click(self.find(self.locators.URL_PARAMETER_REGION))
        return self

    def select_utm(self):
        self.action_click(self.multiple_find(self.locators.URL_OPTIONS)[1])
        return self

    def send_text_url(self, text: str):
        el = self.find(self.locators.URL_INPUT)

        el.clear()
        el.send_keys(text, Keys.RETURN)
        return self

    def is_utm_not_correct(self):
        return "Неверный формат utm-метки" in self.driver.page_source

    def get_to_next(self):
        self.get_page().site_region_click().click_continue_button()
        return self
