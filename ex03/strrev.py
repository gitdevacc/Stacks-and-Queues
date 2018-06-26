# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 19:02:32 2018

@author: Li Wende
"""
from Stacks import Stacks
def strrev(input_string):
    a=Stacks()
    for c in input_string:
        a.push(c)
    final_string=''
    while a.pop():
        final_string+=a.pop()
    return final_string
strrev(input('What string would you like to be reversed?'))
    
    