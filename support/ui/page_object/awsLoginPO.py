"""
awsLoginPO -

Author: Jeff Bian
Date:2022-08-27
"""
import os
import allure
import requests

from support.ui.utils import BasePage
from support.ui.utils_captcha import Captcha_recognize
from time import sleep

elementsMap = {
    'log_back_in_button': '#aws-page-content-main a[class="lb-btn-p-primary"] span',
    'email_address_input_field': '#resolving_input',
    'next_button': '#next_button',
    'captcha_image': '#captcha_image',
    'captcha_input_field': '#captcha_container > div > input',
    'captcha_submit_button': '#submit_captcha',
    'password_input_field': '#password',
    'signin_button': '#signin_button'
}


class LoginPage(BasePage):
    url = 'https://aws.amazon.com/console/'

    def __init__(self, driver):
        BasePage.__init__(self, driver)

    def login_method(self, email, pwd):
        """login steps"""
        self.go_to_url()
        self.wait_page_elem_up(30)
        with allure.step('Click Log back in button'):
            self.click_element(elementsMap['log_back_in_button'])
        with allure.step(f'Enter login email: {email}'):
            self.wait_elem_find(elementsMap['email_address_input_field'])
            self.input_text(elementsMap['email_address_input_field'], email)
            self.click_element(elementsMap['next_button'])
        with allure.step('Enter captcha'):
            '''
            AWS captcha is hard to recognize. I tried below two method:
            1. free OCR to (OCR space) https://ocr.space/ocrapi/
            2. tesseract
            Both method cannot recognize the AWS captcha, hence I used the 
            third party OCR which is NOT FREE. It still cannot recognize
            the captcha every time. 
            Comment out below and can show during the demo
            '''
            # src_url = self.get_attribute(elementsMap['captcha_image'], 'src')
            # img_r = requests.get(url=src_url)
            # with open(os.getcwd() + '/output/ui/captcha.png', 'wb') as f:
            #     f.write(img_r.content)
            # decode = Captcha_recognize('anjeff1225', 'woshishui', '938314')
            # img = open(os.getcwd() + '/output/ui/captcha.png', 'rb').read()
            # res = decode.PostPic(img, 1902)
            # captcha_text = res['pic_str']
            # print(captcha_text)

            self.input_text(elementsMap['captcha_input_field'], '12345')  # Put a temp fake captcha here
            sleep(2)
            self.click_element(elementsMap['captcha_submit_button'])
        with allure.step(f'Enter password: {pwd}'):
            self.wait_elem_find(elementsMap['password_input_field'])
            self.input_text(elementsMap['password_input_field'], pwd)
            self.click_element(elementsMap['signin_button'])
            sleep(2)
