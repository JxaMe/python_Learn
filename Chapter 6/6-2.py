#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
喜欢的数字：使用一个字典来存储一些人喜欢的数字。请想出 5 个人的名字，
并将这些名字用作字典中的键；想出每个人喜欢的一个数字，并将这些数字作为值存储在字典中。
打印每个人的名字和喜欢的数字。为让这个程序更有趣，通过询问朋友确保数据是真实的喜欢的数字：
'''

favorite_number = {
    'jack': 7,
    'tom': 8,
    'lili': 1,
    'loli': 3,
    'seya': 5
}

for k,v in favorite_number.items():
    print(k,v)