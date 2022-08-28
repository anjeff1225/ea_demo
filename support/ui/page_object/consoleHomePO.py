"""
consoleHomePO.py -

Author: Jeff Bian
Date:2022-08-27
"""
import allure

from support.ui.utils import BasePage

elementsMap = {
    's3_bucket': 'a[data-analytics="serviceLink_s3"]'
}

class ConsoleHome(BasePage):

    def __init__(self, driver):
        BasePage.__init__(self, driver)

    def click_bucket(self):
        with allure.step('Click S3 Bucket'):
            self.click_element(elementsMap['s3_bucket'])