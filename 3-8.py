#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
放眼世界:想出是少5个你想去旅游的地方
- 将这些地方存储在列表中,确保不是按字母排序的
- 按照原始排列打印列表
- 使用sorted()按字母顺序打印列表,不要修改它
- 再次打印原列表,核实原列表顺序未变
- 使用sorted()按与字母相反的顺序打印列表,不要修改它
- 再次打印原列表
- 使用reverse()修改原列表的排序,打印该列表,核实顺序确实变了
- 使用reverse()修改原列表,打印核实顺序变回来了
- 使用sort()修改列表,按字母顺序排列
- 使用sort()修改列表,按字母顺序相反排列
'''

local = ['paris', 'eiffel tower', 'pyramid', 'tibet', 'munich']
print("原始列表:")
print(local)
print("临时字母排序:")
print(sorted(local))
print("原始列表:")
print(local)
print("临时字母相反排序:")
print(sorted(local,reverse=True))

local.reverse()
print("反转列表:")
print(local)
local.reverse()
print("再次反转")
print(local)
local.sort()
print("永久字母排序")
print(local)
local.sort(reverse=True)
print("永久字母反转:")
print(local)