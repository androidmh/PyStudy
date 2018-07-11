#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/7/10 13:50
# @Author : MengHe
# @File : people.py
# @Software: PyCharm


class Human:
    sum = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        print(self.name)