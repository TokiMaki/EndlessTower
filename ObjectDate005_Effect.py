from pico2d import *
import Project_SceneFrameWork as Framework
import Resource_Manager as rssmgr
import System_000_Battle as Sys_Battle
import ObjectDate002_Monster as Obj_Monster
import ObjectDate003_State as Obj_State

effect = None

class Effect:
    def __init__(self, target, max_frame, effect_num):

        self.target = target
        self.x, self.y = Obj_Monster.monster[self.target].x, Obj_Monster.monster[self.target].y

        self.frame = 0
        self.max_frame = max_frame
        self.effect_num = effect_num

        self.TIME_PER_ACTION = 0.25  # 초당 0.5장
        self.ACTION_PER_TIME = 1.0 / self.TIME_PER_ACTION  # 1초에 2개
        self.FRAMES_PER_ACTION = max_frame  # 총 4장

    def update(self):
        if (self.frame < self.max_frame):
            self.frame += self.ACTION_PER_TIME * self.FRAMES_PER_ACTION * Framework.frame_time

    def position_set(self):
        if (self.position == 0):
            self.x = 650
            self.y = Framework.Window_H / 2
        if (self.position == 1):
            self.x = 750
            self.y = Framework.Window_H / 2 + 64
        if (self.position == 2):
            self.x = 750
            self.y = Framework.Window_H / 2 - 64
        if (self.position == 3):
            self.x = 850
            self.y = Framework.Window_H / 2

    def draw(self):
        if (self.frame > 0):
            rssmgr.Effect[0].image.clip_draw(192 * int(self.frame), 0, 192, 192,
                                            self.x, self.y , 96, 96)