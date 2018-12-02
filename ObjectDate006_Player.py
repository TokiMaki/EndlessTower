from pico2d import *
import Project_SceneFrameWork
import Resource_Manager as rssmgr
import System_000_Battle as Sys_Battle
import ObjectDate005_Effect as Obj_Effect
import ObjectDate003_State as Obj_State
import random

player = None

class Player:
    def __init__(self):
        self.x, self.y = 0, 0
        self.dir = 1
        self.effect = []
        self.now_skill = 0
        self.exp = 0
        self.nextexp = 5
        self.level = 1

        self.atk = 5

    def level_stat(self):
        if (self.exp > self.nextexp):
            self.level += 1
            self.atk = self.atk * 1.2
            self.exp = self.exp - self.nextexp
            self.nextexp = self.nextexp + 2


    def update(self, frame_time):
        for i in range(0, len(self.effect)):
            self.effect[i].update()
        self.level_stat()

    def return_myturn(self):
        return self.myturn

    def get_bb(self):
        return self.x - 48, self.y - 48, self.x + 48, self.y + 48

    def position_set(self):
        self.x = random.randint(650, 850)
        self.y = random.randint(Project_SceneFrameWork.Window_H / 2 - 32 - 96, Project_SceneFrameWork.Window_H / 2 + 32 + 96)

    def draw(self):
        for i in range(0, len(self.effect)):
            self.effect[i].update()