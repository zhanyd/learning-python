import os
class GameStats:
    '''跟踪游戏的统计信息'''

    def __init__(self, ai_game):
        '''初始化统计信息'''
        self.settings = ai_game.settings
        self.reset_stats()

        # 游戏刚启动时处于活动状态
        self.game_active = False

        # 任何情况下都不应该重置最高得分
        # self.high_score = 0

        # 从文件中读取最高得分
        self.read_high_score()


    def reset_stats(self):
        '''初始化在游戏运行期间可能变化的统计信息'''
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1


    def read_high_score(self):
        '''从文件中读取最高得分'''
        # 获取当前脚本所在目录
        self.current_dir = os.path.dirname(os.path.realpath(__file__))
        try:
            with open(os.path.join(self.current_dir, 'high_score.txt'), 'r') as high_score_file:
                self.high_score = int(high_score_file.read())
        except FileNotFoundError:
            self.high_score = 0
          