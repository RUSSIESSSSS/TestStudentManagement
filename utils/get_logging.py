#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/6/2 16:41
# @Author  : pauline
# @File    : get_logging.py
import logging
import os.path
from logging.handlers import RotatingFileHandler

logger = logging.getLogger(__name__)  # 绑定句柄到logger对象

root_path = os.path.dirname(os.path.abspath(__file__))  # 获取当前工具文件所在路径

log_dir_path = os.sep.join([root_path, f'/logs'])  # 拼接日志输出路径
if not os.path.isdir(log_dir_path):
    os.mkdir(log_dir_path)

file_log_handler = RotatingFileHandler(os.sep.join([log_dir_path, 'log.log']), maxBytes=1024 * 1024, backupCount=10,
                                       encoding="utf-8")

date_string = '%Y-%M-%D %H-%M-%S'
formatter = logging.Formatter(
    '[%(asctime)s] [%(levelname)s] [%(filename)s]/[line: %(lineno)d]/[%(FuncName)s] %(message)s', date_string)
stream_handler = logging.StreamHandler()

file_log_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)

logger.addHandler(stream_handler)
logger.addHandler(file_log_handler)

logger.setLevel(level=logging.INFO)

