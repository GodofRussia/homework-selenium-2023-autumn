import pytest
import time
from tests.base_case import BaseCase, credentials
from ui.pages.login_page import LoginPage

from selenium.common.exceptions import TimeoutException


class TestLogin(BaseCase):
    authorize = False

    # def test_login(self, credentials, login_page: LoginPage):
    #     login_page.login(credentials["user"], credentials["password"])

    #     try:
    #         self.driver.get_cookie("remixnsid")
    #     except Exception as e:
    #         assert False, f"self.driver.get_cookie raised {e}"

    # @pytest.mark.skip
    # @pytest.mark.parametrize("invalid_creds", [{"user": "stegozavr", "password": "a"}])
    # def test_login_neg(self, invalid_creds, login_page: LoginPage):
    #     with pytest.raises(TimeoutException):
    #         login_page.login(invalid_creds["user"], invalid_creds["password"])
