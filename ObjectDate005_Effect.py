from pico2d import *
import Project_SceneFrameWork as Framework
import Resource_Manager as rssmgr
import System_000_Battle as Sys_Battle
import ObjectDate001_Actor as Obj_Actor
import ObjectDate002_Monster as Obj_Monster
import ObjectDate003_State as Obj_State
import ObjectDate006_Player as Obj_Player
import random

class Effect:
    def __init__(self, target, effect_num, damege):

        self.target = target
        self.x, self.y = random.randint(Obj_Monster.monster.x - 64, Obj_Monster.monster.x + 64), random.randint(Obj_Monster.monster.y - 64, Obj_Monster.monster.y + 64)

        self.frame = 0
        self.effect_num = effect_num
        self.max_frame = rssmgr.Effect[self.effect_num].max_frame

        self.TIME_PER_ACTION = 0.5  # 초당 0.5장
        self.ACTION_PER_TIME = 1.0 / self.TIME_PER_ACTION  # 1초에 2개
        self.FRAMES_PER_ACTION = 4  # 총 4장

        self.damege = Damege(self.x, self.y + 32, damege)
        self.sound = False


    def update(self):
        if (self.frame < self.max_frame):
            if self.sound == False:
                rssmgr.Effect[self.effect_num].sound.play()
                self.sound = True
            self.frame += self.ACTION_PER_TIME * self.FRAMES_PER_ACTION * Framework.frame_time
        if (self.max_frame - self.frame < 6):
            self.damege.update()

    def draw(self):
        if (self.frame > 0 and self.frame < self.max_frame):
            rssmgr.Effect[self.effect_num].image.opacify(0.7)
            rssmgr.Effect[self.effect_num].image.clip_draw(192 * (int(self.frame) % 5), 192 * int((self.max_frame - self.frame) / 5), 192, 192, self.x, self.y, 96, 96)
            if (self.max_frame - self.frame < 6):
                self.damege.draw()

class Mon_Effect:
    def __init__(self, target, effect_num, damege):

        self.target = target
        self.x, self.y = Obj_Actor.hero[target].x, Obj_Actor.hero[target].y

        self.frame = 0
        self.effect_num = effect_num
        self.max_frame = rssmgr.Effect[self.effect_num].max_frame

        self.TIME_PER_ACTION = 0.5  # 초당 0.5장
        self.ACTION_PER_TIME = 1.0 / self.TIME_PER_ACTION  # 1초에 2개
        self.FRAMES_PER_ACTION = 4  # 총 4장

        self.damege = Damege(self.x, self.y + 32, damege)

    def exit(self):
        Obj_Monster.monster.effect.remove(self)

    def update(self):
        if (self.frame < self.max_frame):
            self.frame += self.ACTION_PER_TIME * self.FRAMES_PER_ACTION * Framework.frame_time
        if (self.max_frame - self.frame < 6):
            self.damege.update()
        if (self.frame >= self.max_frame):
            Mon_Effect.exit(self)

    def draw(self):
        if (self.frame > 0 and self.frame < self.max_frame):
            rssmgr.Effect[self.effect_num].image.clip_draw(192 * (int(self.frame) % 5), 192 * int((self.max_frame - self.frame) / 5), 192, 192, self.x, self.y, 96, 96)
            if (self.max_frame - self.frame < 6):
                self.damege.draw()

class Player_Effect:
    def __init__(self, x, y, effect_num, damege):
        self.x, self.y = x, y

        self.frame = 0
        self.effect_num = effect_num
        self.max_frame = rssmgr.Effect[self.effect_num].max_frame

        self.TIME_PER_ACTION = 0.5  # 초당 0.5장
        self.ACTION_PER_TIME = 1.0 / self.TIME_PER_ACTION  # 1초에 2개
        self.FRAMES_PER_ACTION = 4  # 총 4장

        self.damege = Player_Damege(self.x, self.y + 32, damege)
        rssmgr.Effect[self.effect_num].sound.play()

    def exit(self):
        Obj_Player.player.effect.remove(self)

    def update(self):
        if (self.frame < self.max_frame):
            self.frame += self.ACTION_PER_TIME * self.FRAMES_PER_ACTION * Framework.frame_time
            self.damege.update()
        if (self.frame >= self.max_frame):
            Player_Effect.exit(self)

    def draw(self):
        if (self.frame > 0 and self.frame < self.max_frame):
            rssmgr.Effect[self.effect_num].image.clip_draw(192 * (int(self.frame) % 5), 192 * int((self.max_frame - self.frame) / 5), 192, 192, self.x, self.y, 96, 96)
            self.damege.draw()


class Damege:
    def __init__(self, x = 0, y = 0, damege = 0):
        self.x, self.y = x, y
        self.damege = damege
        self.frame = 0

    def update(self):
        if (self.frame < 0.5):
            self.frame += Framework.frame_time

    def draw(self):
        if self.frame < 0.5:
            rssmgr.font[0].font.draw(self.x, self.y + self.frame * 20, '%d' % self.damege, (255, 0, 0))

class Player_Damege:
    def __init__(self, x = 0, y = 0, damege = 0):
        self.x, self.y = x, y
        self.damege = damege
        self.frame = 0

    def update(self):
        if (self.frame < 0.5):
            self.frame += Framework.frame_time

    def draw(self):
        if self.frame < 0.5:
            rssmgr.font[0].font.draw(self.x, self.y + self.frame * 20, '%d' % self.damege, (0, 255, 0))