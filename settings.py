class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.f_speed = 3
        #laser settings
        self.laser_speed = 2.5
        self.laser_height = 45
        self.laser_width = 4
        self.laser_color = (255,0,0) # want red
        #this is a limit I didn't think of , should be something for playtesting
        self.laser_capacity = 3
        self.f_eye1 = 0