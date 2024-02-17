from random import randint

class Die:
    '''表示一个色子的类'''
    def __init__(self, num_sides=6):
        '''色子默认6面'''
        self.num_sides = num_sides

    def roll(self):
        '''返回一个1-6之间的随机数'''
        return randint(1, self.num_sides)
    
        