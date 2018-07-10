#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/7/9 15:21
# @Author : MengHe
# @File : compose.py
# @Software: PyCharm
from eight.stone import *
import random


def get1_stone():
    stone1_gold = l1_value + l1_value_diamond * diamond
    return stone1_gold


def get3_stone():
    stone1_gold = get1_stone()
    stone3_gold = stone1_gold * 13 + l1_to_13_gold + l1_to_l3_vit * vit
    return stone3_gold


def get4_stone():
    global fail_sum
    fail_sum = 0
    stone3_gold = get3_stone()
    is_success = True
    stone4_gold = 0
    while is_success:
        random_num = random.randint(0, 10000)
        if random_num <= 4878:
            is_success = False
            stone4_gold += stone3_gold + get1_stone() * l3_to_l4 + l3_to_l4_gold + l3_to_l4_vit * vit
        else:
            is_success = True
            fail_sum += 1
            stone4_gold += get1_stone() * l3_to_l4 + l3_to_l4_gold
    return stone4_gold, fail_sum


def get6_stone():
    stone4_gold = 0
    fail_sums = 0
    for i in range(0, 11):
        a, b = get4_stone()
        stone4_gold += a
        fail_sums += b
    print('合成4级石头一共失败了'+str(fail_sums)+'次')
    return stone4_gold + l4_to_l6_gold + l4_to_l6_vit * vit


gold_sum = get6_stone()
print(gold_sum)
