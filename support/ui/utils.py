"""
utlis - Basic web common functions

Author: Jeff Bian
Date:2022-08-27
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def go_to_url(self):
        self.driver.get(self.url)

    def refresh(self):
        self.driver.refresh()

    def wait_page_elem_up(self, time):
        self.driver.implicitly_wait(time)

    def wait_elem_find(self, value):
        return WebDriverWait(self.driver, 30, 1) \
            .until(lambda x: x.find_element(By.CSS_SELECTOR, value))

    def find_element(self, value):
        return self.driver.find_element(By.CSS_SELECTOR, value)

    def get_text(self, value):
        return self.find_element(value).text

    def switch_handle(self, num):
        self.driver.switch_to.window(self.driver.window_handles[num])

    def get_attribute(self, value, attr_name):
        return WebDriverWait(self.driver, 30) \
            .until(EC.visibility_of_element_located((By.CSS_SELECTOR, value))) \
            .get_attribute(attr_name)

    def input_text(self, value, txt):
        self.click_element(value)
        self.find_element(value).send_keys(txt)

    def click_element(self, value):
        self.find_element(value).click()

    def get_title(self):
        return self.driver.title

    def quit_driver(self):
        self.driver.quit()
