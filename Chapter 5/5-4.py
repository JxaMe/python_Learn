#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
外星人颜色#2：像练习 5-3 那样设置外星人的颜色，并编写一个 if-else 结构。
- 如果外星人是绿色的，就打印一条消息，指出玩家因射杀该外星人获得了 5 个点。
- 如果外星人不是绿色的，就打印一条消息，指出玩家获得了 10 个点。
编写这个程序的两个版本，在一个版本中执行 if 代码块，而在另一个版本中执行 else 代码块。
'''

alien_color = 'red'

if alien_color == 'green':
    print('获得5点积分')
else:
    print('获得10点积分')
