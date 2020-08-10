class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.f_speed = 3
        #laser settings
        self.laser_speed = 2.5
        self.laser_height = 100
        self.laser_width = 40
        #will eventually refactor laser to be a graphical pair of beams
        self.laser_color = (255,0,0) # want red
        self.laser_capacity = 3
        #for placing the laser over frasier's face
        self.f_eye1 = 197