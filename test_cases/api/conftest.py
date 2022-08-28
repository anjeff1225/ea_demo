"""
conftest.py -

Author: Jeff Bian
Date:2022-08-19
"""
import os

import pytest
import shutil


@pytest.fixture(scope="session", autouse=True)
def pre_setup():
    # delete log files if exist
    path = os.getcwd() + '/output/api'
    if not os.path.exists(path):
        os.mkdir(os.getcwd() + '/output/api')
    else:
        shutil.rmtree(path, ignore_errors=True)
        os.mkdir(os.getcwd() + '/output/api')
