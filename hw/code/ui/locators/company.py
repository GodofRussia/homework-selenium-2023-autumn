from selenium.webdriver.common.by import By
from ui.locators.basic import BasePageLocators


class CompanyPageLocators(BasePageLocators):
    GROUP_BUTTON = (By.ID, "dashboardV2.groups")
    ADVERTISEMENTS_BUTTON = (By.ID, "dashboardV2.ads")
    SETTINGS_BUTTON = (By.CLASS_NAME, "TableSettings_settingsButton__uz8xK")
    DOWNLOAD_BUTTON = (By.CLASS_NAME, "tableActions_downloadButton__Kuuoy")
    CREATE_BUTTON = (By.XPATH, '//*[@data-testid="create-button"]')

    ACTION_SELECTOR = (By.XPATH, '//*[@data-testid="select-options"]')

    DOWNLOAD_DROPDOWN = (By.CLASS_NAME, "Dropdown_content__53ZvI")
    SETTINGS_DROPDOWN = (By.CLASS_NAME, "PresetsMenu_wrapper__CcwQ-")

    FILTER_FIELD = (By.XPATH, '//*[@data-testid="filter-search-input"]')
    FILTER_BUTTON = (By.XPATH, '//*[@data-testid="filter-button"]')
    DELETED_FILTER = (
        By.XPATH,
        '//*[contains(@class,"CreateFilter_filterList")]//*[contains(text(), "Удаленные")]',
    )

    FILTER_APPLY_BUTTON = (By.XPATH, '//*[contains(text(), "Применить")]')
    COMPANY_OPTIONS = (
        By.XPATH,
        "//div[@data-entityid]//label[contains(@class, 'vkuiCheckbox')]//input[@type='checkbox']",
    )
    STARTED_FILTER = (By.XPATH, '//*[contains(text(), "Запущенные")]')
    DELETE_ACTION = (By.XPATH, '//*[contains(text(), "Удалить")]')

    DRAFT_BUTTON = (By.XPATH, '//*[@data-testid="drafts-button"]')
    DELETE_DRAFT = (By.XPATH, '//*[@data-testid="delete-button"]')

    DELETE_MODAL = (
        By.XPATH,
        '//*[contains(@id, "modal")]//button//span[contains(text(),"Удалить")]',
    )

    DRAFT_OPTIONS = (
        By.XPATH,
        # "//div[@data-entityid]//label[contains(@class, 'vkuiCheckbox')]//input[@type='checkbox']",
        "//div[@data-entityid]//label[contains(@class, 'vkuiCheckbox')]",
    )

    COUNT_LINE = (By.XPATH, '//*[contains(@class, "nameCell_footerCell")]')
    GRIDS = (
        By.XPATH,
        '//*[contains(@class,"BaseTable__body")]//*[@role="gridcell"]',
    )

    FILTER_EXIST = (By.XPATH, '//div[contains(@class, "form_wrap")]')