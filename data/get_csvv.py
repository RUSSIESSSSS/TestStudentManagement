#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/5/23 19:19
# @Author  : pauline
# @File    : get_csvv.py
import csv
import json


def get_csv():
    with open('params.csv') as f:
        raw = csv.reader(f)
        data = []
        for line in raw:
            data.append(line)
    return data


def get_json():
    with open('123.json', 'r') as f:
        # print(type(f.read()))
        data = json.loads(f.read())
        print(type(data))


if __name__ == '__main__':
    # get_csv()
    get_json()
