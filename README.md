# ea_demo

Demo for EDA

## Getting Started

check below instructions will give you a copy of the project up and running on your locla machine

###Prerequisties

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

