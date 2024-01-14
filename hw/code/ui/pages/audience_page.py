from ui.pages.base_page import BasePage

from ui.pages.consts import AUDIENCE_USER_LIST_URL as USER_LIST_URL, POSITIONS_SITE

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from ui.locators.audience import AudienceLocators
from selenium.common.exceptions import TimeoutException, JavascriptException

from ui.pages.consts import (
    BASE_POSITIONS,
    POSITIONS_AUDIENCE,
    URLS,
    WaitTime,
)


class AudiencePage(BasePage):
    url = URLS.audience_url
    locators = AudienceLocators

    def click_create_button(self):
        self.search_action_click(self.locators.CREATE_BUTTON)
        return self

    def write_text_to_name(self, text, timeout=None):
        field = self.find(self.locators.CREATION_NAME_AUDITORY)

        self.wait(timeout).until(
            EC.element_to_be_clickable(self.locators.CREATION_NAME_AUDITORY)
        )

        self.send_keys_with_enter(field, text)
        return self

    def click_add_source(self):
        self.search_action_click(self.locators.ADD_SOURCE)
        return self

    def select_lead_region(self):
        self.search_action_click(self.locators.LEAD_REGION)
        return self

    def click_lead_input(self):
        self.search_action_click(self.locators.LEAD_INPUT)
        return self

    def select_lead_option(self, what_option=BASE_POSITIONS.first_search_pos):
        self.search_action_click(self.locators.LEAD_OPTIONS, what_option)
        return self

    def click_checkbox_lead(self,
                            what_checkbox=BASE_POSITIONS.first_search_pos):
        self.search_action_click(self.locators.LEAD_CHECKBOXES, what_checkbox)
        return self

    def write_to_from_field(self, form_days: int):
        input = self.multiple_find(self.locators.LEAD_INPUT_DAYS)
        from_input = input[POSITIONS_AUDIENCE.from_input_days]

        self.remove_symbols_from_el(
            from_input, len(str(self.get_from_value())))
        self.send_keys_with_enter(from_input, form_days)
        return self

    def write_to_to_field(self, form_days: int):
        input = self.multiple_find(self.locators.LEAD_INPUT_DAYS)
        from_input = input[POSITIONS_AUDIENCE.to_input_days]

        self.remove_symbols_from_el(from_input, len(str(self.get_to_value())))
        self.send_keys_with_enter(from_input, form_days)
        return self

    def get_from_value(self) -> int:
        input = self.multiple_find(self.locators.LEAD_INPUT_DAYS)

        value = input[POSITIONS_AUDIENCE.from_input_days].get_attribute(
            "value")
        assert value is not None
        return int(value)

    def get_to_value(self) -> int:
        input = self.multiple_find(self.locators.LEAD_INPUT_DAYS)

        value = input[POSITIONS_AUDIENCE.to_input_days].get_attribute("value")
        assert value is not None
        return int(value)

    def select_key_phrases_region(self):
        self.search_action_click(self.locators.KEY_PHRASES_REGION)
        return self

    def write_to_period(self, period: int):
        period_field = self.find(self.locators.KEY_DAYS_PERIOD)

        self.remove_symbols_from_el(
            period_field, len(str(self.get_period_value())))

        self.send_keys_with_enter(period_field, period)

        return self

    def get_period_value(self) -> int:
        period_field = self.find(self.locators.KEY_DAYS_PERIOD)

        value = period_field.get_attribute("value")
        assert value is not None
        return int(value)

    def is_modal_exist(self):
        try:
            el = self.multiple_find(self.locators.SAVE_BUTTON,
                                    WaitTime.SUPER_SHORT_WAIT)

            if not el:
                return True
            try:
                self.search_action_click_not_clickable(
                    self.locators.SAVE_BUTTON)
            except (TimeoutException, JavascriptException) as e:
                pass

            return False
        except TimeoutException:
            pass

        return True

    def click_save_button(self):
        self._wait_until_func_true(
            lambda _: self.is_modal_exist(), WaitTime.SUPER_LONG_WAIT)
        return self

    def click_save_button_without_wait(self):
        self.search_action_click(self.locators.SAVE_BUTTON)
        return self

    def click_save_button_modal(self):
        self.search_action_click(
            self.locators.SAVE_BUTTON, POSITIONS_AUDIENCE.save_button_modal)
        return self

    def click_user_list(self):
        self.search_action_click(
            self.locators.USER_LIST, POSITIONS_AUDIENCE.user_list)
        return

    def is_user_list_url(self) -> bool:
        return USER_LIST_URL == self.driver.current_url

    def select_vk_group_region(self):
        self.search_action_click(
            self.locators.VK_GROUP_REGION,
            timeout=WaitTime.SUPER_LONG_WAIT
        )

        return self

    def write_to_vk_group(self, text: str):
        input = self.find(self.locators.VK_GROUP_INPUT, WaitTime.LONG_WAIT)

        self.send_keys_with_enter(input, text)

        return self

    def select_vk_group(self):
        self.search_action_click(
            self.locators.VK_GROUPS,
            timeout=WaitTime.SUPER_LONG_WAIT
        )
        self.search_action_click(
            self.locators.VK_GROUPS_OPTIONS,
            timeout=WaitTime.SUPER_LONG_WAIT
        )

        self.empty_click()
        return self

    def empty_click(self):
        self.search_action_click(self.locators.VK_GROUP_TEXT)
        return self

    def get_name_audience(self) -> str:
        elem = self.find(self.locators.CREATION_NAME_AUDITORY)
        value = elem.get_attribute("value")
        assert value is not None
        return value

    def select_vk_group_filter(self):
        self.filter_click()

        self.search_action_click(self.locators.SUBSCRIBER_VK_GROUP)
        self.search_action_click(self.locators.APPLY_BUTTON)

        return self

    def delete_source(self, what_source=BASE_POSITIONS.first_search_pos):
        self.search_action_click(
            self.locators.SOURCE_BUTTONS, what_source * 2 + 1
        )

        self.click_until_confirm_show(
            self.locators.DELETE_ICON, POSITIONS_AUDIENCE.delete_source_btn)

        self.search_action_click(
            self.locators.CONFRIM_BUTTONS,
            POSITIONS_AUDIENCE.delete_confirm_btn
        )

        self.wait_for_confirm_box_dissappear()
        return self

    def is_confirm(self, locator, position):
        try:
            self.search_action_click(
                locator, position, WaitTime.SUPER_SHORT_WAIT)

            return self.find(self.locators.CONFRIM_BUTTONS)
        except TimeoutException:
            pass

        return False

    def click_until_confirm_show(self, locator, position):
        self._wait_until_func_true(
            lambda _: self.is_confirm(locator, position))
        return self

    def wait_for_dropdown_filter(self, filter_btn) -> bool:
        try:
            self.action_click(filter_btn)
            self.find(self.locators.FILTER_DROPDOWN_EXIST,
                      WaitTime.SUPER_SHORT_WAIT)

            return True
        except TimeoutException:
            pass

        return False

    def filter_click(self):
        filter_btn = self.multiple_find(self.locators.FILTER_BUTTON)[
            POSITIONS_AUDIENCE.filter_btn]
        self.wait(WaitTime.LONG_WAIT).until(
            lambda _: self.wait_for_dropdown_filter(filter_btn))

        return self

    def _is_value_equal(self, locator, what_element, value):
        try:
            el = self.multiple_find(locator)[what_element]

            return el.get_attribute("value") == str(value)
        except TimeoutException:
            pass

        return False

    def _wait_until_func_true(self, func, timeout=WaitTime.LONG_WAIT):
        self.wait(timeout).until(func)
        return self

    def _wait_until_value_equal(self, locator, what_element, old_value):
        self.wait(WaitTime.LONG_WAIT).until(
            lambda _: self._is_value_equal(locator, what_element, old_value)
        )

        return self

    def wait_to_field_equal(self, value):
        self._wait_until_value_equal(
            self.locators.LEAD_INPUT_DAYS,
            POSITIONS_AUDIENCE.from_input_days,
            value)
        return self

    def wait_from_filed_equal(self, value):
        self._wait_until_value_equal(
            self.locators.LEAD_INPUT_DAYS,
            POSITIONS_AUDIENCE.to_input_days,
            value)
        return self

    def wait_period_filed_equal(self, value):
        self._wait_until_value_equal(
            self.locators.KEY_DAYS_PERIOD,
            POSITIONS_AUDIENCE.period_pos,
            value)
        return self

    def wait_for_confirm_box_dissappear(self):
        self.wait(WaitTime.LONG_WAIT).until_not(
            EC.presence_of_all_elements_located(self.locators.CONFRIM_BUTTONS))
        return self

    def delete_all_auditories(self):
        while True:
            try:
                grid_id = self.multiple_find(self.locators.GRID_IDS)[0]
                element = self.multiple_find(self.locators.MORE_OPTIONS)[0]
                self.js_click(element)

                self.search_action_click(
                    self.locators.DELETE_OPTION,
                    POSITIONS_AUDIENCE.delete_btn_pop_up,
                    WaitTime.SHORT_WAIT)

                delete_button = self.multiple_find(self.locators.MODAL_BUTTONS)[  # type: ignore
                    POSITIONS_SITE.delete_modal_btn]
                self.action_click(delete_button)

                self.wait(WaitTime.MEDIUM_WAIT).until(
                    EC.staleness_of(delete_button))
                self.wait(WaitTime.LONG_WAIT).until(EC.staleness_of(grid_id))
            except TimeoutException:
                break

        return self
