#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
立方：将同一个数字乘三次称为立方。例如，在 Python 中，2 的立方用 2**3 表示。
请创建一个列表，其中包含前 10 个整数（即 1~10）的立方，再使用一个 for 循环将这些立方数都打印出来
'''

number = list(range(1, 11))
for i in number:
    i = i**3
    print(i)