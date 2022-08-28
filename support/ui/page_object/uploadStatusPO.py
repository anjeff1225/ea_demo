"""
uploadStatusPO -

Author: Jeff Bian
Date:2022-08-27
"""
import allure

from support.ui.utils import BasePage

elementsMap = {
    '1st_file': 'span[class="upload-summary-table__column-name"]',
    '1st_file_status': 'span[class="upload-summary-table__column-status"]'
}

class UploadStatusPage(BasePage):

    def __init__(self, driver):
        BasePage.__init__(self, driver)

    def check_uploaded_file_name(self):
        with allure.step('Check uploaded file name'):
            return self.get_text(elementsMap['1st_file'])

    def check_uploaded_file_status(self):
        with allure.step('Check uploaded file status'):
            return self.get_text(elementsMap['1st_file_status'])
