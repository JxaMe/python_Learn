#!/usr/bin/env python
# -*- coding: utf-8 -*-

#在完成3-4至3-7的练习其中之一程序中,使用len()打印一条消息,指出你邀请了多少位嘉宾

Guest = ['bill', 'zuckerberg', 'jack马']
print('将邀请' + Guest[0].title() + ',' + Guest[1].title() + ',' + Guest[2].title() + ',' + '一起共进晚餐')
print('但是' + Guest[1].title() + ',' + '有事无法赴宴!')

Guest[1] = 'Pony马'
print('将重新邀请' + Guest[0].title() + ',' + Guest[1] + ',' + Guest[2].title() + ',' + '一起共进晚餐')
print('一共邀请了', len(Guest), '位嘉宾!')
