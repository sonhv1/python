import random
import string
from datetime import datetime
from selenium.common import exceptions


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    def refresh_page(self):
        self.driver.refresh()

    @staticmethod
    def get_current_time():
        now = datetime.now()
        current_time = now.strftime("%H_%M_%S")
        return current_time

    def click_elt_by_css(self, css_selector):
        return self.driver.find_element_by_css_selector(css_selector).click()

    def find_element_by_xpath(self, locator_xpath):
        return self.driver.find_element_by_xpath(locator_xpath)

    def screen_shot(self, path, file_name):
        self.driver.save_screenshot(f"{path}{file_name}")
        print(f"{path}{file_name}")

    def get_text(self, locator):
        return self.driver.find_element_by_css_selector(locator).text

    @staticmethod
    def clear_text(element):
        element.clear()

    def is_element_present_by_css(self, css_selector):
        try:
            self.find_elt_by_css(css_selector)
            # print("is_element_present_by_css + css_selector)
            return True
        except exceptions.NoSuchElementException as ex:
            # print("NoSuchElementException: " + str(ex))
            return False

    def send_key_by_css(self, css_selector, text):
        return self.driver.find_element_by_css_selector(css_selector).send_keys(text)

    @staticmethod
    def generate_random_string(length):
        # choose from all lowercase letter
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(length))
