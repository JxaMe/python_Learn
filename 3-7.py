#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
缩减名单:你刚得知新购买的餐桌无法送达,因此只能邀请两位嘉宾.
- 完成3-6程序的基础下,在程序末尾添加一行代码,打印一条你只能邀请两位嘉宾的消息.
- 使用pop()不断删除名单中的嘉宾,直到只有两位嘉宾,每次从名单中弹出一位嘉宾时,都打印一条消息,表示很抱歉.
- 对余下的两位嘉宾中的每一位,都打印一条消息,指出他依然在受邀请人之列
- 使用del()将最后两位嘉宾从名单中删除,让名单变成空白,打印该名单,核实程序结束时,名单确实是空的
'''

Guest = ['bill', 'zuckerberg', 'jack马']
print('将邀请' + Guest[0].title() + ',' + Guest[1].title() + ',' + Guest[2].title() + ',' + '一起共进晚餐')
print('但是' + Guest[1].title() + ',' + '有事无法赴宴!')

Guest[1] = 'Pony马'
print('将重新邀请' + Guest[0].title() + ',' + Guest[1] + ',' + Guest[2].title() + ',' + '一起共进晚餐')

print("突然找到了一个更大的餐桌!")

Guest.insert(0, '王健林')
Guest.insert(2, 'Trump')
Guest.append('David')

print('将重新邀请:' + Guest[0].title() + ',' + Guest[1] + ',' + Guest[2].title() + ',' + Guest[3] + ',' + Guest[4] + ',' +
      Guest[5] + '一起共进晚餐!')

print('他喵的,吃饭桌没了,只能请两个人!')

pop = Guest.pop()
print('很抱歉,没地方坐了,' + pop + ',' + '你回家吧!')
pop = Guest.pop()
print('很抱歉,没地方坐了,' + pop + ',' + '你回家吧!')
pop = Guest.pop()
print('很抱歉,没地方坐了,' + pop + ',' + '你回家吧!')
pop = Guest.pop()
print('很抱歉,没地方坐了,' + pop + ',' + '你回家吧!')

print(Guest[0]+','+Guest[1]+','+'放心,你们依然有饭吃!')

'''
初学者,这里有个坑,删除了Guest[0]之后
第二次删除可能会写成Guest[1],程序会报错,因为del Guest[0]之后,列表中已经只剩1个数据了
他依然是Guest[0]
'''

del Guest[0]

del Guest[0]

print(Guest)


