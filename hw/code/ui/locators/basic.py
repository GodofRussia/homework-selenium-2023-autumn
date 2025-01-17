from selenium.webdriver.common.by import By


class BasePageLocators:
    COOKIE_BANNER_BUTTON = (
        By.XPATH,
        "//button[contains(@class, 'CookieBanner_button__')]",
    )
    BANNER_BUTTON = (By.CLASS_NAME, "vkuiIcon--cancel_20")
    ELEMENT_WITH_TEXT = lambda self, element, text: (
        By.XPATH,
        f'//{element}[text()="{text}"]',
    )
    ELEMENT_WITH_TEXT_AND_CLASS = lambda self, element, text, class_name: (
        By.XPATH,
        f'//{element}[text()="{text}" and contains(@class, "{class_name}")]',
    )
    ELEMENT_WITH_CLASS = lambda self, element, class_name: (
        By.XPATH,
        f'//{element}[contains(@class, "{class_name}")]',
    )
    INPUT_WITH_PLACEHOLDER = lambda self, placeholder: (
        By.XPATH,
        f'//input[@placeholder="{placeholder}"]',
    )
    LINK_WITH_HREF = lambda self, href: (
        By.XPATH,
        f"//a[contains(@href, '{href}')]",
    )
    VALIDATION_FAILED_NOTIFICATION = (By.ID, "Validation failed")

    CONTAINS_ANY_TEXT = lambda self, text: (
        By.XPATH,
        f"//*[contains(text(), '{text}')]",
    )
