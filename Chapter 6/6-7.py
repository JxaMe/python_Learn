#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
人：在为完成练习 6-1 而编写的程序中，再创建两个表示人的字典，然后将这三个字典都存储在一个名为 people 的列表中。
遍历这个列表，将其中每个人的所有信息都打印出来
'''

jax = {
    'first_name': 'jack',
    'last_name': 'solo fuck',
    'age': 18,
    'city': 'Magic capital'
}

tom = {
    'first_name': 'tom',
    'last_name': 'krosi',
    'age': 23,
    'city': 'Chengdu'
}

lili = {
    'first_name': 'lili',
    'last_name': 'andm',
    'age': 26,
    'city': 'Imperial capital'
}

peoples = [jax, tom, lili]

for people in peoples:
    print(people['first_name'].title()+' '+people['last_name']+','+'的年龄是:'
          +str(people['age'])+','+'住在:'+people['city'])
