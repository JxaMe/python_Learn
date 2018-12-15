#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
调查：在 6.3.1 节编写的程序 favorite_languages.py 中执行以下操作。
- 创建一个应该会接受调查的人员名单，其中有些人已包含在字典中，而其他人未包含在字典中。
- 遍历这个人员名单，对于已参与调查的人，打印一条消息表示感谢。对于还未参与调查的人，打印一条消息邀请他参与调查。
'''

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edeard': 'ruby',
    'phii': 'python'
}

member = ['sarah', 'phii', 'jack', 'rose']

for i in member:
    if i in favorite_languages.keys():
        print("3Q参与调查")
    else:
        print("请配合参与调查!")
