#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
梦想的度假胜地：编写一个程序，调查用户梦想的度假胜地。
使用类似于“If you could visit one place in the world, where would you go?”的提示，并编写一个打印调查结果的代码块。
'''

info = {}
while True:
    name = input("请输入你的姓名:")
    msg = input("你最想去哪里度假:")

    info[name] = msg
    print(info)
    repeat = input("你还想继续调查吗?yes/no")

    if repeat == 'no':
        break

for name, msg in info.items():
    print('姓名:'+name+' '+'度假地:'+msg)
