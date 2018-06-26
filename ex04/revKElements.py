# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 19:09:18 2018

@author: Li Wende
"""
from Stacks import Stacks
def revKElements(input_string, k):
    a=Stacks()
    for i in range(k):
        a.push(input_string[i])
    final_string=input_string[k+1:-1]
    while a.pop():
        final_string+=a.pop()
    return final_string
revKElements(input('Enter the list of numbers:'), input('Enter k:'))
        