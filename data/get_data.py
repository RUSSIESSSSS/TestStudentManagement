#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/5/29 22:24
# @Author  : pauline
# @File    : get_data.py
import yaml


def get_yaml_data(file_path, name, level):
    with open(file_path, encoding='utf-8') as f:
        yaml_data = yaml.safe_load(f)
        data = yaml_data.get(name).get(level).get('data')
        return data

# def get_modify_data():
#     with open('modify_stu.yaml.yaml', encoding='utf-8') as f:
#         data = yaml.safe_load(f)
#         return data
