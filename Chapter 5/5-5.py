#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
外星人颜色#3：将练习 5-4 中的 if-else 结构改为 if-elif-else 结构。
- 如果外星人是绿色的，就打印一条消息，指出玩家获得了 5 个点。
- 如果外星人是黄色的，就打印一条消息，指出玩家获得了 10 个点。
- 如果外星人是红色的，就打印一条消息，指出玩家获得了 15 个点。
- 编写这个程序的三个版本，它们分别在外星人为绿色、黄色和红色时打印一条消息。
'''

alien_color = 'red'

if alien_color == 'green':
    print('获得5点积分')
elif alien_color == 'yellow':
    print('获得10点积分')
else:
    print('获得15点积分')
#################################################
alien_color = 'yellow'

if alien_color == 'green':
    print('获得5点积分')
elif alien_color == 'yellow':
    print('获得10点积分')
else:
    print('获得15点积分')
#################################################
alien_color = 'green'

if alien_color == 'green':
    print('获得5点积分')
elif alien_color == 'yellow':
    print('获得10点积分')
else:
    print('获得15点积分')