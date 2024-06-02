#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/5/22 22:22
# @Author  : pauline
# @File    : test_add.py
import csv

import pytest
import yaml

from func.operation import my_add


def get_data():
    with open('../data/data.yaml', encoding='utf-8') as f:
        data = yaml.safe_load(f)
        return data


def test_get_data():
    print(get_data())


class TestWithYAML:
    @pytest.mark.parametrize('x,y,expected', get_data())
    # @pytest.mark.parametrize('x,y,expected', [[1, 1, 2], [200, 300, 500]])
    def test_add(self, x, y, expected):
        # assert my_add(int(x), int(y)) == int(expected)
        print(my_add(1, 2))


def get_csv():
    with open('../data/params.csv') as file:
        raw = csv.reader(file)
        data = []
        for line in raw:
            data.append(line)
    print(data)
    return data


class TestWithCSV:
    @pytest.mark.parametrize('x,y,expected', get_csv())
    def test_add(self, x, y, expected):
        assert my_add(int(x), int(y)) == int(expected)
        # print(my_add(1, 2))
