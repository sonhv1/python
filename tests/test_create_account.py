import unittest

from ddt import data
import pytest
from pages.home_page import HomePage
from pages.sign_in_page import SignInPage
from testdata.locators.constant import Constant
from testdata.library.get_create_account_data import get_csv_data
from config.drivers import Drivers
from pages.base_page import BasePage
from utils import XLUtils
from selenium import webdriver


class TestCreateAccount(unittest.TestCase, BasePage):
    def setUp(self):
        self.driver = webdriver.Chrome("C:/Users/SonHV3/PycharmProjects/pythonProject3/chromedriver.exe")
        # self.driver = Drivers.get_driver(Constant.CHROME)
        self.driver.implicitly_wait(30)
        # self.driver.maximize_window()

    @data(*get_csv_data('create_account.csv'))
    def test_create_account(self, obj):
        driver = self.driver
        driver.get(Constant.BASE_URL)
        self.hp = HomePage(self.driver)
        self.hp.click_login_btn()
        # self.screen_shot(Constant.SCREENSHOT_PATH, "123.png")
        # self.driver.save_screenshot("../screenshots/abc.png")
        signInPage = SignInPage(driver)
        signInPage.input_email_register(obj.email)

    def tearDown(self):
        # close the browser window
        self.driver.close()


if __name__ == '__main__':
    unittest.TestCase()
