"""
test_login -

Author: Jeff Bian
Date:2022-08-27
"""

import allure
import pytest

from time import sleep
from support.ui.page_object.awsLoginPO import LoginPage
from support.ui.page_object.consoleHomePO import ConsoleHome
from support.ui.page_object.bucketsMainPO import BucketsMainPage
from support.ui.page_object.individualBucketPO import IndividualBucketPage
from support.ui.page_object.uploadPO import UploadPage
from support.ui.page_object.uploadStatusPO import UploadStatusPage


@allure.feature('Login a to AWS console and upload file (UI)')
class TestUploadFile:
    url = LoginPage.url

    @pytest.fixture(scope="function", autouse=True)
    def setup_class(self, driver):
        driver.get(self.url)
        self.loginpage = LoginPage(driver)
        self.consolehomepage = ConsoleHome(driver)
        self.bucketsmainpage = BucketsMainPage(driver)
        self.individualbucketpage = IndividualBucketPage(driver)
        self.uploadpage = UploadPage(driver)
        self.uploadstatuspage = UploadStatusPage(driver)

    @allure.title('Test Upload file to S3 Bucket success')
    def test_upload_file(self):
        # don't want to share my AWS account password, put a fake here
        self.loginpage.login_method('jeff.sbian@gmail.com', 'fake_password')
        self.consolehomepage.click_bucket()
        self.bucketsmainpage.individual_bucket()
        self.individualbucketpage.upload_click()
        self.uploadpage.upload_file()
        sleep(2)
        file_name = self.uploadstatuspage.check_uploaded_file_name()
        file_upload_status = self.uploadstatuspage.check_uploaded_file_status()

        assert file_name == 'demo-upload.txt' and file_upload_status == 'Succeeded'
