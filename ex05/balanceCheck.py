# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 19:17:14 2018

@author: Li Wende
"""

def isBalanced(input_string):
    if input_string=='':
        return True
    elif input_string[0] in ['(',')', ']', '[', '{', '}']:
        if input_string[-1] in ['(',')', ']', '[', '{', '}']:
            return input_string[0]==input_string[-1]
        else:
            return False
    else:
        return False
        