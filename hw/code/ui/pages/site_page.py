import re
import time
from ui.pages.consts import WaitTime

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
from selenium.common.exceptions import TimeoutException


class SitePage(BasePage):
    url = "https://ads.vk.com/hq/pixels"
    locators = SiteLocators

    def click_add_button(self):
        self.click(self.locators.ADD_PIXEL_BUTTON, WaitTime.MEDIUM_WAIT)
        return self

    def is_domen_input_exist(self):
        return bool(self.find(self.locators.INPUT_DOMEN))

    # Return id of pixel
    def create_pixel(self, site="ababababba.com"):
        self.click_add_button()
        input = self.find(self.locators.INPUT_DOMEN)
        input.clear()
        input.send_keys(site, Keys.RETURN)

        self.search_action_click(self.locators.ADD_BUTTON_MODAL)
        if self.is_on_site_text("Нашли пиксели"):
            self.search_action_click(self.locators.CREATE_NEW_PIXEL_REGION)
    
        value = self.find(self.locators.PIXEL_ID, WaitTime.LONG_WAIT)
        self.search_action_click(self.locators.CLOSE_BUTTON)
        
        match = re.search(r'\d+', value.text)
        if match:
            print("Pixel match", match.group())
            return match.group()
        else:
            return 0
    
    def wait_for_pixel(self, id:str):
        self.is_on_site_text(id, WaitTime.MEDIUM_WAIT)
        return self

    def select_collection_checkbox(self):
        self.search_action_click(self.locators.CHECBOX_SETTINGS)
        return self

    def input_collection_data(self, text: str):
        input = self.find(self.locators.DATA_INPUT)
        input.clear()
        input.send_keys(text, Keys.RETURN)
        return self

    # TODO Maybe is_on_page
    def is_error_on_page(self, text):
        try:
            WebDriverWait(self.driver, WaitTime.MEDIUM_WAIT).until(
                EC.text_to_be_present_in_element((By.XPATH, "//*"), text)
            )
            return True
        except Exception:
            return False

    def click_events(self):
        self.search_action_click(self.locators.EVENTS_REG)
        return self

    def get_url(self) -> str:
        return self.driver.current_url

    def current_id(self):
        match = re.search(r"/(\d+)/code$", self.driver.current_url)
        if match:
            return match.group(1)
        else:
            return None

    def click_tags(self):
        self.search_action_click(self.locators.AUDIENCE_TAGS_REG)
        return self

    def click_access(self):
        self.search_action_click(self.locators.ACCESSABLE_REG)
        return self

    def click_add_event(self):
        self.search_action_click(self.locators.ADD_EVENT)
        return self

    def click_add_event_modal(self):
        self.search_action_click(self.locators.ADD_EVENT_MODAL)
        return self

    def select_manual(self):
        self.search_action_click(self.locators.SELECT_EVENT_NAME)
        return self

    def input_event_name(self, text: str):
        input = self.find(self.locators.INPUT_EVENT_NAME)
        input.clear()
        input.send_keys(text, Keys.RETURN)
        return self

    def select_event_category(self):
        self.search_action_click(self.locators.EVENT_SELECTOR,0)
        self.search_action_click(self.locators.CATEGORY_BUY_OPTION)
        return self

    def select_event_condition(self):
        self.search_action_click(self.locators.EVENT_SELECTOR,1)
        self.search_action_click(self.locators.CONDITION_OPTION)
        return self

    def input_text_url(self, text: str):
        input = self.multiple_find(self.locators.URL_INPUT)[1]
        input.clear()
        input.send_keys(text, Keys.RETURN)
        return self

    def click_add_tag(self):
        self.search_action_click(self.locators.ADD_TAG)
        return self

    def input_name_tag(self, text: str):
        input = self.find(self.locators.INPUT_NAME_TAG)
        input.clear()
        input.send_keys(text, Keys.RETURN)
        return self

    def delete_pixel(self, what_delete:int = 0):
        element = self.multiple_find(self.locators.MORE_OPTIONS)[what_delete]
        self.driver.execute_script("arguments[0].click();", element)

        self.search_action_click(
            self.locators.DELETE_OPTION, 1,  WaitTime.SHORT_WAIT)
        
        delete_button = self.multiple_find(self.locators.MODAL_BUTTONS)[1]
        self.action_click(delete_button)
        
        WebDriverWait(self.driver, WaitTime.MEDIUM_WAIT).until(
            EC.staleness_of(delete_button))
        return self

    def wait_for_settings(self, locator, what_element) -> bool:
        try:
            el = self.multiple_find(locator)[what_element]
            self.action_click(el)
            WebDriverWait(self.driver, WaitTime.SHORT_WAIT).until(
                EC.presence_of_element_located(self.locators.SETTINGS_PAGE_ELEMENT))
            return True
        except TimeoutException:
            pass

        return False

    def click_settings_until_change(self, what_element = 0):
        WebDriverWait(self.driver, WaitTime.MEDIUM_WAIT).until(
            lambda _: self.wait_for_settings(self.locators.SETTINGS, what_element))

        return self
