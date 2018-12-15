#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
2：既然你知道了如何遍历字典，现在请整理你为完成练习 6-3 而编写的代码
将其中的一系列 print 语句替换为一个遍历字典中的键和值的循环。确定该循环正确无误后，再在词汇表中添加 5 个 Python 术语。
当你再次运行这个程序时，这些新术语及其含义将自动包含在输出中
'''

vocabulary = {
    'Python': '正在学习的一种高级编程语言,人生苦短,我用Python',
    'while': '循环,让一段代码一遍又一遍不停的运行',
    'if': '条件判断语句',
    'for': '同样是一种循环',
    'list': 'Python中的列表数据结构',
    'range': '生成数字列表'
}

for k, v in vocabulary.items():
    print(k, v)
