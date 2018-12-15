#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
电影票：有家电影院根据观众的年龄收取不同的票价：不到 3 岁的观众免费；
3~12 岁的观众为 10 美元；超过 12 岁的观众为 15 美元。请编写一个循环，在其中询问用户的年龄，并指出其票价
'''
while True:
    msg = input("请输入你的年龄:")
    msg = int(msg)
    if msg < 3:
        print("免费")
    elif msg >= 3 and msg <= 12:
        print('收费10美元')
    elif msg > 12:
        print("收费15美元")
