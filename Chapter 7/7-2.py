#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
餐馆订位：编写一个程序，询问用户有多少人用餐。如果超过 8 人，就打印一条消息，指出没有空桌；否则指出有空桌。
'''

msg = input("请问有多少人用餐?:")
msg = int(msg)
if msg > 8:
    print("人太多,没地坐!")
else:
    print("大爷里边请!")