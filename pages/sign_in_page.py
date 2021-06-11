from testdata.locators.sign_in_page_locator import SignInPageLocator
from pages.base_page import BasePage

class SignInPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def input_email_register(self, email):
        self.send_key_by_css(SignInPageLocator.email_create, email)