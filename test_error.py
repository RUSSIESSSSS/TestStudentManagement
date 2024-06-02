#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/5/22 22:00
# @Author  : pauline
# @File    : test_error.py


import pytest


def test_raise():
    with pytest.raises(ValueError):
        raise ValueError("值错误")


def test_raise1():
    with pytest.raises(ValueError) as exe:
        raise ValueError("value")
    assert exe.type is ValueError
    assert exe.value.args[0] == "value"
