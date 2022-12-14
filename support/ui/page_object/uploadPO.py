"""
uploadPO -

Author: Jeff Bian
Date:2022-08-27
"""
import os

import allure
import pywinauto
from pywinauto.keyboard import send_keys

from support.ui.utils import BasePage

elementsMap = {
    'add_files_button': 'awsui-button[class="upload-file-table__add-file-button"] > button',
    '1st_check_box': '#awsui-checkbox-13-label',
    'upload_button': 'awsui-button[class="upload-configuration__submit"] >button > span',
    '1st_file': 'span[class="upload-summary-table__column-name"]',
    '1st_file_status': 'span[class="upload-summary-table__column-status"]'
}


def upload_file_window_action(path):
    '''
    using pywinauto to control the win10 file upload window
    :param path:
    :return:
    '''
    app = pywinauto.Desktop()
    # My PC default language is Chinese, hence there is some chinese
    # character, which means app['open']
    dlg = app['打开']
    dlg["Toolbar3"].click()
    send_keys(path)
    send_keys('{VK_RETURN}')
    # below chinese means dlg['file name(N):]
    dlg["文件名(&N):Edit"].type_keys("demo-upload.txt")
    # below chinese means dlg['open']
    dlg["打开(&O)"].click()


class UploadPage(BasePage):
    url = 'https://s3.console.aws.amazon.com/s3/upload/jeff-ea-demo?region=us-west-1'

    def __init__(self, driver):
        BasePage.__init__(self, driver)

    def upload_file(self):
        with allure.step('Click add file button'):
            self.click_element(elementsMap['add_files_button'])
        with allure.step('select local file to upload'):
            upload_file_window_action(os.getcwd() + r'/input')
            self.click_element(elementsMap['1st_check_box'])
            self.click_element(elementsMap['upload_button'])

    def check_uploaded_file_name(self):
        with allure.step('Check uploaded file name'):
            return self.get_text(elementsMap['1st_file'])

    def check_uploaded_file_status(self):
        with allure.step('Check uploaded file status'):
            return self.get_text(elementsMap['1st_file_status'])
