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
from ui.locators.site import SiteLocators


class SitePage(BasePage):
    url = "https://ads.vk.com/hq/pixels"
    locators = SiteLocators

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

    def click_add_button(self):
        self.click(self.locators.ADD_PIXEL_BUTTON, 15)
        return self

    def is_domen_input_exist(self):
        return bool(self.find(self.locators.INPUT_DOMEN))

    def create_pixel(self, site="ababa.com"):
        self.click_add_button()
        input = self.find(self.locators.INPUT_DOMEN)
        input.clear()
        input.send_keys(site, Keys.RETURN)

        add_btn = self.find(self.locators.ADD_BUTTON_MODAL)
        if self.action_click(add_btn).is_on_site_text("Нашли пиксели"):
            new_pix_reg = self.find(self.locators.CREATE_NEW_PIXEL_REGION)
            self.action_click(new_pix_reg)

        close_btn = self.find(self.locators.CLOSE_BUTTON)
        self.action_click(close_btn)
        return self

    def click_settings(self, what_settings=0):
        settings = self.multiple_find(self.locators.SETTINGS)
        self.action_click(settings[what_settings])
        return self

    def select_collection_checkbox(self):
        checkboxes = self.find(self.locators.CHECBOX_SETTINGS)
        self.action_click(checkboxes)
        return self

    def input_collection_data(self, text: str):
        input = self.find(self.locators.DATA_INPUT)
        input.clear()
        input.send_keys(text, Keys.RETURN)
        return self

    def is_error_on_page(self, text):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.text_to_be_present_in_element((By.XPATH, "//*"), text)
            )
            return True
        except Exception:
            return False

    def click_events(self):
        el = self.find(self.locators.EVENTS_REG)
        self.action_click(el)
        return self

    def get_url(self) -> str:
        return self.driver.current_url

    def current_id(self):
        match = re.search(r"/(\d+)/code$", self.driver.current_url)
        if match:
            return match.group(1)
        else:
            print("Can't find pixel id")
            return None

    def click_tags(self):
        el = self.find(self.locators.AUDIENCE_TAGS_REG)
        self.action_click(el)
        return self

    def click_access(self):
        el = self.find(self.locators.ACCESSABLE_REG)
        self.action_click(el)
        return self

    def click_add_event(self):
        btn = self.find(self.locators.ADD_EVENT)
        self.action_click(btn)
        return self

    def click_add_event_modal(self):
        btn = self.find(self.locators.ADD_EVENT_MODAL)
        self.action_click(btn)
        return self

    def select_manual(self):
        manual_option = self.find(self.locators.SELECT_EVENT_NAME)
        self.action_click(manual_option)
        return self

    def input_event_name(self, text: str):
        input = self.find(self.locators.INPUT_EVENT_NAME)
        input.clear()
        input.send_keys(text, Keys.RETURN)
        return self

    def select_event_category(self):
        selector = self.multiple_find(self.locators.EVENT_SELECTOR)[0]
        self.action_click(selector)
        option = self.find(self.locators.CATEGORY_BUY_OPTION)
        self.action_click(option)
        return self

    def select_event_condition(self):
        selector = self.multiple_find(self.locators.EVENT_SELECTOR)[1]
        self.action_click(selector)
        option = self.find(self.locators.CONDITION_OPTION)
        self.action_click(option)
        return self

    def input_text_url(self, text: str):
        input = self.multiple_find(self.locators.URL_INPUT)[1]
        input.clear()
        input.send_keys(text, Keys.RETURN)
        return self

    def click_add_tag(self):
        btn = self.find(self.locators.ADD_TAG)
        self.action_click(btn)
        return self

    def input_name_tag(self, text: str):
        input = self.find(self.locators.INPUT_NAME_TAG)
        input.clear()
        input.send_keys(text, Keys.RETURN)
        return self
