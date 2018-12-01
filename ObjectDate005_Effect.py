from pico2d import *
import Project_SceneFrameWork as Framework
import Resource_Manager as rssmgr
import System_000_Battle as Sys_Battle
import ObjectDate002_Monster as Obj_Monster
import ObjectDate003_State as Obj_State
import random

class Effect:
    def __init__(self, target, effect_num):

        self.target = target
        self.x, self.y = random.randint(Obj_Monster.monster.x - 48, Obj_Monster.monster.x + 48), random.randint(Obj_Monster.monster.y - 48, Obj_Monster.monster.y + 48)

        self.frame = 0
        self.effect_num = effect_num
        self.max_frame = rssmgr.Effect[self.effect_num].max_frame

        self.TIME_PER_ACTION = 0.5  # 초당 0.5장
        self.ACTION_PER_TIME = 1.0 / self.TIME_PER_ACTION  # 1초에 2개
        self.FRAMES_PER_ACTION = 4  # 총 4장

    def update(self):
        if (self.frame < self.max_frame):
            self.frame += self.ACTION_PER_TIME * self.FRAMES_PER_ACTION * Framework.frame_time

    def draw(self):
        if (self.frame > 0 and self.frame < self.max_frame):
            rssmgr.Effect[self.effect_num].image.clip_draw(192 * (int(self.frame) % 5), 192 * int((self.max_frame - self.frame) / 5), 192, 192, self.x, self.y, 96, 96)