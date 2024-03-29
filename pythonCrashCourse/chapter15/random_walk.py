from random import choice

class RandomWalk:
    '''一个生成随机漫步数据的类'''

    def __init__(self, num_points=50000):
        '''初始化随机漫步的属性'''
        self.num_points = num_points

        # 所有随机漫步都以一个(0, 0)点开始
        self.x_values = [0]
        self.y_values = [0]


    def fill_walk(self):
        '''根据当前的坐标生成随机步数'''

        # 不断漫步，直到列表达到指定的长度
        while len(self.x_values) < self.num_points:

            # 决定前进方向以及沿这个方向前进的距离
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4, 5, 6])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4, 5, 6])
            y_step = y_direction * y_distance

            # 不能原地不动
            if x_step == 0 and y_step == 0:
                continue

            # 计算下一个点的x值和y值
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)