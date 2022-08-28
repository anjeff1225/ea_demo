"""
response_util -

Author: Jeff Bian
Date:2022-08-28
"""
import os

import allure
import pandas as pd
from pathlib import Path
import glob

path = os.getcwd() + '/output/api/'


def response_write_to_xlsx(response, filename):
    df = pd.DataFrame.from_dict(response)
    df['timestamp'] = pd.to_datetime('now').strftime("%Y-%m-%d %H:%M:%S")
    df.set_index('timestamp', inplace=True)
    df.to_excel(path + filename + '.xlsx')


def merge_xlsx(filename):
    file_list = glob.glob(path + f'{filename}*.xlsx')
    excl_list = []
    for file in file_list:
        excl_list.append(pd.read_excel(file))

    excl_merged = pd.DataFrame()
    for excl_file in excl_list:
        # appends the data into the excl_merged
        # dataframe.
        excl_merged = excl_merged.append(excl_file, ignore_index=True)

    # exports the dataframe into excel file with
    # specified name.
    excl_merged.to_excel(path + f'final-{filename}.xlsx', index=False)

def attach_log_file(filename):
    allure.attach.file(path + filename, name=filename, extension='xlsx')