# 在 game_stats.py 文件中
import os


class GameStats():
    """跟踪游戏的统计信息"""

    def __init__(self, ai_settings):
        """初始化统计信息"""
        self.ai_settings = ai_settings
        self.reset_stats()
        # 游戏刚启动的时候处于活动状态
        self.game_active = False
        # 在任何情况下都不应该重置最高分
        self.high_score = 0
        self.load_high_score()  # 在初始化时加载最高分

    def reset_stats(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1

    def save_high_score(self):
        """将最高得分保存到文件"""
        with open('1.txt', 'w') as file:
            file.write(str(self.high_score))

    def load_high_score(self):
        """从文件加载最高得分"""
        if os.path.exists('1.txt'):
            with open('1.txt', 'r') as file:
                try:
                    self.high_score = int(file.read())
                except ValueError:
                    # 文件内容不是整数，可能是损坏的文件等，忽略错误
                    pass
