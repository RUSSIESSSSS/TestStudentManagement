#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author   : paulinelee
# @Time     : 2024/5/25 15:24
# @File     : test_fixture.py
# @Project  : pytest_00
import pytest


@pytest.fixture(params=['username', 'password'], autouse=True)  # """把参数放在fixture中，经过fixture的处理，再传入测试用例当中"""
def login(request):
    print(request.param)
    return request.param


def test_login_fixture():
    print("我是test_login_fixture函数的print")


if __name__ == '__main__':
    test_login_fixture()
