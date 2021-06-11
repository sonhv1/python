import chromedriver_autoinstaller
from selenium import webdriver

from testdata.locators.constant import Constant


class Drivers:
    @staticmethod
    def get_driver(browser):
        if browser == Constant.CHROME:
            chromedriver_autoinstaller.install()
            driver = webdriver.Chrome()
        return driver
