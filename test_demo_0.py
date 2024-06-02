#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/5/21 22:42
# @Author  : pauline
# @File    : test_demo_0.py
import sys

import pytest


@pytest.mark.int
def test_int1():
    print("int = ", 1)


@pytest.mark.skip
@pytest.mark.int
def test_int2():
    print("int = ", 2)


@pytest.mark.skipif(sys.platform == 'darwin', reason='does not run on mac')
@pytest.mark.int
def test_int3():
    print("int = ", 3)


@pytest.mark.xfail
@pytest.mark.float
def test_float():
    assert 1 == 2


@pytest.mark.str
def test_str():
    print("str = ", 'sttttt')
