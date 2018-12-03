from pico2d import *
import Project_SceneFrameWork as FrameWork
import Resource_Manager as rssmgr
import random
import ObjectDate005_Effect as Obj_Effect

monster = None

TIME_PER_ACTION = 0.5       # 초당 0.5장
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION     # 1초에 2개
FRAMES_PER_ACTION = 4   # 총 4장

class Monster:
    def __init__(self, now_stage):
        self.x, self.y = 0, 0

        self.frame = 0
        self.framebool = FRAMES_PER_ACTION * ACTION_PER_TIME
        self.dir = 1
        self.Acgauge = 0;
        self.myturn = 0
        self.kind = random.randint(0, 7)
        if (now_stage == 5):
            self.kind = 8

        self.position = 0
        self.state = 0      # 0은 기본 1은 사망
        self.stage = now_stage
        self.maxhp = 1300 + int(1300 * (0.3 * now_stage))
        self.hp = 100
        self.atk = random.randint(5, 6) + int(random.randint(5, 6) * (0.3 * now_stage))
        self.speed = random.randint(10, 11) + int(random.randint(5, 6) * (0.3 * now_stage))

        self.effect = []

    def update(self, frame_time):
        self.frame = (self.frame + (self.framebool * FrameWork.frame_time))

        for effect in self.effect:
            effect.update()
        if (self.hp <= 0):
            self.state = 1
        if (self.frame >= 3):
            self.frame = 2.99
            self.framebool *= -1
        if (self.frame <= 0):
            self.framebool *= -1

    def position_set(self):
        self.x = 250
        self.y = FrameWork.Window_H / 2

    def get_bb(self):
        return 250 - 96, FrameWork.Window_H / 2 - 96, 250 + 98, FrameWork.Window_H / 2 + 96

    def draw(self):
        if (self.state == 0):
            for effect in self.effect:
                effect.draw()
            if (self.kind != 8):
                rssmgr.Monster[0].image.clip_draw(48 * int(self.frame) + ((48 * 3) * (self.kind % 4)), 240 - ((48 * 4) * int(self.kind / 4)), 48, 48, self.x, self.y, 192, 192)
            if (self.kind == 8):
                rssmgr.Monster[2].image.clip_draw(0, 0, 560, 560, self.x, self.y + int(self.frame) * 5, 192, 192)

        if (self.state == 1):
            if (self.kind != 8):
                rssmgr.Monster[1].image.clip_draw(48 * (self.kind % 4), 384 - (48 * int(self.frame)) - ((48 * 3) * int(self.kind / 4)), 48, 48, self.x, self.y, 192, 192)