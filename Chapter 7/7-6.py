#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
三个出口：以另一种方式完成练习 7-4 或练习 7-5，在程序中采取如下所有做法。
- 在 while 循环中使用条件测试来结束循环。
- 使用变量 active 来控制循环结束的时机。
使用 break 语句在用户输入'quit'时退出循环
'''

'''
while True:
    msg = input("请输入你的年龄:")
    if msg == 'quit':
        break
    else:
        msg = int(msg)
        if msg < 3:
            print("免费")
        elif msg >= 3 and msg <= 12:
            print('收费10美元')
        else:
            print("收费15美元")
'''
'''
active = True
while active:
    msg = input("请输入你的年龄:")
    if msg == 'quit':
        active = False
    else:
        msg = int(msg)
        if msg < 3:
            print("免费")
        elif msg >= 3 and msg <= 12:
            print('收费10美元')
        else:
            print("收费15美元")
'''

msg = ''
while msg != 'quit':
    msg = input("请输入你的年龄:")
    msg = int(msg)
    if msg < 3:
        print("免费")
    elif msg >= 3 and msg <= 12:
        print('收费10美元')
    else:
        print("收费15美元")
