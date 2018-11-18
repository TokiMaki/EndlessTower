from pico2d import *
import ObjectDate001_Actor as Obj_Actort
import Resource_Manager as rssmgr
import Project_SceneFrameWork as Framework
import System_000_Battle as Sys_Battle

TIME_PER_ACTION = 0.5       # 초당 0.5장
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION     # 1초에 2개
FRAMES_PER_ACTION = 4   # 총 4장

ATT_TIME_PER_ACTION = 1       # 초당 1장
ATT_ACTION_PER_TIME = 1.0 / ATT_TIME_PER_ACTION     # 1초에 1개
ATT_FRAMES_PER_ACTION = 3   # 총 3장

PIXEL_PER_METER = (10.0 / 0.2) # 10pixel 20cm
RUN_SPEED_KMPH = 20.0 # km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

class IdleState:
    @staticmethod
    def enter(Actor):
        Actor.frame = 0
        Actor.framebool = FRAMES_PER_ACTION * ACTION_PER_TIME

    @staticmethod
    def exit(Actor):
        pass

    @staticmethod
    def do(Actor):
        if (Actor.hp <= 0):
            Actor.event_que.append(DeadState)
        Actor.frame = (Actor.frame + (Actor.framebool * Framework.frame_time))
        if (Actor.frame >= 3):
            Actor.frame = 2.99
            Actor.framebool *= -1
        if (Actor.frame <= 0):
            Actor.framebool *= -1

    @staticmethod
    def draw(Actor):
        if (Actor.myturn == 0):
            rssmgr.Actor1[Actor.actor_num][Actor.actor_in_num].image.clip_draw(64 * int(Actor.frame), 320 - 64 * 0, 64, 64, Actor.x, Actor.y)
        if (Actor.myturn == 1):
            rssmgr.Actor1[Actor.actor_num][Actor.actor_in_num].image.clip_draw(64 * int(Actor.frame), 320 - 64 * 1, 64, 64, Actor.x, Actor.y)
            rssmgr.Skill_sel.image.clip_draw(0, 0, 32, 32, Actor.x, Actor.y, 64, 64)

class DeadState:
    @staticmethod
    def enter(Actor):
        Actor.frame = 0
        Actor.framebool = FRAMES_PER_ACTION * ACTION_PER_TIME

    @staticmethod
    def exit(Actor):
        pass

    @staticmethod
    def do(Actor):
        Actor.frame = (Actor.frame + Actor.framebool * Framework.frame_time)
        if (Actor.hp > 0):
            Actor.event_que.append(IdleState)
        if (Actor.frame >= 3):
            Actor.frame = 2.99
            Actor.framebool *= -1
        if (Actor.frame <= 0):
            Actor.framebool *= -1

    @staticmethod
    def draw(Actor):
        rssmgr.Actor1[Actor.actor_num][Actor.actor_in_num].image.clip_draw(64 * int(Actor.frame) + (64 * 6), 320 - 64 * 5, 64, 64, Actor.x, Actor.y)

class AttackState:
    @staticmethod
    def enter(Actor):
        Actor.frame = 0
        Actor.framebool = FRAMES_PER_ACTION * ACTION_PER_TIME
        Actor.actframe = 0
        Actor.next_act_frame = 0

    @staticmethod
    def exit(Actor):
        pass

    @staticmethod
    def do(Actor):


        if (Actor.next_act_frame == 0):
            Actor.actframe += Framework.frame_time
            if (Actor.actframe < 0.5):
                Actor.x -= RUN_SPEED_PPS * Framework.frame_time
            if (Actor.actframe >= 0.5):
                Actor.next_act_frame += 1
                Actor.frame = 0
                Actor.framebool = ATT_FRAMES_PER_ACTION * ATT_ACTION_PER_TIME

        if (Actor.next_act_frame == 1):
            Actor.frame = (Actor.frame + Actor.framebool * Framework.frame_time)
            if (Actor.frame >= 3):
                Actor.next_act_frame += 1
                Actor.frame = 0
                Actor.framebool = FRAMES_PER_ACTION * ACTION_PER_TIME

        if (Actor.next_act_frame == 2):
            Actor.position_set()
            Actor.myturn = 0
            Actor.Acgauge = 0
            Sys_Battle.Sel_Skill = 0
            Sys_Battle.Sel_Monster = None
            Actor.event_que.append(IdleState)


    @staticmethod
    def draw(Actor):
        if (Actor.next_act_frame == 0):
            rssmgr.Actor1[Actor.actor_num][Actor.actor_in_num].image.clip_draw(64 * int(Actor.frame) + 64 * 0, 320 - 64 * 0, 64, 64, Actor.x, Actor.y)
        if (Actor.next_act_frame == 1):
            rssmgr.Weapon.image.clip_draw(96 * int(Actor.frame) + 96 * 0, 320 - 64 * 0, 96, 64, Actor.x - 16, Actor.y)
            rssmgr.Actor1[Actor.actor_num][Actor.actor_in_num].image.clip_draw(64 * int(Actor.frame) + 64 * 3, 320 - 64 * 1, 64, 64, Actor.x, Actor.y)

class VictoryState:
    @staticmethod
    def enter(Actor):
        Actor.frame = 0
        Actor.framebool = FRAMES_PER_ACTION * ACTION_PER_TIME

    @staticmethod
    def exit(Actor):
        pass

    @staticmethod
    def do(Actor):
        Actor.frame = (Actor.frame + Actor.framebool * Framework.frame_time)
        if (Actor.frame >= 3):
            Actor.frame = 2.99
            Actor.framebool *= -1
        if (Actor.frame <= 0):
            Actor.framebool *= -1

    @staticmethod
    def draw(Actor):
        rssmgr.Actor1[Actor.actor_num][Actor.actor_in_num].image.clip_draw(64 * int(Actor.frame) + (64 * 6), 320 - 64 * 1, 64, 64, Actor.x, Actor.y)

class LobbyState:
    @staticmethod
    def enter(Actor):
        Actor.frame = 0
        Actor.framebool = FRAMES_PER_ACTION * ACTION_PER_TIME

    @staticmethod
    def exit(Actor):
        pass

    @staticmethod
    def do(Actor):
        Actor.frame = (Actor.frame + Actor.framebool * Framework.frame_time)
        if (Actor.frame >= 3):
            Actor.frame = 2.99
            Actor.framebool *= -1
        if (Actor.frame <= 0):
            Actor.framebool *= -1

    @staticmethod
    def draw(Actor):
        rssmgr.Actor[Actor.actor_num].image.clip_draw(48 * int(Actor.frame) + (48 * 3) * (Actor.actor_in_num % 4), (48 * 7) - (48 * 4) * int((Actor.actor_in_num / 4)), 48, 48, Framework.Window_W / 2, Framework.Window_H / 2)