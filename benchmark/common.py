import os
import time

data_folder = 'data'


def current_milli_time():
    return int(round(time.time() * 1000))


def print_result(subject, start, purpose=None):
    p = ''
    if purpose is not None:
        p = ' for ' + purpose
    print(subject + ': ' + str(current_milli_time() - start) + 'ms' + p)


def create_folder(folder=None):
    path = data_folder
    if folder is not None:
        path += '/' + folder
    if not os.path.exists(path):
        os.makedirs(path)
