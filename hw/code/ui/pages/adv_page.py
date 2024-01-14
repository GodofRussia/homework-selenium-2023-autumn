import re

from ui.locators.adv import AdvLocators
from ui.pages.base_page import BasePage
from ui.pages.group_adv_page import GroupAdvPage

from ui.pages.consts import URLS, WaitTime, BASE_POSITIONS, POSITIONS_ADV

from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class AdvPage(BasePage):
    url = URLS.new_ad
    locators = AdvLocators

    def get_page(self):
        page = GroupAdvPage.__new__(GroupAdvPage)
        page.driver = self.driver
        page.get_to_next()

        return self

    def click_continue_button(self):
        self.search_action_click(
            self.locators.FOOTER_BUTTONS, POSITIONS_ADV.continue_button
        )
        return self

    def send_text_to_title(self, text: str):
        el = self.multiple_find(self.locators.INPUT_TITLE)[
            POSITIONS_ADV.title_position
        ]
        self.send_keys_with_enter(el, text)

        return self

    def get_title_max(self) -> int:
        el = self.multiple_find(self.locators.COUNTS_CHARS)[
            POSITIONS_ADV.title_position
        ]
        text = el.text

        matches = re.search(r"\d+ / (\d+)", text)
        count_chars_value = 0
        if matches:
            count_chars_value = int(matches.group(1))

        return count_chars_value

    def send_url(self, url: str):
        el = self.find(self.locators.URL_INPUT)
        self.send_keys_with_enter(el, url)

        return self

    def wait_logo_dissapper(self):
        el = self.multiple_find(self.locators.LOG_VARIANTS)[
            BASE_POSITIONS.first_search_pos
        ]

        self.wait(WaitTime.SUPER_SHORT_WAIT).until(EC.staleness_of(el))
        return self

    def select_logo(
        self, number_of_logo: int = BASE_POSITIONS.first_search_pos
    ):
        self.search_action_click(self.locators.LOGO_INPUT)
        self.search_action_click(self.locators.LOG_VARIANTS, number_of_logo)

        return self

    def write_to_inputs(self, text: str):
        inputs = self.multiple_find(self.locators.TEXT_INPUTS)

        for i in inputs:
            self.send_keys_with_enter(i, text)

        return self

    def write_to_textarea(self, text: str):
        areas = self.multiple_find(self.locators.AREA_INPUTS)
        for i in areas:
            self.send_keys_with_enter(i, text)

        return self

    def get_company_name(self):
        return self.find(self.locators.COMPANY_NAME).text

    def click_send_button(self, timeout=WaitTime.LONG_WAIT):
        self.click(self.locators.SEND_BUTTON)
        return self

    def create_company(self, url, timeout=WaitTime.LONG_WAIT) -> str:
        self.get_page()

        self.select_logo(BASE_POSITIONS.first_search_pos).write_to_inputs(
            url,
        )
        self.write_to_textarea(url)

        name = self.get_company_name()

        self.click_media_upload().wait_load_upload_modal()
        self.select_media_options().add_media_option()
        self.click_continue_until_modal().click_send_button()
        self.wait_for_company_page()

        return name

    def wait_for_company_page(self):
        self.multiple_find(self.locators.FILTER_BUTTON, WaitTime.LONG_WAIT)
        return self

    def wait_for_only_one_upload_field(self):
        return (
            len(
                self.multiple_find(
                    self.locators.CHOOSE_MEDIA, WaitTime.SUPER_SHORT_WAIT
                )
            )
            == 1
        )

    def click_media_upload(self):
        self.wait(WaitTime.SUPER_LONG_WAIT).until(
            lambda _: self.wait_for_only_one_upload_field()
        )
        self.click(self.locators.CHOOSE_MEDIA)
        return self

    def select_media_options(self, options=BASE_POSITIONS.first_search_pos):
        self.search_action_click(self.locators.MEDIA_OPTIONS, options)
        return self

    def add_media_option(self):
        self.search_action_click(self.locators.ADD_MEDIA)
        return self

    def upload_logo(self, file):
        self.search_action_click(
            locator=self.locators.LOGO_INPUT, timeout=WaitTime.LONG_WAIT
        )

        file_input = self.find(self.locators.LOGO_INPUT_FILE)
        file_input.send_keys(file)

        el = self.find(self.locators.LOADING_IMG)
        self.wait(WaitTime.LONG_WAIT).until(EC.staleness_of(el))

        self.search_action_click(self.locators.CLOSE_MODAL)
        return self

    def wait_for_modal(self, locator, position) -> bool:
        try:
            self.search_action_click(locator, position)
            self.find(self.locators.MODAL_WIN)

            return True
        except TimeoutException:
            pass

        return False

    def click_continue_until_modal(self):
        self.wait(timeout=WaitTime.LONG_WAIT).until(
            lambda _: self.wait_for_modal(
                self.locators.FOOTER_BUTTONS, BASE_POSITIONS.last_search_pos
            )
        )

        return self

    def wait_load_upload_modal(self):
        self.wait(timeout=WaitTime.MEDIUM_WAIT).until(
            EC.visibility_of_all_elements_located(self.locators.MEDIA_OPTIONS)
        )
        return self
