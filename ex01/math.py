
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
            product*=element
        return product
    def mean(self):
        return (self.total()/self.size())
    def max_e(self):
        self.nodes.sort()
        return self.nodes[-1]
    def min_e(self):
        self.nodes.sort()
        return self.nodes[0]
    def print_all(self):
        print('Total count=', self.size())
        print('Sum=', self.total())
        print('Product=', self.product())
        print('Mean=', self.mean())
        print('Min=', self.min_e())
        print('Max=', self.max_e())
a=Stack_Math()
a.print_all()
        