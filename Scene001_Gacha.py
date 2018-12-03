import Project_SceneFrameWork as Framework
import ObjectDate001_Actor
import ObjectDate002_Monster
from pico2d import *
import Resource_Manager as rssmgr
import Scene000_Battle as Sc_Battle
import Scene002_Newhero as Sc_Newhero
import Scene003_Actor_Maneger as Sc_Acmgr
import ObjectDate004_Background as Obj_Background
import ObjectDate006_Player as Obj_Player
import game_world
import Resource
import Resource_Manager
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
    rssmgr.Upload_data()
    background = Obj_Background.Background(2)
    game_world.add_object(background, 0)
    if Obj_Player.player is None:
        Obj_Player.player = Obj_Player.Player()
    if rssmgr.Bgm.sound != rssmgr.battle_Bgm[2].sound:
        rssmgr.Bgm.sound.stop()
        rssmgr.Bgm.sound = rssmgr.battle_Bgm[2].sound
        rssmgr.Bgm.sound.repeat_play()


def exit():
    game_world.clear()


def update(frame_time):
    global frame_updater
    frame_updater += 1
    if (frame_updater > (Framework.FPS_TIME / 8.0)):
        pass


def draw(frame_time):
    clear_canvas()
    # weapon.clip_draw(96 * frame , 320 - 64 * 5, 96, 64, 100 + 48, 300 + 64)
    # weapon.clip_draw(96 * frame + 96 * 3, 320 - 64 * 5, 96, 64, 100 - 16, 300 + 64)
    for game_object in game_world.all_objects():
        game_object.draw()
    Resource_Manager.font[0].font.draw(50, 50, 'Gold: %d' % Resource.Money, (0, 0, 0))
    Resource_Manager.font[0].font.draw(Framework.Window_W / 2 - 300, Framework.Window_H / 2, 'T를 눌러 뽑기를 해주세요!', (0, 0, 0))
    Resource_Manager.font[0].font.draw(Framework.Window_W / 2 - 300, Framework.Window_H / 2 - 24, 'R를 눌러 연속으로 뽑기를 진행할 수 있어요!', (0, 0, 0))
    update_canvas()


def handle_events(frame_time):
    global x, y, prees_t
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            exit()
            Framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            exit()
            Framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_t:
            if Resource.Money > 0:
                Sc_Newhero.gacha_times = 1
                Sc_Newhero.gachatemp = []
                Framework.push_state(Sc_Newhero)

        elif event.type == SDL_KEYDOWN and event.key == SDLK_r:
            if Resource.Money > 0:
                Sc_Newhero.gacha_times = Resource.Money
                Sc_Newhero.gachatemp = []
                Framework.push_state(Sc_Newhero)

        elif event.type == SDL_KEYDOWN and event.key == SDLK_1:
            game_world.clear()
            Framework.change_state(Sc_Battle)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_2:
            game_world.clear()
            Framework.change_state(Sc_Acmgr)
    pass


def pause(): pass


def resume(): pass
