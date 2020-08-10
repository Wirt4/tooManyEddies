class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.f_speed = 3
        self.f_limit =3
        #laser settings
        self.laser_speed = 4
        self.laser_height = 100
        self.laser_width = 40
        #will eventually refactor laser to be a graphical pair of beams
        self.laser_color = (255,0,0) # want red
        self.laser_capacity = 3
        self.f_eye1 = 197
        #eddie settings
        self.eddie_speed = 2.5
        self.eddie_drop_speed = 10
        self.eddie_dir = 1