#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
添加嘉宾:你刚找到了一个更大的餐桌,可以容纳更多的嘉宾,请再邀请三位嘉宾.
- 以完成3-4,3-5的程序为基础,在程序末尾添加一条print语句,指出你找到了一个更大的餐桌
- 使用insert()将一位新嘉宾添加到名单开头.
- 使用insert()将另一位嘉宾添加到名单中间.
- 使用append()将最后一位新嘉宾添加到名单末尾
- 打印一系列消息,向名单中的嘉宾发出邀请
'''

Guest = ['bill', 'zuckerberg', 'jack马']
print('将邀请' + Guest[0].title() + ',' + Guest[1].title() + ',' + Guest[2].title() + ',' + '一起共进晚餐')
print('但是' + Guest[1].title() + ',' + '有事无法赴宴!')

Guest[1] = 'Pony马'
print('将重新邀请' + Guest[0].title() + ',' + Guest[1] + ',' + Guest[2].title() + ',' + '一起共进晚餐')

print("突然找到了一个更大的餐桌!")

Guest.insert(0,'王健林')
Guest.insert(2,'Trump')
Guest.append('David')

print('将重新邀请:' + Guest[0].title() + ',' + Guest[1] + ',' + Guest[2].title() + ',' + Guest[3]+ ',' + Guest[4] + ',' + Guest[5] +'一起共进晚餐!')