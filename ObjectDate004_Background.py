from pico2d import *
import Project_SceneFrameWork
import Resource_Manager as rssmgr
import random
import System_000_Battle as Sys_Battle
import ObjectDate003_State as Obj_State

class Background:

    def __init__(self, state):
        self.x = Project_SceneFrameWork.Window_W / 2
        self.y = Project_SceneFrameWork.Window_H / 2
        self.random_background = random.randint(0, 2)
        self.state = state

    def update(self, frame_time):
        pass

    def draw(self):
        if self.state == 0:
            rssmgr.battle_background[self.random_background].image.clip_draw(0, 0, 1000, 740, self.x, self.y, Project_SceneFrameWork.Window_W, Project_SceneFrameWork.Window_H)
        if self.state == 1:
            for i in range(0, 2):
                rssmgr.actor_maneger_background[i].image.clip_draw(0, 0, 1000, 740, self.x, self.y, Project_SceneFrameWork.Window_W, Project_SceneFrameWork.Window_H)
        if self.state == 2:
            for i in range(0, 2):
                rssmgr.gacha_background[i].image.clip_draw(0, 0, 1000, 740, self.x, self.y, Project_SceneFrameWork.Window_W, Project_SceneFrameWork.Window_H)
        if self.state == 3:
            rssmgr.Logo_background[0].image.clip_draw(0, 0, 1024, 768, self.x, self.y, Project_SceneFrameWork.Window_W, Project_SceneFrameWork.Window_H)
            rssmgr.Logo_background[1].image.clip_draw(0, 0, 480, 288, self.x, self.y, 480 * 1.5, 288 * 1.5)