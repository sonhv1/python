import unittest
import time
from pages.home_page import HomePage
from pages.sign_in_page import SignInPage
from testdata.locators.constant import Constant
from testdata.library.get_create_account_data import get_csv_data
from config.drivers import Drivers
from pages.base_page import BasePage
from testdata.locators.sign_in_page_locator import SignInPageLocator
from utils import XLUtils
from selenium import webdriver


class TestCreateAccount(unittest.TestCase, BasePage):
    def setUp(self):
        self.driver = Drivers.get_driver(Constant.CHROME)
        driver = self.driver
        driver.get(Constant.BASE_URL)
        self.driver.implicitly_wait(30)
        # self.driver.maximize_window()

    # @data(*get_csv_data('create_account.csv'))
    def test_create_account_invalid(self):
        driver = self.driver
        self.home_page = HomePage(self.driver)
        self.home_page.click_login_btn()
        # self.screen_shot(Constant.SCREENSHOT_PATH, "123.png")
        # self.driver.save_screenshot("../screenshots/abc.png")
        signInPage = SignInPage(driver)
        signInPage.input_email_register('abc123')
        signInPage.click_create_account()
        time.sleep(5)
        signInPage.check_display_error_msg()

    def test_create_account_success(self):
        driver = self.driver
        self.home_page = HomePage(self.driver)
        self.home_page.click_login_btn()
        signInPage = SignInPage(driver)
        signInPage.input_email_register(
            f"{self.generate_random_string(5)}{SignInPageLocator.email_extension}")
        time.sleep(3)
        signInPage.click_create_account()

    def tearDown(self):
        # close the browser window
        self.driver.close()


if __name__ == '__main__':
    unittest.TestCase()
