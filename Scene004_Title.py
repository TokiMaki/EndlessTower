import Project_SceneFrameWork as Framework
import ObjectDate001_Actor
import ObjectDate002_Monster
import ObjectDate004_Background as Obj_Background
from pico2d import *
import Scene001_Gacha as Sc_Gacha
import ObjectDate003_State as Obj_State
import Resource_Manager as rssmgr
import System_000_Battle as Sys_Battle
import random
import game_world

# 무기를 쥐어줄때는 원 좌표에서 16을 빼야됨

name = "Battle"
weapon = None
user = None
frame = 0
frame_bool = 20


def enter():
    # open_canvas(Framework.Window_W, Framework.Window_H)
    rssmgr.Upload_data()
    background = Obj_Background.Background(3)
    game_world.add_object(background, 0)



def exit():
    game_world.clear()


def update(frame_time):
    global frame, frame_bool
    for game_object in game_world.all_objects():
        game_object.update(frame_time)
    frame += frame_bool * Framework.frame_time
    if (frame > 10):
        frame_bool *= -1
    if (frame < -10):
        frame_bool *= -1


def draw(frame_time):
    clear_canvas()
    # weapon.clip_draw(96 * frame , 320 - 64 * 5, 96, 64, 100 + 48, 300 + 64)
    # weapon.clip_draw(96 * frame + 96 * 3, 320 - 64 * 5, 96, 64, 100 - 16, 300 + 64)
    for game_object in game_world.all_objects():
        game_object.draw()
    rssmgr.font[1].font.draw(Framework.Window_W / 2 - 300, Framework.Window_H / 8 * 7, '매니매니 히어로즈', (0, 0, 0))
    rssmgr.font[2].font.draw(Framework.Window_W / 2 - 300 + frame, Framework.Window_H / 8 * 1, '마우스 좌클릭을 눌러주세요', (255, 228, 0))

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
            Framework.change_state(Sc_Gacha)


def pause(): pass


def resume(): pass
