from selenium import webdriver
from testdata.locators.home_page_locator import HomePageLocator
from pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_login_btn(self):
        self.click_elt_by_css(HomePageLocator.sign_in_btn)
