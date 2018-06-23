# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 18:18:13 2018

@author: Li Wende
"""
from stacks import Stacks
class Stack_Math(Stacks):
    def __init__(self):
        a=input('Enter the numbers:')
        a1=a.replace(',', '')
        a1.strip()
        a1.split()
        self.nodes=[int(n) for n in a1]
    def total(self):
        return sum(self.nodes)
    def product(self):
        product=1
        for element in self.nodes:
            product=product*element
        return product
    def mean(self):
        return (self.total()/self.size())
    def max_e(self):
        a=self.nodes.sort()
        return a.pop()
    def min_e(self):
        a=self.nodes.sort()
        return a[0]
    def print_all(self):
        print('Total count=', self.size())
        print('Sum=', self.total())
        print('Product=', self.product())
        print('Mean=', self.mean())
        print('Min=', self.min_e())
        print('Max=', self.max_e())
a=Stack_Math()
a.print_all()
        