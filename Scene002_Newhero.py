import Project_SceneFrameWork as Framework
import ObjectDate001_Actor as Obj_Actor
import ObjectDate002_Monster
from pico2d import *
import Resource_Manager as rssmgr
import Scene001_Gacha as Sc_Gacha
import System_000_Battle as Sys_Battle
import random

# 무기를 쥐어줄때는 원 좌표에서 16을 빼야됨

name = "Battle"
user = None
x = 0
y = 0

gachahero = None
frame = 0
framebool = 1


def enter():
    global gachahero
    gachahero = Obj_Actor.Actor()
    gachahero.grade = random.randint(3, 5)
    gachahero.job = 0
    gachahero.actor_num = random.randint(0, 2)
    gachahero.actor_in_num = random.randint(0, 7)
    gachahero.job = random.randint(0, 3)
    if (gachahero.job == 0):
        gachahero.hp = random.randint(17, 20)
        gachahero.atk = random.randint(3, 5)
        gachahero.speed = random.randint(5, 6)
    if (gachahero.job == 1):
        gachahero.hp = random.randint(10, 13)
        gachahero.atk = random.randint(5, 7)
        gachahero.speed = random.randint(7, 9)
    if (gachahero.job == 2):
        gachahero.hp = random.randint(8, 12)
        gachahero.atk = random.randint(5, 7)
        gachahero.speed = random.randint(6, 7)
    if (gachahero.job == 3):
        gachahero.hp = random.randint(8, 12)
        gachahero.atk = random.randint(2, 4)
        gachahero.speed = random.randint(5, 6)
    Obj_Actor.hero.append(gachahero)


def exit():
    pass


def update(frame_time):
    global frame, framebool
    frame += framebool
    if frame >= 2:
        framebool *= -1
    if frame <= 0:
        framebool *= -1
        pass


def draw(frame_time):
    global frame, gachahero
    clear_canvas()
    rssmgr.Actor[gachahero.actor_num].image.clip_draw(48 * frame + (48 * 3) * (gachahero.actor_in_num % 4), (48 * 7) - (48 * 4) * int((gachahero.actor_in_num / 4)), 48, 48, Framework.Window_W / 2, Framework.Window_H / 2)
    update_canvas()


def handle_events(frame_time):
    global x, y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            Framework.running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            Framework.running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_t:
            Framework.pop_state()
    pass


def pause(): pass


def resume(): pass
