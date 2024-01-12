from selenium.webdriver.common.by import By
from ui.locators.basic import BasePageLocators


class LeadPageLocators(BasePageLocators):
    CREATE_BUTTON = (By.XPATH, '//*[contains(text(), "Создать лид-форму")]')
    UPLOAD_LOGO = (By.XPATH, '//*[@data-testid="set-global-image"]')
    INPUTS = (By.XPATH, '//input[@type="text"]')
    CONTINUE_BUTTON = (By.XPATH, '//*[contains(text(), "Продолжить")]')
    SAVE_BUTTON = (By.XPATH, '//*[contains(text(), "Сохранить")]')
    MEDIA_OPTIONS = (
        By.XPATH,
        '//div[contains(@class, "ItemList_content")]//div[contains(@class, "ImageItems_active") and not(contains(@class, "ImageItems_disabled"))]',
    )

    CONTACT_INFO = (By.XPATH, '//*[contains(text(), "Контактная информация")]')
    ADD_SITE = (By.XPATH, '//*[contains(text(), "Добавить сайт")]')

    MODAL = (By.XPATH, '//*[contains(@class, "ModalRoot")]')