import os
import pygame.font
from pygame.sprite import Group
from ship import Ship

class Scoreboard:
    '''显示得分的信息的类'''

    def __init__(self, ai_game):
        '''初始化显示得分信息'''
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # 显示得分信息的字体
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        # 准备初始得分图像
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        '''将得分转换为一幅渲染的图像'''
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color,
                                           self.settings.bg_color)

        # 将得分放在屏幕右上角
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        '''将最高得分转换为一幅渲染的图像'''
        high_score = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color,
                                           self.settings.bg_color)

        # 将得分放在屏幕顶部中央
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.right = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top


    def prep_level(self):
        '''将等级转换为一幅渲染的图像'''
        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str, True, self.text_color,
                                           self.settings.bg_color)
        
        # 将等级放在得分下方
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10
    
    
    def show_score(self):
        '''在屏幕上显示得分'''
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)
    

    def check_high_score(self):
        '''检查是否有新的最高得分'''
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()
            # 将最高得分写入文件
            self.write_high_score()


    def prep_ships(self):
        '''显示还余下多少飞船'''
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_game)
            ship.rect.x = 10 + ship_number * ship.rect.width  
            ship.rect.y = 10
            self.ships.add(ship)

        
    def write_high_score(self):
        '''将最高得分写入文件'''
        # 获取当前脚本所在目录
        self.current_dir = os.path.dirname(os.path.realpath(__file__))
        high_score_file = open(os.path.join(self.current_dir, 'high_score.txt'), 'w')
        high_score_file.write(str(self.stats.high_score))
        high_score_file.close()
    

    