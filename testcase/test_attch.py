#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/6/2 16:25
# @Author  : pauline
# @File    : test_attch.py
import logging
import allure


class TestAttach:
    def test_pic(self):
        allure.attach.file(source='../../resourcess/WechatIMG55.jpg', attachment_type=allure.attachment_type.PNG,
                           extension="png")
