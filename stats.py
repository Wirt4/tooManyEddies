class Stats:

    def __init__(self, tme_game):
        self.settings = tme_game.settings
        self.reset_stats()
        self.game_active = False
        self.high_score = 1500

    def reset_stats(self):
        """Initialize the stats to track for the game"""
        self.frasiers_left = self.settings.f_limit
        self.score = 0
        self.level = 1
