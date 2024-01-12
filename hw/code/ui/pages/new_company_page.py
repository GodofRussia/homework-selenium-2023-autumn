import time
from ui.pages.consts import BASE_POSITIONS, INPUT_TEXT, LABELS, URLS, WaitTime
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from ui.pages.base_page import BasePage
from ui.locators.new_company import NewCompanyPageLocators

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException


class NewCompanyPage(BasePage):
    url = URLS.new_ad
    locators = NewCompanyPageLocators

    def send_keys_with_enter(self, element: WebElement, keys_to_send: str):
        element.click()
        element.clear()
        element.send_keys(keys_to_send, Keys.RETURN)

        return self

    def site_region_click(self, timeout=WaitTime.LONG_WAIT):
        self.click(self.locators.SITE_REGION, timeout)
        return self

    def catalog_region_click(self):
        self.click(self.locators.CATALOG_REGION)
        return self

    def lead_region_click(self):
        self.click(self.locators.LEAD_FORM_REGION)
        return self

    def continue_click(self, timeout=WaitTime.LONG_WAIT):
        self.search_action_click(
            locator=self.locators.CONTINUE_BUTTON, what_choose=BASE_POSITIONS.last_search_pos, timeout=timeout)
        return self

    def send_keys_site(self, text, timeout=WaitTime.MEDIUM_WAIT):
        el = self.find(self.locators.SITE_INPUT, timeout)
        self.send_keys_with_enter(el, text)
        return self

    def send_cost(self, cost, timeout=WaitTime.LONG_WAIT):
        el = self.find(self.locators.COST_INPUT, timeout)
        el.clear()
        el.send_keys(cost, Keys.RETURN)
        return self

    def delete_symbols_from_field(self, field_locator, count_delete):
        el = self.find(field_locator)
        el.send_keys(Keys.END)
        for i in range(count_delete):
            el.send_keys(Keys.BACKSPACE)
        return self

    def click_selector_strategy(self):
        selector = self.find(
            self.locators.SELECTOR_STRATEGY, WaitTime.SHORT_WAIT)
        self.action_click(selector)

        return self

    def select_min_cost(self):
        elements = self.find(self.locators.MIN_STRATEGY)
        self.action_click(elements)
        return self

    def select_pred_cost(self):
        elements = self.find(self.locators.PRED_STRATEGY)
        self.action_click(elements)
        return self

    def send_max_click_cost(self, cost):
        el = self.find(self.locators.MAX_CLICK_COST)
        self.send_keys_with_enter(el, cost)
        return self

    def select_vk_group(self, group: str):
        self.click(self.locators.RADIO_BUTTON_VK_GROUP)
        self.click(self.locators.GROUP_SELECTOR)
        self.click(self.locators.VK_ANOTHER_GROUP)

        input_group = self.find(self.locators.VK_INPUT_ANOTHER_GROUP)
        self.send_keys_with_enter(input_group, group)

        self.click(self.locators.ADD_BUTTON_GROUP)
        return self

    def select_split(self):
        self.click(self.locators.SPLIT_CHECKBOX)
        return self

    def select_lead_click(self, what_lead: int):
        element = WebDriverWait(self.driver, WaitTime.MEDIUM_WAIT).until(
            EC.presence_of_all_elements_located(
                self.locators.SELECTOR_LEAD
            )
        )

        self.action_click(element[what_lead])
        return self

    def select_lead_option(self, what_option: int = BASE_POSITIONS.first_search_pos):
        self.search_action_click(
            self.locators.SELECT_LEAD_OPTION, what_option)

    def click_date(self):
        self.search_action_click(self.locators.DATE_PICKER)
        return self

    def select_prev_month(self):
        self.search_action_click(self.locators.DATE_LAST_MONTH_BUTTON)
        return self

    def click_first_day(self):
        self.search_action_click(self.locators.FIRST_DAY)
        return self

    def is_already_selected(self):
        return self.find(self.locators.ERROR_ALREADY_SELECTED)

    def is_not_found_community(self):
        return self.find(self.locators.ERROR_NOT_FOUND_COM)

    def is_must_field(self):
        return self.find(self.locators.ERROR_MUST_FIELD)

    def is_less_than_hundred(self):
        return self.find(self.locators.ERROR_LESS_THAN_HUN)

    def wait_for_next_page(self, filter_btn) -> bool:
        try:
            self.action_click(filter_btn)
            WebDriverWait(self.driver, WaitTime.SUPER_SHORT_WAIT).until(
                lambda _: self.is_on_site_text(LABELS.show_regions))
            return True
        except TimeoutException:
            pass

        return False

    def click_until_next_page(self):
        filter_btn = self.multiple_find(self.locators.CONTINUE_BUTTON)[
            BASE_POSITIONS.last_search_pos]
        WebDriverWait(self.driver, WaitTime.MEDIUM_WAIT).until(
            lambda _: self.wait_for_next_page(filter_btn))

        return self

    def get_to_next(self):
        self.site_region_click().send_keys_site(URLS.test_site).send_cost(
            INPUT_TEXT.corrected_cost
        )
        self.click_until_next_page()
        return self
