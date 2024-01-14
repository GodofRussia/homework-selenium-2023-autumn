from selenium.webdriver.common.by import By
from ui.locators.basic import BasePageLocators


class GroupAdvLocators(BasePageLocators):
    SEARCH_INPUT = (By.XPATH, '//*[@data-testid="search"]')
    REGION_VARIANTS = (
        By.XPATH,
        '//*[@role="tooltip"]//*[contains(@class,"Branch_branch")]',
    )

    SELECTED_RUSSIA = (
        By.XPATH,
        '//*[@class="RegionsList_wrapper__wuqdC"]//button',
    )

    SITE_REGION = (By.XPATH, '//*[@data-id="site_conversions"]')
    CONTINUE_BUTTON = (By.XPATH, '//*[@id="footer"]//button')
    SITE_INPUT = (By.XPATH, '//input[@placeholder="Введите ссылку на сайт"]')
    COST_INPUT = (By.XPATH, '//input[@data-testid="targeting-not-set"]')

    DEMOGRAPHY_REGION = (By.XPATH, '//*[@id="react-collapsed-toggle-2"]')
    AGE = (
        By.XPATH,
        '//div[@id="react-collapsed-panel-2"]//*[contains(@class, "RangeSelector_from__vlHfX AgeTargeting_select")]',
    )

    AGE_FIELD = (
        By.XPATH,
        '//div[@id="react-collapsed-panel-2"]//*[contains(@class, "AgeTargeting_select__QcsRp")]//span[contains(@tabindex,"0")]',
    )

    FOOTER_BUTTONS = (
        By.XPATH,
        '//*[@id="footer"]//*[contains(@class, "vkuiButton__in")]',
    )

    SAVE_TEXT = (
        By.XPATH,
        '//*[@id="footer"]//*[text()="Изменения сохранены"]',
    )

    INTEREST_REGION = (By.XPATH, '//*[@data-testid="section-interests"]')

    KEY_PHRASES = (By.XPATH, '//*[contains(text(), "Ключевые фразы")]')
    KEY_PHRASES_REGION = (
        By.XPATH,
        '//*[contains(@class, "InterestsSubSection_content")]',
    )
    KEY_PHRASE_INPUTS = (
        By.XPATH,
        '//div[contains(@class, "InterestsSubSection_content__VfrET")]//textarea',
    )

    DEVICES = (By.XPATH, '//*[contains(text(), "Устройства")]')
    DEVICES_OPTIONS = (By.XPATH, '//*[@name="device_types"]')

    URL_PARAMETER_REGION = (By.XPATH, '//*[@data-testid="section-urlUtm"]')
    URL_OPTIONS = (By.XPATH, '//*[@data-testid="section-urlUtm"]//label')
    URL_CHECBOXES = (
        By.XPATH,
        '//*[@data-testid="section-urlUtm"]//fieldset[contains(@class, "DisabledBlock_fieldset")]//input',
    )
    URL_INPUT = (By.XPATH, '//*[@data-testid="section-urlUtm"]//textarea')
