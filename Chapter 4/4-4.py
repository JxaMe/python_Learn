#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
一百万：创建一个列表，其中包含数字 1~1 000 000，
再使用一个 for 循环将这些数字打印出来（如果输出的时间太长，按 Ctrl + C 停止输出，或关闭输出窗口）。
'''

number = list(range(1, 1000001))

for i in number:
    print(i)
