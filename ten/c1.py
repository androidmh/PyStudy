#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/7/10 14:26
# @Author : MengHe
# @File : c1.py
# @Software: PyCharm
import re

a = 'Python|Java|C#|C++|Kotlin|JavaScript'
r = re.findall('Java', a)
print(r)

# print(a.index('Python') > -1)
# print('Kotlin' in a)