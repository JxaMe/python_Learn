#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
10 的整数倍：让用户输入一个数字，并指出这个数字是否是 10 的整数倍。
'''

msg = input("请输入一个数字:")
msg = int(msg)

if msg % 10 == 0:
   print("这是10的整数倍")
else:
    print("这不是10的整数倍")