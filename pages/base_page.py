import random
import string
import csv
import xlrd
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


    def get_csv_data(file_name):
         # create an empty list to store rows
        rows = []
        # open the CSV file
        data_file = open(file_name, "r")
        # create a CSV Reader from CSV file
        reader = csv.reader(data_file)
        # skip the headers
        next(reader, None)
        # add rows from reader to list
        for row in reader:
         rows.append(row)
        return rows

    def get_xlsx_data(file_name):
        # create an empty list to store rows
        rows = []
        # open the CSV file
        book = xlrd.open_workbook(file_name)
        # get the frist sheet
        sheet = book.sheet_by_index(0)
        # iterate through the sheet and get data from rows in list
        for row_idx in range(1, sheet.nrows): #iterate 1 to maxrows
            rows.append(list(sheet.row_values(row_idx, 0, sheet.ncols)))
        return rows
