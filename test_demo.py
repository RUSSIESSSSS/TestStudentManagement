#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/5/21 20:59
# @Author  : pauline
# @File    : test_demo.py
import pytest


def setup_module():
    print("准备资源：setup module")


def teardown_module():
    print("准备资源：teardown module")


def test_case_1():
    print("test1")


def test_case_2():
    print("test2")


def setup_function():
    print("资源准备：setup function")


def teardown_function():
    print("资源销毁：teardown function")


class TestDemo():
    def setup_class(self):
        print("类级别的 setup_class")

    def teardown_class(self):
        print("类级别的 teardown_class")

    def setup(self):
        print("这里是执行方法前 setup")

    @pytest.mark.parametrize
    def teardown(self):
        print("这里是执行方法后 teardown")

    def test_demo1(self):
        print("test demo1")

    def test_demo2(self):
        print("test demo2")

    def test_demo3(self):
        print("test demo3")
