#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
词汇表：Python 字典可用于模拟现实生活中的字典，但为避免混淆，我们将后者称为词汇表。
- 想出你在前面学过的 5 个编程词汇，将它们用作词汇表中的键，并将它们的含义作为值存储在词汇表中。以整洁的方式打印每个词汇及其含义。
为此，你可以先打印词汇，在它后面加上一个冒号，再打印词汇的含义；
也可在一行打印词汇，再使用换行符（\n） 插入一个空行，然后在下一行以缩进的方式打印词汇的含义
'''

vocabulary = {
    'Python': '正在学习的一种高级编程语言,人生苦短,我用Python',
    'while': '循环,让一段代码一遍又一遍不停的运行',
    'if': '条件判断语句',
    'for': '同样是一种循环',
    'list': 'Python中的列表数据结构'
}

print('Python:' + vocabulary['Python'])
print('while:' + vocabulary['while'])
print('for:' + vocabulary['for'])
print('list:' + vocabulary['list'])
print('if:' + vocabulary['if'])
