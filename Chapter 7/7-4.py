#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
比萨配料：编写一个循环，提示用户输入一系列的比萨配料，并在用户输入
'quit'时结束循环。每当用户输入一种配料后，都打印一条消息，说我们会在比萨中添加这种配料。
'''

msg = ""
while msg!='quit':
    msg=input("请输入比萨配料:")
    if msg !="" and msg!='quit':
        print("我们会添加这种配料!")
    else:
        print("你什么都输入,或者退出")