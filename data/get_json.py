#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author   : paulinelee
# @Time     : 2024/5/23 13:43
# @File     : get_json.py
# @Project  : pytest_00

import json


def get_json():
    with open('data_json.json', 'r') as file:
        data = json.dumps(file)
        # print(data, type(data))
        print(json.dumps(data))
    return data


if __name__ == '__main__':
    get_json()
