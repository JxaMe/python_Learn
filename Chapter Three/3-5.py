#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
修改嘉宾名单:你刚得知有位嘉宾无法赴宴,因此需要另外邀请以为嘉宾.
- 以完成练习3-4的程序为基础,在末尾添加一条print语句,指出哪位嘉宾无法赴宴.
- 修改嘉宾名单,将无法赴宴的嘉宾的姓名替换为新邀请的嘉宾的名字
- 再次打印一条消息,向名单中的每位嘉宾发起邀请
'''

Guest = ['bill', 'zuckerberg', 'jack马']
print('将邀请' + Guest[0].title() + ',' + Guest[1].title() + ',' + Guest[2].title() + ',' + '一起共进晚餐')
print('但是' + Guest[1].title() + ',' + '有事无法赴宴!')

Guest[1] = 'Pony马'
print('将重新邀请' + Guest[0].title() + ',' + Guest[1] + ',' + Guest[2].title() + ',' + '一起共进晚餐')
