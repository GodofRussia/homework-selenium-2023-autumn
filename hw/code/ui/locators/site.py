from selenium.webdriver.common.by import By
from ui.locators.basic import BasePageLocators


class SiteLocators(BasePageLocators):
    ADD_PIXEL_BUTTON = (
        By.XPATH,
        '//*[contains(@id, "pixels")]//button//*[contains(text(),"Добавить пиксель")]',
    )

    INPUT_DOMEN = (
        By.XPATH,
        '//*[contains(@class, "ModalRoot")]//input[@type="text"]',
    )
    CLOSE_BUTTON = (
        By.XPATH,
        '//*[contains(@class, "ModalRoot")]//div[@aria-label="Закрыть"]',
    )

    ADD_BUTTON_MODAL = (By.XPATH, '//*[contains(@class, "ModalRoot")]//button')
    CREATE_NEW_PIXEL_REGION = (
        By.XPATH,
        '//*[contains(text(), "Создать новый пиксель")]',
    )

    SETTINGS = (By.XPATH, '//*[@data-route="pixels.code"]')
    CHECBOX_SETTINGS = (
        By.XPATH,
        '//*[contains(text(), "Сбор событий из слоя")]',
    )

    DATA_INPUT = (By.XPATH, '//*[@name="dataLayer"]//input')

    EMPTY_SPACE_DATA = (By.XPATH, '//*[contains(text(),"Код пикселя")]')

    EVENTS_REG = (By.ID, "tab_pixels.events")
    AUDIENCE_TAGS_REG = (By.ID, "tab_pixels.audience_tags")
    ACCESSABLE_REG = (By.ID, "tab_pixels.pixel_access")

    ADD_EVENT = (By.XPATH, '//*[contains(@class, "vkuiPanel__in")]//button')
    ADD_EVENT_MODAL = (
        By.XPATH,
        '//*[contains(@class, "footer")]//button//*[contains(text(),"Добавить событие")]',
    )

    SELECT_EVENT_NAME = (By.XPATH, '//*[contains(text(), "Выбирать вручную")]')
    INPUT_EVENT_NAME = (By.XPATH, '//input[@type="text"]')

    EVENT_SELECTOR = (
        By.XPATH,
        '//label[contains(@class, "vkuiCustomSelect")]',
    )
    CATEGORY_BUY_OPTION = (By.XPATH, '//*[contains(text(),"Покупка")]')
    CONDITION_OPTION = (By.XPATH, '//*[contains(text(),"Посещена страница")]')
    URL_INPUT = (By.XPATH, '//input[@type="text"]')

    ADD_TAG = (
        By.XPATH,
        '//button[@type="button"]//span[contains(text(),"Создать аудиторный тег")]',
    )

    INPUT_NAME_TAG = (
        By.XPATH,
        '//*[contains(@class, "Modal")]//input[@type="text"]',
    )
    CREATE_TAG_MODAL = (
        By.XPATH,
        '//*[contains(@class, "Modal")]//button//*[contains(text(),"Создать")]',
    )

    MORE_OPTIONS = (By.XPATH, '//div[@role="table"]//button')
    DELETE_OPTION = (By.XPATH, '//*[@data-testid="dropdown-item"]')

    MODAL_BUTTONS = (
        By.XPATH,
        '//*[contains(@class, "vkuiModalCardBase__actions")]//button',
    )

    PIXEL_ID = (By.XPATH, '//*[contains(text(),"Создан ID")]')

    SETTINGS_PAGE_ELEMENT = (By.XPATH, '//*[contains(text(), "Код пикселя")]')
