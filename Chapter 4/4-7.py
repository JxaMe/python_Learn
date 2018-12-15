#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
3 的倍数：创建一个列表，其中包含 3~30 内能被 3 整除的数字；再使用一个 for循环将这个列表中的数字都打印出来
'''

number = list(range(3, 31, 3))
for i in number:
    print(i)
