#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/7/9 11:43
# @Author : MengHe
# @File : c3.py
# @Software: PyCharm


def demo(*a):
    print(*a)


demo(1, 2, 3)


def demo2():
    global c
    c = 2


demo2()
print(c)