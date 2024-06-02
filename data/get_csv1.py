#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author   : paulinelee
# @Time     : 2024/5/23 09:45
# @File     : get_csv1.py
# @Project  : pytest_00


import csv


def get_csv():
    with open('params.csv') as file:
        raw = csv.reader(file)
        data = []
        for line in raw:
            data.append(line)
    print("这是data里存的数据", data)
    return data


if __name__ == '__main__':
    get_csv()
