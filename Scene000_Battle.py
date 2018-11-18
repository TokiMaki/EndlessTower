import Project_SceneFrameWork as Framework
import ObjectDate001_Actor
import ObjectDate002_Monster
import ObjectDate004_Background as Obj_Background
from pico2d import *
import Resource_Manager as rssmgr
import System_000_Battle as Sys_Battle
import random
import game_world

# 무기를 쥐어줄때는 원 좌표에서 16을 빼야됨

name = "Battle"
weapon = None
user = None
frame = 0
frame_tog = 1
x = 0
y = 0
floor = 0


def enter():
    global weapon
    # open_canvas(Framework.Window_W, Framework.Window_H)
    rssmgr.Upload_data()
    ObjectDate002_Monster.monster = [ObjectDate002_Monster.Monster() for i in range(4)]
    for i in range (0 ,len(ObjectDate001_Actor.actor), 1):
            ObjectDate001_Actor.actor[i].Acgauge = 0
            game_world.add_object(ObjectDate001_Actor.actor[i], 1)

    for act in ObjectDate001_Actor.actor:
        act.position_set()


    for i in range(0, 4, 1):
        ObjectDate002_Monster.monster[i].position = i
        ObjectDate002_Monster.monster[i].speed = random.randint(5, 10)
        game_world.add_object(ObjectDate002_Monster.monster[i], 1)

    for mon in ObjectDate002_Monster.monster:
        mon.position_set()

    background = Obj_Background.Background(0)
    game_world.add_object(background, 0)

    Sys_Battle.Sel_Skill = 0


def exit():
    game_world.clear()
    close_canvas()


def update(frame_time):
    for game_object in game_world.all_objects():
        game_object.update(frame_time)
    Sys_Battle.AcgaugeUpdate()


def draw(frame_time):
    clear_canvas()
    # weapon.clip_draw(96 * frame , 320 - 64 * 5, 96, 64, 100 + 48, 300 + 64)
    # weapon.clip_draw(96 * frame + 96 * 3, 320 - 64 * 5, 96, 64, 100 - 16, 300 + 64)
    for game_object in game_world.all_objects():
        game_object.draw()

    update_canvas()


def handle_events(frame_time):
    global x, y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            exit()
            Framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            exit()
            Framework.quit()
        elif event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
            x = event.x
            y = Framework.Window_H - event.y


def pause(): pass


def resume(): pass
