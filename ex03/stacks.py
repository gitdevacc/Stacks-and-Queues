# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 18:00:39 2018

@author: Li Wende
"""
class Stacks:
    def __init__(self): 
            self.nodes=[]
    def isEmpty(self):
        if self.size()==0:
            return True
        else:
            return False
    def push(self, data):
        self.nodes.append(data)
        return self.nodes
    def pop(self):
        if self.isEmpty!=True:
            return self.nodes.pop()
        else: 
            raise Exception("Cannot pop from an empty stack.")
    def peek(self):
        return self.nodes[-1]
    def size(self):
        return len(self.nodes)
    def __str__(self):
        return [str(element) for element in self]
    