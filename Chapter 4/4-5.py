#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
计算 1~1 000 000 的总和：创建一个列表，其中包含数字 1~1000000
再使用min()和 max()核实该列表确实是从 1 开始，到 1000000 结束的。另外，对这个列表调用函数 sum()，看看 Python 将一百万个数字相加需要多长时间
'''

number = list(range(1, 1000001))

print(min(number))  # 列表最小数1
print(max(number))  # 列表最大数1000000

print(sum(number))  #500000500000