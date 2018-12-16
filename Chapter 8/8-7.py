#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
8-7专辑：编写一个名为 make_album()的函数，它创建一个描述音乐专辑的字典。这个函数应接受歌手的名字和专辑名，并返回一个包含这两项信息的字典。

给函数 make_album()添加一个可选形参，以便能够存储专辑包含的歌曲数。
如果调用这个函数时指定了歌曲数，就将这个值添加到表示专辑的字典中。调用这个函数，并至少在一次调用中指定专辑包含的歌曲数
'''


def make_album(name, album_name, quantity=''):
    if quantity:
        album = {'name': name, 'album_name': album_name, 'quantity': quantity}
        return album
    else:
        album = {'name': name, 'album_name': album_name}
        return album


a = make_album('jay', '七里香',12)
b = make_album('张学友', '吻别')
c = make_album('迈克尔·杰克逊', '颤栗')
print(a, b, c)
