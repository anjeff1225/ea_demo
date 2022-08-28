"""
s3BucketPO -

Author: Jeff Bian
Date:2022-08-27
"""
import allure

from support.ui.utils import BasePage

elementsMap = {
    'jeff_demo_bucket': 'a[class="bucket-name"]'
}

class BucketsMainPage(BasePage):

    def __init__(self, driver):
        BasePage.__init__(self, driver)

    def individual_bucket(self):
        with allure.step('Click individual bucket link'):
            self.click_element(elementsMap['jeff_demo_bucket'])