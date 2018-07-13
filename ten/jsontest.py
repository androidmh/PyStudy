#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/7/11 11:08
# @Author : MengHe
# @File : jsontest.py
# @Software: PyCharm
import json
'''
    反序列化json字符串
'''
# json_str = '[{"name":"qiyue", "age":18}, {"name":"aa", "age":12}]'
# student = json.loads(json_str)
# print(student[1]['name'])

'''
    序列化json对象
'''
student = [
    {'name': 'aa', 'age': 18, 'flag': False},
    {'name': 'bb', 'age': 17}
]
json_str = json.dumps(student)
print(json_str)