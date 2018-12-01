import Project_SceneFrameWork as Framework
import ObjectDate001_Actor
import ObjectDate002_Monster
import ObjectDate004_Background as Obj_Background
from pico2d import *
import Scene001_Gacha as Sc_Gacha
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

    ObjectDate002_Monster.monster = ObjectDate002_Monster.Monster()
    ObjectDate002_Monster.monster.speed = random.randint(10, 15)
    game_world.add_object(ObjectDate002_Monster.monster, 1)

    for i in range(0, len(ObjectDate001_Actor.hero), 1):
        ObjectDate001_Actor.actor.append(ObjectDate001_Actor.hero[i])
    for i in range (0 ,len(ObjectDate001_Actor.actor), 1):
        game_world.add_object(ObjectDate001_Actor.actor[i], 1)

    for act in ObjectDate001_Actor.actor:
        act.Acgauge = random.randint(0, 30)
        act.hp = act.maxhp
        act.position_set()

    ObjectDate002_Monster.monster.position_set()

    background = Obj_Background.Background(0)
    game_world.add_object(background, 0)

    Sys_Battle.Sel_Skill = 0


def exit():
    game_world.clear()


def update(frame_time):
    for game_object in game_world.all_objects():
        game_object.update(frame_time)
    Sys_Battle.AcgaugeUpdate()
    if (Sys_Battle.All_Die()):
        Framework.change_state(Sc_Gacha)


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
