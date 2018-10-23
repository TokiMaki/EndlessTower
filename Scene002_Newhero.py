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
weapon = None
user = None
frame = 0
frame_tog = 1
frame_updater = 8
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
    gachahero.actor_num = 0
    gachahero.actor_in_num = random.randint(0, 7)
    Obj_Actor.hero.append(gachahero)


def exit():
    pass


def update(frame_time):
    global frame_updater, frame, framebool
    frame_updater += 1
    if (frame_updater > (Framework.FPS_TIME / 8.0)):
        frame += framebool
        if frame >= 2:
            framebool *= -1
        if frame <= 0:
            framebool *= -1
        pass


def draw(frame_time):
    global frame, gachahero
    clear_canvas()
    rssmgr.Actor[gachahero.actor_num].image.clip_draw(48 * frame + (48 * 3) * (gachahero.actor_in_num % 4), (48 * 7) - (48 * 4) * int((gachahero.actor_in_num / 4)), 48, 48, 400, 300)
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