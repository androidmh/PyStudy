#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/7/10 14:38
# @Author : MengHe
# @File : c2.py
# @Software: PyCharm
import re
'''
    获取数字正则
'''
# a = 'Python0Java2C#3C++5Kotlin9JavaScript'
# r = re.findall('\d', a)
# print(r)
'''
    获取字符集
'''
# s = 'abc, acc, adc, aec, afc, ahc'
# r = re.findall('a[^c-f]c', s)
# print(r)
'''
    概括字符集
    \d \D 数字非数字
    \w \W 单词字符[A-Za-z0-9]
    \s \S 空白字符 \n \t \r ' '
    . 匹配除了换行符\n之外所有字符
'''
# a = 'python1111java&67678php'
# r = re.findall('\W', a)
# print(r)
'''
    数量词
    贪婪与非贪婪
    默认情况下是贪婪的
    非贪婪加'?'
'''
# a = 'python 1111java678php'
# r = re.findall('[a-z]{3,6}', a)
# print(r)
'''
    数量词
    * 匹配多次或者0次
    + 批次一次或者多次
    ?匹配0次或者一次
'''
# a = 'pytho0python1pythonn2'
# r = re.findall('python?', a)
# print(r)

'''
    边界匹配
    ^开始位置$结尾位置
    匹配完整字符串
'''
# qq = '12344'
# r = re.findall('^\d{4,8}$', qq)
# print(r)

'''
    组
'''
# a = 'PythonPythonPythonPythonPython'
# r = re.findall('(Python){3}', a)
# print(r)

'''
匹配模式参数
第三个参数为模式
多个模式之间用|分隔
I忽略大小写
S计入换行符
'''
# a = 'PythonC#\nJavaPHP'
# r = re.findall('c#.{1}', a, re.I | re.S)
# print(r)

'''
    正则替换
    第一个参数 被替换的字符
    第二个参数 替换成新的字符(可以使用函数,很重要)
    第三个参数 需要操作字符串 
    第四个参数 替换几次字符 
    简单的字符串操作建议使用replace
'''

# a = 'PythonC#JavaC#PHPC#'
#
#
# def convert(value):
#     matched = value.group()
#     return '!!' + matched + '!!'
#
#
# r = re.sub('C#', convert, a)
# print(r)

'''
    把函数作为参数传递
'''
# a = 'A83C3721D86'
#
#
# def convert(value):
#     matched = int(value.group())
#     if matched >= 6:
#         return '9'
#     else:
#         return '0'
#
#
# r = re.sub('\d', convert, a)
# print(r)

'''
    match与search函数
    match从开始的地方匹配（如果开头不符合规则就不继续）
    search搜索所有字符串，一旦搜到结果立马返回
    两种都是只要搜到结果就立马结束
'''
# s = '83C72D1D8E67'
# r = re.match('\d', s)
# print(r)
# r1 = re.search('\d', s)
# print(r1)

'''
    group分组
'''
s = 'life is short, i use python, i love python'
r = re.search('life(.*)python(.*)python', s)
print(r.group(0, 1, 2))
print(r.groups())