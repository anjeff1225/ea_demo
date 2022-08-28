"""
yaml_util.py -

Author: Jeff Bian
Date:2022-08-28
"""
import yaml
import os

yaml_file = os.getcwd() + '/support/api/extract.yml'


# read yaml
def read_yaml(key):
    with open(yaml_file, encoding='utf-8') as file:
        value = yaml.load(stream=file, Loader=yaml.FullLoader)
        return value[key]


# write yaml
def write_yaml(data):
    with open(yaml_file, encoding='utf-8', mode='a') as file:
        yaml.dump(data, stream=file, allow_unicode=True)


# clear yaml
def clear_yaml():
    with open(yaml_file, encoding='utf-8', mode='w') as file:
        file.truncate()


# read test_case yaml
def read_testcase_yaml(yaml_name):
    with open(os.getcwd() + '/test_cases/api/' + yaml_name, encoding='utf-8') as file:
        value = yaml.load(stream=file, Loader=yaml.FullLoader)
        return value
