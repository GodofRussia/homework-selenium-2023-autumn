from selenium.webdriver.common.by import By
from ui.locators.basic import BasePageLocators


class AdvLocators(BasePageLocators):
    SEARCH_INPUT = (By.XPATH, '//*[@data-testid="search"]')
    REGION_VARIANTS = (
        By.XPATH,
        '//*[@role="tooltip"]//*[contains(@class,"Branch_branch")]',
    )

    SITE_REGION = (By.XPATH, '//*[@data-id="site_conversions"]')
    CONTINUE_BUTTON = (By.XPATH, '//*[@id="footer"]//button')
    SITE_INPUT = (By.XPATH, '//input[@placeholder="Введите ссылку на сайт"]')
    COST_INPUT = (By.XPATH, '//input[@data-testid="targeting-not-set"]')

    FOOTER = (
        By.XPATH,
        '//*[@id="footer"]',
    )
    FOOTER_BUTTONS = (
        By.XPATH,
        '//*[@id="footer"]//*[contains(@class, "vkuiButton__in")]',
    )

    AUTOGEN = (By.XPATH, '//div[contains(@class, "AutogenOpener")]')
    GENERATION_TEXT_INPUTS = (
        By.XPATH,
        '//div[contains(@class, "AutogenModal_modalContent")]//textarea',
    )
    GENERATE_BUTTON = (
        By.XPATH,
        '//div[contains(@class, "AutogenModal_modalContent")]//button',
    )

    GENERATE_ERROR = (
        By.XPATH,
        '//div[contains(@class, "AutogenModal_modalContent")]//*[contains(text(), "Ошибка валидации текста: Недостаточно слов:")]',
    )
    INPUT_TITLE = (By.XPATH, '//input[@data-testid="text-field"]')
    COUNTS_CHARS = (By.XPATH, '//div[@class="FormItem_topRight__C-aii"]')

    URL_INPUT = (By.XPATH, '//*[@placeholder="Рекламируемая страница сайта"]')

    LOGO_INPUT = (By.XPATH, '//*[@data-testid="set-global-image"]')
    LOG_VARIANTS = (
        By.XPATH,
        '//*[@id="media-library-image"]//div[contains(@class, "ImageItems_active")]',
    )

    TEXT_INPUTS = (By.XPATH, '//input[@type="text"]')
    AREA_INPUTS = (By.XPATH, "//textarea")

    COMPANY_NAME = (
        By.XPATH,
        '//*[contains(@class, "Sidebar")]//span[contains(text(),"Кампания")]',
    )

    SEND_BUTTON = (
        By.XPATH,
        '//*[contains(@id, "modal")]//button//span[contains(text(),"Отправить")]',
    )

    CHOOSE_MEDIA = (By.XPATH, '//*[@data-testid="set-global-image"]')
    MEDIA_OPTIONS = (
        By.XPATH,
        '//div[contains(@class, "ItemList_content")]//div[contains(@class, "ImageItems_active") and not(contains(@class, "ImageItems_disabled"))]',
    )
    ADD_MEDIA = (
        By.XPATH,
        '//div[contains(@class, "MediaLibrary_container")]//div[contains(@class, "Footer")]//button//*[contains(text(),"Добавить")]',
    )

    LOGO_INPUT_FILE = (
        By.XPATH,
        '//*[contains(@class, "MediaLibrary")]//input[@type="file"]',
    )

    LOADING_IMG = (By.XPATH, '//*[contains(@class, "ImageItems_loading")]')
    CLOSE_MODAL = (By.XPATH, '//button[@aria-label="Close"]')

    MODAL_WIN = (
        By.XPATH, '//*[contains(@class, "vkuiModalCardBase__container")]')

    FILTER_BUTTON = (By.XPATH, '//*[@data-testid="filter-button"]')
