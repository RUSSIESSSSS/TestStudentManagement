#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/5/21 22:19
# @Author  : pauline
# @File    : conftest.py

def pytest_collection_modifyitems(items):
    """
    测试用例收集完成时，将收集到的用例名name和用例标识nodeid的中文信息显示在控制台上
    """
    for i in items:
        i.name = i.name.encode("utf-8").decode("unicode_escape")
        i._nodeid = i.nodeid.encode("utf-8").decode("unicode_escape")
