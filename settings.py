class Settings:
    def __init__(self):
        self.screen_width = 700
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.f_speed = 0.25
        self.f_limit = 2
        #laser settings
        self.laser_speed = 1.0
        self.laser_height = 50
        self.laser_width = 10
        #will eventually refactor laser to be a graphical pair of beams
        self.laser_color = (255, 0, 0) # want red
        self.laser_capacity = 3
        self.f_eye1 = 60
        #eddie settings
        self.eddie_speed = 1.0
        self.eddie_drop_speed = 10
        self.eddie_dir = 1

        self.accelerate = 1.5
        self.initialize_dynamic_settings()
        #can initialize an event drop rate here

    def initialize_dynamic_settings(self):
        self.eddie_speed = 0.07


    def increase_speed(self):
        if self.eddie_speed < 0:
            self.eddie_speed /= self.accelerate
        else:
            self.eddie_speed *= self.accelerate
        #self.laser_speed *= self.accelerate