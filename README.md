# ea_demo

Demo for EDA

## Getting Started

check the below instructions will give you a copy of the project up and running on your local machine

### Prerequisties

* You need to install the python 3+ version. https://www.python.org/downloads/

* Install request libraries using the below commands:
  ```
  pip install -r requirements.txt
  ```
* Install webdriver

  - **Windows**: download the webdriver from below links, make sure the version you select matches the brwose version your host has
    
    _Chrome Webdriver: https://chromedriver.chromium.org/downloads_
    
    _Firefox Webdriver: https://github.com/mozilla/geckodriver/releases_

    After download the zip file, unzip them and put the *.exe file in the same path as your python3 binary

  - Linux: https://tecadmin.net/setup-selenium-chromedriver-on-ubuntu/

* Install allure

  1. Download allure with the latest version. https://github.com/allure-framework/allure2/releases/tag/2.19.0
  2. Unpack the archive to the allure-commandline directory
  3. Add allure to system PATH

## Running the test and generating a report

* Simply execute the below command to execute the test and generate an allure report
  ```
  pytest && allure generate ./allure_result -o ./allure_report --clean
  ```

* Sampler Report below
  ![Image text](https://github.com/anjeff1225/ea_demo/blob/162aad3b4ee2fe14e3111c331b7e67b49c0d7a66/sample_report_img/main_report.png)
  ![Image text](https://github.com/anjeff1225/ea_demo/blob/162aad3b4ee2fe14e3111c331b7e67b49c0d7a66/sample_report_img/failure_case.png)
  ![Image text](https://github.com/anjeff1225/ea_demo/blob/162aad3b4ee2fe14e3111c331b7e67b49c0d7a66/sample_report_img/success_case.png)
