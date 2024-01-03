import re
from ui.pages.consts import WaitTime
from ui.pages.base_page import BasePage
from ui.locators.company import CompanyPageLocators

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webelement import WebElement


class CompanyPage(BasePage):
    url = "https://ads.vk.com/hq/dashboard/ad_plans?mode=ads&attribution=impression&sort=-created"
    locators = CompanyPageLocators

    def get_current_url(self):
        return self.driver.current_url

    def create_company(self, timeout=None):
        self.click(self.locators.CREATE_BUTTON, timeout=timeout)
        return self

    def download(self, timeout=None):
        self.search_action_click_not_clickable(self.locators.DOWNLOAD_BUTTON, 0,timeout)
        return self

    def settings(self, timeout=None):
        self.search_action_click_not_clickable(self.locators.SETTINGS_BUTTON, timeout=timeout)
        return self

    def advertisment_view(self, timeout=None):
        self.click(self.locators.ADVERTISEMENTS_BUTTON, timeout=timeout)
        return self

    def select_filter(self, timeout=None):
        self.click(self.locators.FILTER_BUTTON, timeout)
        return self

    def select_deleted_filter(self):
        self.search_action_click_not_clickable(self.locators.DELETED_FILTER)
        return self

    def select_started_filter(self):
        self.search_action_click_not_clickable(self.locators.STARTED_FILTER)
        return self

    def apply_filters(self):
        self.click(self.locators.FILTER_APPLY_BUTTON)
        return self

    def select_company(self, number_of_company=0):
        self.search_action_click_not_clickable(self.locators.COMPANY_OPTIONS, number_of_company)
        return self

    def select_action_list(self):
        self.search_action_click_not_clickable(self.locators.ACTION_SELECTOR)
        return self

    def select_delete_action(self):
        self.search_action_click_not_clickable(self.locators.DELETE_ACTION)
        return self

    def group_view(self, timeout=None):
        self.click(self.locators.GROUP_BUTTON, timeout=timeout)
        return self

    def go_to_drafts(self):
        self.click(self.locators.DRAFT_BUTTON)
        return self

    def select_draft_option(self, what_to_select=0):
        self.search_action_click_not_clickable(self.locators.DRAFT_OPTIONS, what_to_select)
        return el

    def delete_draft(self):
        self.click(self.locators.DELETE_DRAFT)
        return self

    def get_selector_attribute(self):
        return self.find(self.locators.ACTION_SELECTOR).get_attribute("class")

    def click_approve_delete(self):
        self.self.search_action_click_not_clickable(self.locators.DELETE_MODAL)
        return self

    def not_on_site(self, text: str):
        res = self.is_on_site_text(text)
        return not res

    def wait_until_draft_delete(self, el: WebElement):
        try:
            WebDriverWait(self.driver, WaitTime.LONG_WAIT).until(EC.staleness_of(el))
        except TimeoutException:
            pass

        return self
