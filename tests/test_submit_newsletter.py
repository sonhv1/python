from pages.base_page import BasePage
import unittest
from testdata.locators.home_page_locator import HomePageLocator
from pages.home_page import HomePage
from config.drivers import Drivers
from testdata.locators.constant import Constant
import time


class TestSubmitNewsLetter(unittest.TestCase, BasePage):
    def setUp(self):
        self.driver = Drivers.get_driver(Constant.CHROME)
        driver = self.driver
        driver.get(Constant.BASE_URL)
        self.driver.implicitly_wait(30)
        # self.driver.maximize_window()

    def test_submit_newsletter(self):
        driver = self.driver
        self.home_page = HomePage(self.driver)
        self.home_page.input_email(f"{self.generate_random_string(6)}{HomePageLocator.email_extension}")
        self.home_page.click_submit_email_button()
        self.home_page.check_display_success_msg()

    def tearDown(self):
        # close the browser window
        self.driver.close()


if __name__ == '__main__':
    unittest.TestCase()
