#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/7/10 9:52
# @Author : MengHe
# @File : c1.py
# @Software: PyCharm


class Student:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age


student = Student('DM', 26)
print(student._Student__name)