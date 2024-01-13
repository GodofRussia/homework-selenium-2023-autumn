from ui.pages.base_page import BasePage
from ui.locators.lk import LKPageLocators

from selenium.common.exceptions import TimeoutException
from ui.pages.consts import SidebarTabsTitles


class LKPage(BasePage):
    url = "https://ads.vk.com/hq"
    locators = LKPageLocators

    def switch_tab(self, tab, timeout=None):
        match tab:
            case SidebarTabsTitles.COMPANIES:
                return self.click(self.locators.COMPANIES_TAB_SVG, timeout)
            case SidebarTabsTitles.AUDITORIES:
                return self.click(self.locators.AUDITORIES_TAB_SVG, timeout)
            case SidebarTabsTitles.BUDGET:
                return self.click(self.locators.BUDGET_TAB_SVG, timeout)
            case SidebarTabsTitles.LEARNING:
                return self.click(self.locators.TRAINING_TAB_SVG, timeout)
            case SidebarTabsTitles.CENTER_OF_COMMERCE:
                return self.click(self.locators.COMMERCE_TAB_SVG, timeout)
            case SidebarTabsTitles.SITES:
                return self.click(self.locators.SITES_TAB_SVG, timeout)
            case SidebarTabsTitles.MOBILE_APPS:
                return self.click(self.locators.MOBILE_APP_TAB_SVG, timeout)
            case SidebarTabsTitles.LEAD_FORMS:
                return self.click(self.locators.LEAD_FORMS_TAB_SVG, timeout)
            case SidebarTabsTitles.SETTINGS:
                return self.click(self.locators.SETTINGS_TAB_SVG, timeout)
            case SidebarTabsTitles.HELP:
                return self.click(self.locators.HELP_TAB_SVG, timeout)

    def check_tab_switched(self, tab, timeout=None) -> bool:
        match tab:
            case SidebarTabsTitles.COMPANIES:
                return (
                    self.find(self.locators.COMPANIES_MAIN_PAGE, timeout)
                    is not None
                )
            case SidebarTabsTitles.AUDITORIES:
                return (
                    self.find(self.locators.AUDITORIES_MAIN_PAGE, timeout)
                    is not None
                )
            case SidebarTabsTitles.BUDGET:
                return (
                    self.find(self.locators.BUDGET_MAIN_PAGE, timeout)
                    is not None
                )
            case SidebarTabsTitles.LEARNING:
                return (
                    self.find(self.locators.STARTING_TRAINING_TITLE, timeout)
                    is not None
                )
            case SidebarTabsTitles.CENTER_OF_COMMERCE:
                return (
                    self.find(self.locators.CREATE_CATALOG_BUTTON, timeout)
                    is not None
                )
            case SidebarTabsTitles.SITES:
                return (
                    self.find(self.locators.ADD_PIXEL_BUTTON, timeout)
                    is not None
                )
            case SidebarTabsTitles.MOBILE_APPS:
                return (
                    self.find(self.locators.APP_ADD_BUTTON, timeout)
                    is not None
                )
            case SidebarTabsTitles.LEAD_FORMS:
                return (
                    self.find(self.locators.LEAD_FORMS_CREATE_BUTTON, timeout)
                    is not None
                )
            case SidebarTabsTitles.SETTINGS:
                return (
                    self.find(self.locators.GENERAL_SETTINGS_TAB, timeout)
                    is not None
                )
            case SidebarTabsTitles.HELP:
                return (
                    self.find(self.locators.COMPANY_CASES, timeout) is not None
                )

        return False

    def click_on_wrap(self, timeout=None):
        self.click(self.locators.WRAP_SIDEBAR, timeout)

    def found_redirect_titles(self, timeout=None) -> bool:
        try:
            self.find(self.locators.COMPANIES_TAB_SVG, timeout)
            return True
        except TimeoutException:
            return False
