#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/5/23 19:50
# @Author  : pauline
# @File    : test_dd.py
import pytest


@pytest.fixture()
def login():
    a = '123'
    print("login")
    yield 123
    print("dengchu ")


def test_1(login):
    print("hhhh")


if __name__ == '__main__':
    test_1()
