import re
import time
from ui.pages.consts import BASE_POSITIONS, CLASSES, URLS, WaitTime
from ui.pages.base_page import BasePage
from ui.locators.company import CompanyPageLocators
from urllib.parse import urlparse

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webelement import WebElement


class CompanyPage(BasePage):
    url = URLS.company_url
    locators = CompanyPageLocators

    def is_matching_link(self, link, base_url):
        parsed_link = urlparse(link)
        parsed_base_url = urlparse(base_url)

        return (
            parsed_link.scheme == parsed_base_url.scheme
            and parsed_link.netloc == parsed_base_url.netloc
            and parsed_link.path.startswith(parsed_base_url.path)
        )

    def create_company(self, timeout=None):
        if not timeout:
            timeout = WaitTime.MEDIUM_WAIT
        self.click(self.locators.CREATE_BUTTON, timeout)
        return self

    def download(self, timeout=None):
        self.search_action_click_not_clickable(
            self.locators.DOWNLOAD_BUTTON, 0, timeout)
        return self

    def settings(self, timeout=None):
        self.search_action_click_not_clickable(
            self.locators.SETTINGS_BUTTON, timeout=timeout)
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
        self.search_action_click_not_clickable(
            self.locators.COMPANY_OPTIONS, number_of_company)
        return self

    def select_action_list(self):
        self.search_action_click_not_clickable(self.locators.ACTION_SELECTOR)
        return self

    def select_delete_action(self):
        self.search_action_click_not_clickable(self.locators.DELETE_ACTION)
        return self

    def group_view(self, timeout=None):
        self.click(self.locators.GROUP_BUTTON, timeout)
        return self

    def go_to_drafts(self):
        self.click(self.locators.DRAFT_BUTTON)
        return self

    def select_draft_option(self):
        el = self.multiple_find(self.locators.DRAFT_OPTIONS)[
            BASE_POSITIONS.first_search_pos]
        self.click(self.locators.DRAFT_OPTIONS)
        return el

    def delete_draft(self):
        self.click(self.locators.DELETE_DRAFT)
        return self

    def get_selector_attribute(self):
        return self.find(
            locator=self.locators.ACTION_SELECTOR).get_attribute("class")

    def click_approve_delete(self):
        self.search_action_click_not_clickable(self.locators.DELETE_MODAL)
        return self

    def wait_until_draft_delete(self, el: WebElement):
        try:
            WebDriverWait(self.driver, WaitTime.LONG_WAIT).until(
                EC.staleness_of(el))
        except TimeoutException:
            pass

        return self

    def wait_for_dropdown_filter(self, filter_btn) -> bool:
        try:
            self.action_click(filter_btn)
            WebDriverWait(self.driver, WaitTime.SUPER_SHORT_WAIT).until(
                EC.presence_of_element_located(self.locators.FILTER_EXIST))
            return True
        except TimeoutException:
            pass

        return False

    def filter_click(self):
        filter_btn = self.find(self.locators.FILTER_BUTTON)
        WebDriverWait(self.driver, WaitTime.LONG_WAIT).until(
            lambda _: self.wait_for_dropdown_filter(filter_btn))

        return self

    def is_ad_plan(self):
        return self.is_matching_link(
            self.driver.current_url,
            URLS.ad_plan_url
        )

    def is_ad_groups(self):
        return self.is_matching_link(
            self.driver.current_url,
            URLS.ad_groups_url
        )

    def is_advertisment(self):
        return self.is_matching_link(
            self.driver.current_url,
            URLS.ads_url
        )

    def selector_has_pop_down(self):
        return CLASSES.pop_down not in str(self.get_selector_attribute())

    def delete_all_actions(self):
        while True:
            try:
                self.select_company().select_action_list()
                self.select_delete_action()
            except TimeoutException:
                break
        return self

    def delete_all_drafts(self):
        while True:
            try:
                cnt = self.select_draft_option()
                self.delete_draft().click_approve_delete()
                self.wait_until_draft_delete(cnt)
            except TimeoutException:
                break
        return self

    def delete_all_companies(self):
        while True:
            try:
                cnt = self.get_company_numbers()
                self.select_company().select_action_list()
                self.select_delete_action()
                self.wait_until_company_changes(cnt)
            except TimeoutException:
                break
        return self

    def get_company_numbers(self):
        el = self.find(
            self.locators.COMPANY_NUMBER_PLACE)
        match = re.search(r'\d+', el.text)

        if match:
            return int(match.group())

        return 0

    def wait_until_company_changes(self, previous_company_number):
        WebDriverWait(self.driver, WaitTime.MEDIUM_WAIT).until_not(
            EC.text_to_be_present_in_element(
                (By.XPATH, '//*'), f"Итого: {previous_company_number}")
        )
        return self
