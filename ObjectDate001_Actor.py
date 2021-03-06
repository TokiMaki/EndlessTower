from pico2d import *
import Project_SceneFrameWork
import Resource_Manager as rssmgr
import System_000_Battle as Sys_Battle
import ObjectDate005_Effect as Obj_Effect
import ObjectDate003_State as Obj_State
import random

hero = []
actor = []
play_actor = []


class Actor:
    def __init__(self):
        self.x, self.y = 0, 0
        self.motionstate = 0
        self.frame = 0
        self.framebool = 1
        self.actframe = 0
        self.target = None
        self.next_act_frame = 0
        self.dir = 1
        self.position = 0
        self.skill = [Skill() for i in range(2)]
        self.effect = None
        self.now_skill = 0
        self.exp = 0
        self.nextexp = 5
        self.level = 1

        self.now_skill_left = 0
        self.now_skill_updown = 0

        self.Acgauge = 0

        self.myturn = 0
        self.state = 0      # 0은 생존 1은 죽음
        self.grade = 0
        self.job = 0    # 0은 전사 1은 도적 2는 마법사 3은 성직자
        self.maxhp = 1
        self.hp = 1
        self.speed = 0
        self.atk = 0

        self.actor_num = 0
        self.actor_in_num = 0

        self.skill[0].kind = 0
        self.skill[1].kind = 1

        self.event_que = []
        self.cur_state = Obj_State.IdleState
        self.cur_state.enter(self)

    def level_stat(self):
        if (self.exp > self.nextexp):
            self.level += 1
            self.maxhp = self.maxhp * 1.2
            self.atk = self.atk * 1.2
            self.exp = self.exp - self.nextexp
            self.nextexp = self.nextexp + 3


    def update(self, frame_time):
        self.cur_state.do(self)
        self.level_stat()
        if len(self.event_que) > 0:
            self.cur_state.exit(self)
            self.cur_state = self.event_que.pop()
            if (self.cur_state != Obj_State.BasicAttackState and self.cur_state != Obj_State.MagicState):
                self.cur_state.enter(self)
            if (self.cur_state == Obj_State.BasicAttackState or self.cur_state == Obj_State.MagicState):
                self.cur_state.enter(self, self.skill[self.now_skill].updown_num, self.skill[self.now_skill].left_num)

    def return_myturn(self):
        return self.myturn

    def get_bb(self):
        if (self.position == 0):
            return 650 - 32, Project_SceneFrameWork.Window_H / 2 - 32, 650 + 32, Project_SceneFrameWork.Window_H / 2 + 32
        if (self.position == 1):
            return 750 - 32, Project_SceneFrameWork.Window_H / 2 + 64 - 32, 750 + 32, Project_SceneFrameWork.Window_H / 2 + 64 + 32
        if (self.position == 2):
            return 750 - 32, Project_SceneFrameWork.Window_H / 2 - 64 - 32, 750 + 32, Project_SceneFrameWork.Window_H / 2 - 64 + 32
        if (self.position == 3):
            return 850 - 32, Project_SceneFrameWork.Window_H / 2 - 32, 850 + 32, Project_SceneFrameWork.Window_H / 2 + 32

    def position_set(self):
        self.x = random.randint(650, 850)
        self.y = random.randint(Project_SceneFrameWork.Window_H / 2 - 32 - 96, Project_SceneFrameWork.Window_H / 2 + 32 + 96)

    def draw(self):
        self.cur_state.draw(self)

class Skill():
    def __init__(self, kind = 0, left = 0, updown = 0):
        self.x, self.y = 0, 0
        self.kind = kind
        self.left_num = left           # 왼쪽에서부터 몇번째 이미지
        self.updown_num = updown           # 아래에서 위쪽으로 몇번째 이미지
        self.cooltime = 2
        self.skillturn = 0

    def update(self):
        pass

    def get_bb(self):
        return Project_SceneFrameWork.Window_W - (64 * (3 - self.kind)) - 32, 64 - 32, Project_SceneFrameWork.Window_W - (64 * (3 - self.kind)) + 32, 64 + 32

    def draw(self):
        if (self.kind == 0):
            rssmgr.Skill.image.clip_draw(32 * self.left_num, 32 * self.updown_num, 32, 32,
                                         Project_SceneFrameWork.Window_W - (64 * 3), 64, 64, 64)
        if (self.kind == 1):
            rssmgr.Skill.image.clip_draw(32 * self.left_num, 32 * self.updown_num, 32, 32,
                                         Project_SceneFrameWork.Window_W - (64 * 2), 64, 64, 64)