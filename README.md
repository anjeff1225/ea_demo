# ea_demo

Demo for EDA

## Getting Started

check below instructions will give you a copy of the project up and running on your locla machine

### Prerequisties

* You need to install python 3+ version. https://www.python.org/downloads/

* Install request libiaries using below commands:
  ```
  pip install -r requirements.txt
  ```

## Running the test and generate report

* Simpliy execute the below command to execute the test and generate allure report
  ```
  pytest && allure generate ./allure_result -o ./allure_report --clean
  ```

* Sampler Report below
  ![Image text](https://github.com/anjeff1225/ea_demo/blob/162aad3b4ee2fe14e3111c331b7e67b49c0d7a66/sample_report_img/main_report.png)
  ![Image text](https://github.com/anjeff1225/ea_demo/blob/162aad3b4ee2fe14e3111c331b7e67b49c0d7a66/sample_report_img/failure_case.png)
  ![Image text](https://github.com/anjeff1225/ea_demo/blob/162aad3b4ee2fe14e3111c331b7e67b49c0d7a66/sample_report_img/success_case.png)
