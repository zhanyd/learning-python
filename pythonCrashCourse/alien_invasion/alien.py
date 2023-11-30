import os
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    '''表示单个外星人的类'''
    
    def __init__(self, ai_game):
        '''初始化外星人并设置其初始位置'''
        super().__init__()
        self.screen = ai_game.screen

        # 获取当前脚本所在目录
        current_dir = os.path.dirname(os.path.realpath(__file__))
        # 加载外星人图像并设置其rect属性
        self.image = pygame.image.load(current_dir + '/images/alien.bmp')
        self.rect = self.image.get_rect()

        # 每个外星人最初都在左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储外星人的精确水平位置
        self.x = float(self.rect.x)

        
