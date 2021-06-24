import unittest

from testdata.locators.sign_in_page_locator import SignInPageLocator
from pages.base_page import BasePage


class SignInPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def input_email_register(self, email1):
        self.send_key_by_css(SignInPageLocator.email_create, email1)

    def click_create_account(self):
        self.click_elt_by_css(SignInPageLocator.submit_create_btn)

    def check_display_error_msg(self):
        err_msg = self.get_text(SignInPageLocator.error_msg_locator)
        unittest.TestCase().assertEqual(SignInPageLocator.error_msg, err_msg, "Failed")