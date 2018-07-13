#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/7/11 11:51
# @Author : MengHe
# @File : c1.py
# @Software: PyCharm
from enum import Enum
from enum import IntEnum

'''
    枚举类
    优势:不可变，去重复标签
    IntEnum枚举的值只能是整型
'''


class VIP(Enum):
    YELLOW = 1
    GREEN = 2
    BLACK = 3
    RED = 4


print(VIP.YELLOW.name)
print(VIP(1))