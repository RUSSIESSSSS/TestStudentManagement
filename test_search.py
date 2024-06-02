#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/5/21 21:58
# @Author  : pauline
# @File    : test_search.py

import pytest

search_list = ['appium', 'selenium']


# 单个参数
@pytest.mark.parametrize('search_key', ['appium', 'abc', ' '])
def test_search(search_key):
    assert search_key in search_list


@pytest.mark.parametrize('username,password',
                         [['username1', 'password1'], ['username2', 'password2'], [' ', 'password'], ['', '']],
                         ids=['正确的用户名和密码', '其他正常用户', '用户名为空', '用户名密码为空'])
def test_login(username, password):
    print("username == ", username, "password == ", password)


@pytest.mark.parametrize('c', [7, 8, 9])
@pytest.mark.parametrize('b', [4, 5, 6])
@pytest.mark.parametrize('a', [1, 2, 3])
def test_variety_param(a, b, c):
    print("就是随便打印 a={a},b={b},c={c}")
