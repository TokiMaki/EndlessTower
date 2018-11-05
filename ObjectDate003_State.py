from pico2d import *
import ObjectDate001_Actor as Obj_Actort
import Resource_Manager as rssmgr
import Project_SceneFrameWork as Framework

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 4

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
        rssmgr.Actor1[Actor.actor_num][Actor.actor_in_num].image.clip_draw(64 * int(Actor.frame), 320 - 64 * 0, 64, 64, Actor.x, Actor.y)
        if (Actor.myturn == 1):
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