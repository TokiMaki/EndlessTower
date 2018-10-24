import Project_SceneFrameWork as Framework
import ObjectDate001_Actor
import ObjectDate002_Monster
from pico2d import *
import Resource_Manager as rssmgr
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
floor = 0


def enter():
    global weapon
    # open_canvas(Framework.Window_W, Framework.Window_H)
    rssmgr.Upload_data()
    ObjectDate002_Monster.monster = [ObjectDate002_Monster.Monster() for i in range(4)]
    if (ObjectDate001_Actor.hero_num < 4):
        for i in range (0 ,ObjectDate001_Actor.hero_num, 1):
            ObjectDate001_Actor.actor.append(ObjectDate001_Actor.hero[i])
            ObjectDate001_Actor.actor[i].position = i
            ObjectDate001_Actor.actor[i].speed = random.randint(5, 10)
    else:
        for i in range (0 ,4, 1):
            ObjectDate001_Actor.actor.append(ObjectDate001_Actor.hero[i])
            ObjectDate001_Actor.actor[i].position = i
            ObjectDate001_Actor.actor[i].speed = random.randint(5, 10)

    for act in ObjectDate001_Actor.actor:
        act.position_set()

    for i in range(0, 4, 1):
        ObjectDate002_Monster.monster[i].position = i
        ObjectDate002_Monster.monster[i].speed = random.randint(5, 10)

    for mon in ObjectDate002_Monster.monster:
        mon.position_set()

    weapon = load_image('Resource\\Actor\\Weapons1.png')


def exit():
    close_canvas()


def update(frame_time):
    global frame_updater
    frame_updater += 1
    if (frame_updater > (Framework.FPS_TIME / 8.0)):
        for act in ObjectDate001_Actor.actor:
            act.update(frame_time)
        for mon in ObjectDate002_Monster.monster:
            mon.update(frame_time)
        frame_updater = 0
    Sys_Battle.AcgaugeUpdate()


def draw(frame_time):
    clear_canvas()
    # weapon.clip_draw(96 * frame , 320 - 64 * 5, 96, 64, 100 + 48, 300 + 64)
    # weapon.clip_draw(96 * frame + 96 * 3, 320 - 64 * 5, 96, 64, 100 - 16, 300 + 64)
    for act in ObjectDate001_Actor.actor:
        act.draw()
        if (act.myturn == 1):
            for i in range(0, 3, 1):
                act.skill[i].draw()

    for mon in ObjectDate002_Monster.monster:
        mon.draw()


    update_canvas()


def handle_events(frame_time):
    global x, y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            exit()
            Framework.running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            exit()
            Framework.running = False
        elif event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
            x = event.x
            y = Framework.Window_H - event.y


def pause(): pass


def resume(): pass
