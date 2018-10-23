import Project_SceneFrameWork as Framework
import ObjectDate001_Actor
import ObjectDate002_Monster
from pico2d import *
import Resource_Manager as rssmgr
import Scene002_Newhero as Sc_Newhero
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


def enter():
    open_canvas(Framework.Window_W, Framework.Window_H)
    rssmgr.Upload_data()


def exit():
    close_canvas()


def update(frame_time):
    global frame_updater
    frame_updater += 1
    if (frame_updater > (Framework.FPS_TIME / 8.0)):
        pass


def draw(frame_time):
    clear_canvas()
    # weapon.clip_draw(96 * frame , 320 - 64 * 5, 96, 64, 100 + 48, 300 + 64)
    # weapon.clip_draw(96 * frame + 96 * 3, 320 - 64 * 5, 96, 64, 100 - 16, 300 + 64)
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
            Framework.push_state(Sc_Newhero)
    pass


def pause(): pass


def resume(): pass
