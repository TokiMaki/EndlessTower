from pico2d import *
import Project_SceneFrameWork as FrameWork
import Resource_Manager as rssmgr
import random
import ObjectDate005_Effect as Obj_Effect

monster = None

class Monster:
    def __init__(self):
        self.x, self.y = 0, 0

        self.frame = 0
        self.framebool = 1
        self.dir = 1
        self.Acgauge = 0;
        self.myturn = 0
        self.kind = 0

        self.position = 0
        self.state = 0      # 0은 기본 1은 사망
        self.hp = 1000
        self.atk = 100
        self.speed = 10

        self.effect = None

    def update(self, frame_time):
        self.frame = (self.frame + self.framebool)
        if (self.effect != None):
            self.effect.update()
        if (self.hp <= 0):
            self.state = 1
        if (self.frame >= 2):
            self.framebool = -1
        if (self.frame <= 0):
            self.framebool = 1

    def position_set(self):
        self.x = 250
        self.y = FrameWork.Window_H / 2

    def get_bb(self):
        if (self.position == 0):
            return 250 - 32, FrameWork.Window_H / 2 - 64 - 32, 250 + 32, FrameWork.Window_H / 2 - 64 + 32

    def draw(self):
        if (self.state == 0):
            if (self.effect != None):
                self.effect.draw()
            rssmgr.Monster[0].image.clip_draw(48 * self.frame + ((48 * 3) * (self.kind % 4)), 240 - ((48 * 4) * int(self.kind / 4)), 48, 48, self.x, self.y, 196, 196)

        if (self.state == 1):
            rssmgr.Monster[1].image.clip_draw(48 * (self.kind % 4), 384 - (48 * self.frame) - ((48 * 3) * int(self.kind / 4)), 48, 48, self.x, self.y, 196, 196)