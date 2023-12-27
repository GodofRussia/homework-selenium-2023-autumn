from selenium.webdriver.common.by import By
from ui.locators.basic import BasePageLocators


class AudienceLocators(BasePageLocators):
    CREATE_BUTTON = (By.XPATH, '//button[@data-testid="create-audience"]')
    CREATION_NAME_AUDITORY = (By.XPATH, '//*[@name="segmentName"]//input')

    ADD_SOURCE = (By.XPATH, '//*[contains(@class, "CreateSegmentModal")]//button')
    LEAD_REGION = (
        By.XPATH,
        '//*[contains(text(), "События в лид-форме")]',
    )

    LEAD_INPUT = (
        By.XPATH,
        '//label[contains(@class, "LeadFormEvents")]//span[contains(text(), "Выбрать")]',
    )
    LEAD_OPTIONS = (By.CLASS_NAME, "vkuiCustomSelectOption__description")

    LEAD_CHECKBOXES = (
        By.XPATH,
        '//*[contains(@class, "LeadFormEvents_contentWrapper")]//label',
    )

    LEAD_INPUT_DAYS = (
        By.XPATH,
        '//*[contains(@class, "LeadFormSources_itemFormWrapper")]//input[@type="text"]',
    )

    SAVE_BUTTON = (
        By.XPATH,
        '//*[contains(@class, "ModalSidebarPage_footer")]//button[@type="submit"]',
    )

    KEY_PHRASES_REGION = (
        By.XPATH,
        '//*[contains(text(), "Ключевые фразы")]',
    )

    KEY_DAYS_PERIOD = (
        By.XPATH,
        '//*[contains(@class, "Context_daysWrapper")]//input[@type="text"]',
    )

    USER_LIST = (By.XPATH, '//*[@data-testid="tabs-item"]')

    VK_GROUP_REGION = (
        By.XPATH,
        '//*[contains(text(), "Подписчики сообществ")]',
    )

    VK_GROUP_INPUT = (
        By.XPATH,
        '//*[contains(@class, "SearchInput_content")]//input[@type="text"]',
    )

    VK_GROUPS = (By.XPATH, '//*[contains(text(), "Сообщества ВКонтакте")]')

    VK_GROUPS_OPTIONS = (By.XPATH, '//*[contains(@class, "GroupContent_item")]')
    VK_GROUP_TEXT = (By.XPATH, '//*[contains(text(),"Подписчики сообществ")]')

    SOURCE_BUTTONS = (
        By.XPATH,
        '//*[contains(@class,"Header_buttons")]//*[name()="svg"]',
    )

    FILTER_BUTTON = (
        By.XPATH,
        '//*[contains(@class, "Hint_hintTrigger")]//button',
    )

    SUBSCRIBER_VK_GROUP = (By.XPATH, '//*[text()="Подписчики VK сообществ"]')
    APPLY_BUTTON = (
        By.XPATH,
        '//div[contains(@class, "Filter_buttons")]//button//*[contains(text(), "Применить")]',
    )

    DELETE_BUTTON = (By.XPATH, '//button//*[contains(text(), "Удалить")]')