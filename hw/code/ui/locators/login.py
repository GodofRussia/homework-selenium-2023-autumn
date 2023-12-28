from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN = (By.NAME, "login")
    LOGIN_GO_ON_BOY_BUTTON = (By.XPATH, '//button[@type="submit"]')
    PASSWORD_GO_ON_BOY_BUTTON = (By.XPATH, '//button[@type="submit"]')
    PASSWORD = (By.NAME, "password")
