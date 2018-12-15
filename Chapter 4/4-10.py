#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
切片：选择你在本章编写的一个程序，在末尾添加几行代码，以完成如下任务。
- 打印消息“The first three items in the list are:”，再使用切片来打印列表的前三个元素。
- 打印消息“Three items from the middle of the list are:”，再使用切片来打印列表中间的三个元素。
- 打印消息“The last three items in the list are:”，再使用切片来打印列表末尾的三个元素。
'''
str1 = 'The first three items in the list are:'
print(str1)
print(str1[:3])
str2 = 'Three items from the middle of the list are:'
print(str2)
s = len(str2) // 2
print(str2[s:s + 3])
str3 = 'The last three items in the list are:'
print(str3)
print(str3[-3:])
