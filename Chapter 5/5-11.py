#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
序数：序数表示位置，如 1st 和 2nd。大多数序数都以 th 结尾，只有 1、2 和 3例外。
- 在一个列表中存储数字 1~9。
- 遍历这个列表。
- 在循环中使用一个 if-elif-else 结构，以打印每个数字对应的序数。输出内容应为 1st、2nd、3rd、4th、5th、6th、7th、8th 和 9th，但每个序数都独占一行。
'''

number = list(range(1, 10))
for i in number:
    i = str(i)
    if i == '1':
        print(i + 'st')
    elif i == '2':
        print(i + 'nd')
    elif i == '3':
        print(i + 'rd')
    else:
        print(i + 'th')
