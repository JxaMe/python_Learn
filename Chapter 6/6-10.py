#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
喜欢的数字：修改为完成练习 6-2 而编写的程序，让每个人都可以有多个喜欢的数字，然后将每个人的名字及其喜欢的数字打印出来。
'''

favorite_number = {
    'jack': [2, 3, 7],
    'tom': [1, 2, 3, 4],
    'lili': [4, 7, 9],
    'loli': [0, 23, 56, 66],
    'seya': [88, 99, 101]
}

for name, numbers in favorite_number.items():
    print(name.title() + ',' + '最喜欢的数字是:')
    for number in numbers:
        print(number)

