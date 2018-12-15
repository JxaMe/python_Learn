#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
自助餐：有一家自助式餐馆，只提供五种简单的食品。请想出五种简单的食品，并将其存储在一个元组中。
- 使用一个 for 循环将该餐馆提供的五种食品都打印出来。
- 尝试修改其中的一个元素，核实 Python 确实会拒绝你这样做。
- 餐馆调整了菜单，替换了它提供的其中两种食品。请编写一个这样的代码块： 给元组变量赋值，并使用一个 for 循环将新元组的每个元素都打印出来。
'''

foods = ('Potatoes', 'tomatoes', 'corn', 'braised pork', 'hamburger')

for food in foods:
    print(food)

# foods[0] = 'rice'

foods = ('Potatoes', 'tomatoes', 'corn', 'Beef', 'french fries')

for food in foods:
    print(food)
