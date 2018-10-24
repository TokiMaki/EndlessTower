from pico2d import *
import Project_SceneFrameWork
import Resource_Manager as rssmgr
import System_000_Battle as Sys_Battle

hero = []
hero_num = 0
actor = []

class Actor:
    def __init__(self):
        self.x, self.y = 0, 0
        self.motionstate = 0
        self.frame = 0
        self.framebool = 1
        self.dir = 1
        self.position = 0
        self.skill = [Skill() for i in range(3)]

        self.Acgauge = 0;
        self.speed = 0;

        self.myturn = 0
        self.state = 0      # 0은 생존 1은 죽음
        self.grade = 0
        self.job = 0    # 0은 전사 1은 도적 2는 마법사 3은 성직자
        self.hp = 0
        self.atk = 0

        self.actor_num = 0
        self.actor_in_num = 0

        self.skill[0].kind = 0
        self.skill[1].kind = 1
        self.skill[2].kind = 2

    def update(self, frame_time):
        if (self.hp <= 0):
            self.state = 1
        self.frame = (self.frame + self.framebool)
        if (self.frame >= 2):
            self.framebool = -1
        if (self.frame <= 0):
            self.framebool = 1

    def position_set(self):
        if (self.position == 0):
            self.x = 650
            self.y = Project_SceneFrameWork.Window_H / 2
        if (self.position == 1):
            self.x = 750
            self.y = Project_SceneFrameWork.Window_H / 2 + 64
        if (self.position == 2):
            self.x = 750
            self.y = Project_SceneFrameWork.Window_H / 2 - 64
        if (self.position == 3):
            self.x = 850
            self.y = Project_SceneFrameWork.Window_H / 2

    def draw(self):
        if (self.state == 0):
            rssmgr.Actor1[self.actor_in_num].image.clip_draw(64 * self.frame, 320 - 64 * 0, 64, 64, self.x, self.y)
        if (self.state == 1):
            rssmgr.Actor1[self.actor_in_num].image.clip_draw(64 * self.frame + (64 * 6), 320 - 64 * 5, 64, 64, self.x, self.y)

class Skill:
    def __init__(self):
        self.x, self.y = 0, 0
        self.left_num = 12           # 왼쪽에서부터 몇번째 이미지
        self.updown_num = 15           # 아래에서 위쪽으로 몇번째 이미지
        self.kind = 0

    def update(self):
        pass

    def draw(self):
        if (self.kind == 0):
            rssmgr.Skill.image.clip_draw(32 * self.left_num, 32 * self.updown_num, 32, 32, Project_SceneFrameWork.Window_W - (64 * 3), 64, 64, 64)
            if (Sys_Battle.Sel_Skill == 0):
                rssmgr.Skill_sel.image.clip_draw(0, 0, 32, 32, Project_SceneFrameWork.Window_W - (64 * 3), 64, 64, 64)
        if (self.kind == 1):
            rssmgr.Skill.image.clip_draw(32 * self.left_num, 32 * self.updown_num, 32, 32, Project_SceneFrameWork.Window_W - (64 * 2), 64, 64, 64)
            if (Sys_Battle.Sel_Skill == 1):
                rssmgr.Skill_sel.image.clip_draw(0, 0, 32, 32, Project_SceneFrameWork.Window_W - (64 * 2), 64, 64, 64)
        if (self.kind == 2):
            rssmgr.Skill.image.clip_draw(32 * self.left_num, 32 * self.updown_num, 32, 32, Project_SceneFrameWork.Window_W - (64 * 1), 64, 64, 64)
            if (Sys_Battle.Sel_Skill == 2):
                rssmgr.Skill_sel.image.clip_draw(0, 0, 32, 32, Project_SceneFrameWork.Window_W - (64 * 1), 64, 64, 64)
