#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
熟食店：创建一个名为 sandwich_orders 的列表，在其中包含各种三明治的名字；
再创建一个名为 finished_sandwiches 的空列表。
遍历列表 sandwich_orders，对于其中的每种三明治，都打印一条消息，如 I made your tuna sandwich
并将其移到列表finished_sandwiches。
所有三明治都制作好后，打印一条消息，将这些三明治列出来
'''

sandwich_orders = ['onesandwich', 'twosandwich', 'threesandwich']

finished_sandwiches = []
for sandwich in sandwich_orders:
    print('I made your ' + sandwich)
while sandwich_orders:
    temp = sandwich_orders.pop()
    finished_sandwiches.append(temp)

print(finished_sandwiches)
