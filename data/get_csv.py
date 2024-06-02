#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/5/22 23:38
# @Author  : pauline
# @File    : get_csv.py
import csv


def get_csv():
    with open('params.csv') as file:
        raw = csv.reader(file)
        print(type(raw))
        for line in raw:
            print(line)


if __name__ == '__main__':
    get_csv()
