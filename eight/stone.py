#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/7/9 14:50
# @Author : MengHe
# @File : stone.py
# @Software: PyCharm
diamond = 0.05  # 一颗钻石0.05金
vit = 1  # 一点体力1金
"""
    购买一级石头
"""
l1_value = 0.75  # 1颗一级石头消耗0.75金
l1_value_diamond = 8  # 1颗一级石头还需要消耗8颗钻石


'''
    1级合成3级
'''
l1_to_l3 = 12  # 1颗一级石头合成三级石头，需要额外消耗12颗一级石头
l1_to_13_gold = 0.39  # 同时还要消耗0.39金
l1_to_l3_vit = 10  # 同时还需消耗十点体力

"""
    3级合成4级
"""
l3_to_l4 = 16  # 1颗三级石头合成4级石头需要消耗16个一级石头
l3_to_l4_gold = 0.897  # 消耗0.897金
l3_to_l4_vit = 10  # 消耗10点体力
l3_to_l4_rate = 0.4878  # 合成成功率0.4878 失败扣除金币、16颗一级石头、但不消耗体力、不扣除三级石头

"""
    4级合6级
"""
l4_to_l6 = 12  # 消耗12颗4级石头
l4_to_l6_gold = 19.75  # 消耗19.75金
l4_to_l6_vit = 10  # 消耗10体力

