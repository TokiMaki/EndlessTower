from pico2d import *
import Project_SceneFrameWork
import Resource_Manager as rssmgr

monster = None

class Monster:
    def __init__(self):
        self.x, self.y = 0, 0
        self.frame = 0
        self.framebool = 1
        self.dir = 1
        self.position = 0
        self.Acgauge = 0;
        self.speed = 0;
        self.myturn = 0
        self.hp = 100;

    def update(self, frame_time):
        self.frame = (self.frame + self.framebool)
        if (self.position == 0):
            self.x = 350
            self.y = Project_SceneFrameWork.Window_H / 2
        if (self.position == 1):
            self.x = 250
            self.y = Project_SceneFrameWork.Window_H / 2 + 64
        if (self.position == 2):
            self.x = 250
            self.y = Project_SceneFrameWork.Window_H / 2 - 64
        if (self.position == 3):
            self.x = 150
            self.y = Project_SceneFrameWork.Window_H / 2
        if (self.frame >= 2):
            self.framebool = -1
        if (self.frame <= 0):
            self.framebool = 1

    def draw(self):
        rssmgr.Monster.image.clip_draw(48 * self.frame, 240 - 48 * 0, 48, 48, self.x, self.y, 64, 64)