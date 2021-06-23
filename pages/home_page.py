from testdata.locators.home_page_locator import HomePageLocator
from pages.base_page import BasePage
import unittest

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_login_btn(self):
        self.click_elt_by_css(HomePageLocator.sign_in_btn)

    def input_email(self, email):
        self.send_key_by_css(HomePageLocator.newsletter_input, email)

    def click_submit_email_button(self):
        self.click_elt_by_css(HomePageLocator.submit_email_btn)

    def check_display_success_msg(self):
        success_msg = self.get_text(HomePageLocator.success_msg_locator)
        unittest.TestCase().assertEqual(HomePageLocator.success_msg, success_msg)