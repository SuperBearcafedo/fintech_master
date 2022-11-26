# -*- coding: utf-8 -*-
import docx
import logging


class Logger:
    def __init__(self):
        self.logger = logging.getLogger("")
        self.logger.setLevel(logging.DEBUG)  # 设置级别
        console = logging.StreamHandler()  # 设置柄
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - [line:%(lineno)d] - %(message)s')  # 设置错打印格式
        console.setFormatter(formatter)
        self.logger.addHandler(console)

    def debug(self, msg):
        self.logger.debug(msg)

    def info(self, msg):
        self.logger.info(msg)

    def error(self, msg):
        self.logger.error(msg)
