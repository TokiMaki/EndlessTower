from pico2d import *
import ObjectDate001_Actor as Obj_Actor

class Motion
    def __init__(self):
        self.specialskill = 0
        self.x = 0
        self.y = 0
        self.frame = 0
        self.procedure = 0
    def update(self, frame_time):
        self.frame = 0
    def draw(self, frame_time):
        pass

def Skill_Motion(Actor, left, down, procedure, frame):
    if (left == 12 and down == 15):
