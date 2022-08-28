"""
jeffEADemoPO -

Author: Jeff Bian
Date:2022-08-27
"""
import allure

from support.ui.utils import BasePage

elementsMap = {
    'upload': '#upload-button'
}

class IndividualBucketPage(BasePage):

    def __init__(self, driver):
        BasePage.__init__(self, driver)

    def upload_click(self):
        with allure.step('Click upload file button'):
            self.click_element(elementsMap['upload'])