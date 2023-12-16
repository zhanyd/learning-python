import os
import pygame

class Ship:
    '''管理飞船的类'''

    def __init__(self, ai_game):
        '''初始化飞船并设置其初始位置'''
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # 获取当前脚本所在目录
        current_dir = os.path.dirname(os.path.realpath(__file__))

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load(current_dir + '/images/ship.bmp')
        self.rect = self.image.get_rect()

        # 计算飞船的位置，让其居中
        self.rect.midbottom = self.screen_rect.midbottom

        # 在飞船的属性x中存储小数值
        self.x = float(self.rect.x)

        # 移动标志
        self.moving_right = False
        self.moving_left = False

        # 速度
        self.ship_speed = 1.5

    def blitem(self):
        '''在指定位置绘制飞船'''
        self.screen.blit(self.image, self.rect)

    def update(self):
        '''根据移动标志更新飞船的位置'''
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.ship_speed

        # 根据self.x更新rect.x
        self.rect.x = self.x    

    def center_ship(self):
        '''让飞船在屏幕低端居中'''
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
    