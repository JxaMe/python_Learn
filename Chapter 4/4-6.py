#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
奇数：通过给函数 range()指定第三个参数来创建一个列表，其中包含 1~20 的奇数；再使用一个 for 循环将这些数字都打印出来。
'''

number = list(range(1, 21, 2))  # 不能被2整除的数是奇数

for i in number:
    print(i)
