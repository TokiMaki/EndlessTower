import Project_SceneFrameWork
from pico2d import *

# 무기를 쥐어줄때는 원 좌표에서 16을 빼야됨

name = "Battle"
actor = None
weapon = None
user = None
frame = 0
frame_tog = 1
Window_W = 1024
Window_H = 768


def enter():
    global actor
    global weapon
    open_canvas(Project_SceneFrameWork.Window_W, Project_SceneFrameWork.Window_H)
    actor = load_image('Resource\\Actor\\Actor1_1.png')
    weapon = load_image('Resource\\Actor\\Weapons1.png')


def exit():
    global actor
    actor = None
    close_canvas()


def update(frame_time):
    global frame
    global frame_tog
    frame = (frame + frame_tog) % 3
    if (frame >= 2):
        frame_tog = -1
    if (frame <= 0):
        frame_tog = 1
    delay(1 / 4)


def draw(frame_time):
    global actor
    global weapon
    global frame
    global Window_W
    global Window_H
    clear_canvas()
    # weapon.clip_draw(96 * frame , 320 - 64 * 5, 96, 64, 100 + 48, 300 + 64)
    # weapon.clip_draw(96 * frame + 96 * 3, 320 - 64 * 5, 96, 64, 100 - 16, 300 + 64)
    actor.clip_draw(64 * frame, 320 - 64 * 0, 64, 64, 700 + 64 * 0, Window_H / 2)
    actor.clip_draw(64 * frame, 320 - 64 * 0, 64, 64, 800 + 64 * 0, Window_H / 2 + 64)
    actor.clip_draw(64 * frame, 320 - 64 * 0, 64, 64, 800 + 64 * 0, Window_H / 2 - 64)
    actor.clip_draw(64 * frame, 320 - 64 * 0, 64, 64, 900 + 64 * 0, Window_H / 2)

    update_canvas()


def handle_events(frame_time):
    events = get_events()
    pass


def pause(): pass


def resume(): pass
