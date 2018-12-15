#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
5-9处理没有用户的情形：在为完成练习 5-8 编写的程序中，添加一条 if 语句，检查用户名列表是否为空。
- 如果为空，就打印消息“We need to find some users!”。
  删除列表中的所有用户名，确定将打印正确的消息。
'''

users = ['loster', 'pter', 'skys', 'andis', 'admin']
# users = []
if users:
    for user in users:
        if user == 'admin':
            print('Hello ' + user + ', would you like to see a status report?')
        else:
            print('Hello ' + user + ', thank you for logging in again')
else:
    print('We need to find some users!')
