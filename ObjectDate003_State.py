from pico2d import *
import ObjectDate001_Actor as Obj_Actort
import Resource_Manager as rssmgr
import Project_SceneFrameWork as FrameWork

class IdleState:
    @staticmethod
    def enter(Actor):
        Actor.frame = 0
        Actor.framebool = 1

    @staticmethod
    def exit(Actor):
        pass

    @staticmethod
    def do(Actor):
        if (Actor.hp <= 0):
            Actor.event_que.append(DeadState)
        Actor.frame = (Actor.frame + Actor.framebool)
        if (Actor.frame >= 2):
            Actor.framebool = -1
        if (Actor.frame <= 0):
            Actor.framebool = 1

    @staticmethod
    def draw(Actor):
        rssmgr.Actor1[Actor.actor_in_num].image.clip_draw(64 * Actor.frame, 320 - 64 * 0, 64, 64, Actor.x, Actor.y)

class DeadState:
    @staticmethod
    def enter(Actor):
        Actor.frame = 0
        Actor.framebool = 1

    @staticmethod
    def exit(Actor):
        pass

    @staticmethod
    def do(Actor):
        Actor.frame = (Actor.frame + Actor.framebool)
        if (Actor.frame >= 2):
            Actor.framebool = -1
        if (Actor.frame <= 0):
            Actor.framebool = 1

    @staticmethod
    def draw(Actor):
        rssmgr.Actor1[Actor.actor_in_num].image.clip_draw(64 * Actor.frame + (64 * 6), 320 - 64 * 5, 64, 64, Actor.x, Actor.y)

class LobbyState:
    @staticmethod
    def enter(Actor):
        Actor.frame = 0
        Actor.framebool = 1

    @staticmethod
    def exit(Actor):
        pass

    @staticmethod
    def do(Actor):
        Actor.frame = (Actor.frame + Actor.framebool)
        if (Actor.frame >= 2):
            Actor.framebool = -1
        if (Actor.frame <= 0):
            Actor.framebool = 1

    @staticmethod
    def draw(Actor):
        rssmgr.Actor[Actor.actor_num].image.clip_draw(48 * Actor.frame + (48 * 3) * (Actor.actor_in_num % 4), (48 * 7) - (48 * 4) * int((Actor.actor_in_num / 4)), 48, 48, FrameWork.Window_W / 2, FrameWork.Window_H / 2)