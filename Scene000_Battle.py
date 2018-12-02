import Project_SceneFrameWork as Framework
import ObjectDate001_Actor
import ObjectDate002_Monster
import ObjectDate004_Background as Obj_Background
from pico2d import *
import Scene001_Gacha as Sc_Gacha
import ObjectDate003_State as Obj_State
import Resource_Manager as rssmgr
import System_000_Battle as Sys_Battle
import Resource
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
now_stage = 1
rest_hero = 0


def enter():
    # open_canvas(Framework.Window_W, Framework.Window_H)
    rssmgr.Upload_data()

    ObjectDate002_Monster.monster = ObjectDate002_Monster.Monster()
    ObjectDate002_Monster.monster.maxhp = 1300 + int(1300 * (0.3 * now_stage))
    ObjectDate002_Monster.monster.hp = ObjectDate002_Monster.monster.maxhp
    ObjectDate002_Monster.monster.atk = random.randint(5, 6) + int(random.randint(5, 6) * (0.3 * now_stage))
    ObjectDate002_Monster.monster.speed = random.randint(5, 7) + int(random.randint(2, 3) * (0.2 * now_stage))
    game_world.add_object(ObjectDate002_Monster.monster, 1)

    for i in range (0 ,len(ObjectDate001_Actor.hero), 1):
        game_world.add_object(ObjectDate001_Actor.hero[i], 1)

    for act in ObjectDate001_Actor.hero:
        act.Acgauge = random.randint(0, 50)
        act.hp = act.maxhp
        act.cur_state = Obj_State.IdleState
        act.position_set()

    ObjectDate002_Monster.monster.position_set()

    background = Obj_Background.Background(0)
    game_world.add_object(background, 0)

    Sys_Battle.Sel_Skill = 0


def exit():
    game_world.clear()


def update(frame_time):
    global rest_hero
    for game_object in game_world.all_objects():
        game_object.update(frame_time)
    Sys_Battle.AcgaugeUpdate()
    rest_hero = 0
    for act in ObjectDate001_Actor.hero:
        if (act.cur_state != Obj_State.DeadState):
            rest_hero += 1


def draw(frame_time):
    global now_stage
    clear_canvas()
    # weapon.clip_draw(96 * frame , 320 - 64 * 5, 96, 64, 100 + 48, 300 + 64)
    # weapon.clip_draw(96 * frame + 96 * 3, 320 - 64 * 5, 96, 64, 100 - 16, 300 + 64)
    for game_object in game_world.all_objects():
        game_object.draw()
    if (Sys_Battle.Floor_end() == False and Sys_Battle.All_Die() == False):
        rssmgr.font[0].font.draw(Framework.Window_W / 4, Framework.Window_H / 7,
                                 '남은 영웅의 수 : %d' % (rest_hero),
                                 (0, 216, 255))
        rssmgr.font[0].font.draw(Framework.Window_W / 2, Framework.Window_H / 8 * 7,
                                 '%d' % (ObjectDate002_Monster.monster.hp),
                                 (255, 0, 0))
    if (Sys_Battle.Floor_end()):
        rssmgr.font[0].font.draw(Framework.Window_W / 4, Framework.Window_H / 7, '처치완료! %d의 골드를 획득하였습니다.' % (now_stage * 5),
                                 (0, 216, 255))
        rssmgr.font[0].font.draw(Framework.Window_W / 4, Framework.Window_H / 7 - 30, '%d의 경험치를 획득하였습니다.' % (now_stage),
                                 (0, 216, 255))
        rssmgr.font[0].font.draw(Framework.Window_W / 4, Framework.Window_H / 7 - 60, '마우스 좌클릭을 눌러주세요',
                                 (0, 216, 255))
    if (Sys_Battle.All_Die()):
        rssmgr.font[0].font.draw(Framework.Window_W / 4, Framework.Window_H / 7, '이런! 모든 영웅이 죽었습니다.',
                                 (0, 216, 255))
        rssmgr.font[0].font.draw(Framework.Window_W / 4, Framework.Window_H / 7 - 30, '%d의 골드를 획득하였습니다.' % (now_stage * 3 * ((ObjectDate002_Monster.monster.maxhp - ObjectDate002_Monster.monster.hp) / ObjectDate002_Monster.monster.maxhp)),
                                 (0, 216, 255))
        rssmgr.font[0].font.draw(Framework.Window_W / 4, Framework.Window_H / 7 - 60, '마우스 좌클릭을 눌러주세요',
                                 (0, 216, 255))

    update_canvas()


def handle_events(frame_time):
    global x, y, now_stage
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
            if (Sys_Battle.Floor_end()):
                for act in ObjectDate001_Actor.hero:
                    act.exp += now_stage
                Resource.Money += now_stage * 5
                now_stage += 1
                Framework.change_state(Sc_Gacha)
            if (Sys_Battle.All_Die()):
                Resource.Money += int(now_stage * 3 * ((ObjectDate002_Monster.monster.maxhp - ObjectDate002_Monster.monster.hp) / ObjectDate002_Monster.monster.maxhp))
                Framework.change_state(Sc_Gacha)

        elif event.type == SDL_KEYDOWN and event.key == SDLK_1:
            Framework.change_state(Sc_Gacha)




def pause(): pass


def resume(): pass
