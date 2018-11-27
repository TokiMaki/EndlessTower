import Project_SceneFrameWork as Framework
import ObjectDate001_Actor as Obj_Actor
import ObjectDate003_State as Obj_State
from pico2d import *
import Resource_Manager as rssmgr
import Resource
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

framebool = Obj_State.FRAMES_PER_ACTION * Obj_State.ACTION_PER_TIME

warrior_skill_list = [[14, 1], [15, 7]]
rogue_skill_list = [[14, 9], [14, 8], [14, 7]]
magician_skill_list = [[15, 0], [15, 1], [15, 2]]
cleric_skill_list = [[14, 5], [14, 4]]

def enter():
    global gachahero
    random_temp = 0
    Sys_Battle.Sel_Skill = 4
    gachahero = Obj_Actor.Actor()
    gachahero.grade = random.randint(3, 5)
    gachahero.job = 0
    gachahero.actor_num = random.randint(0, 2)
    gachahero.actor_in_num = random.randint(0, 7)
    gachahero.job = random.randint(0, 3)
    gachahero.skill[0].kind = 0
    gachahero.skill[0].updown_num = 15
    gachahero.skill[0].left_num = 12


    if (gachahero.job == 0):
        gachahero.hp = random.randint(17, 20)
        gachahero.atk = random.randint(3, 5)
        gachahero.speed = random.randint(5, 6)
        random_temp = random.randint(0, len(warrior_skill_list) - 1)
        gachahero.skill[1].kind = 1
        gachahero.skill[1].updown_num = warrior_skill_list[random_temp][0]
        gachahero.skill[1].left_num = warrior_skill_list[random_temp][1]

    if (gachahero.job == 1):
        gachahero.hp = random.randint(10, 13)
        gachahero.atk = random.randint(5, 7)
        gachahero.speed = random.randint(7, 9)
        random_temp = random.randint(0, len(rogue_skill_list) - 1)
        gachahero.skill[1].kind = 1
        gachahero.skill[1].updown_num = rogue_skill_list[random_temp][0]
        gachahero.skill[1].left_num = rogue_skill_list[random_temp][1]
    if (gachahero.job == 2):
        gachahero.hp = random.randint(8, 12)
        gachahero.atk = random.randint(5, 7)
        gachahero.speed = random.randint(6, 7)
        random_temp = random.randint(0, len(magician_skill_list) - 1)
        gachahero.skill[1].kind = 1
        gachahero.skill[1].updown_num = magician_skill_list[random_temp][0]
        gachahero.skill[1].left_num = magician_skill_list[random_temp][1]
    if (gachahero.job == 3):
        gachahero.hp = random.randint(8, 12)
        gachahero.atk = random.randint(2, 4)
        gachahero.speed = random.randint(5, 6)
        random_temp = random.randint(0, len(cleric_skill_list) - 1)
        gachahero.skill[1].kind = 1
        gachahero.skill[1].updown_num = cleric_skill_list[random_temp][0]
        gachahero.skill[1].left_num = cleric_skill_list[random_temp][1]
    Obj_Actor.hero.append(gachahero)


def exit():
    pass


def update(frame_time):
    global frame, framebool
    frame += (framebool * Framework.frame_time)
    if (frame >= 3):
        frame = 2.99
        framebool = -Obj_State.FRAMES_PER_ACTION * Obj_State.ACTION_PER_TIME
    if (frame <= 0):
        framebool = Obj_State.FRAMES_PER_ACTION * Obj_State.ACTION_PER_TIME
    pass


def draw(frame_time):
    global frame, gachahero
    clear_canvas()
    rssmgr.Actor[gachahero.actor_num].image.clip_draw(48 * int(frame) + (48 * 3) * (gachahero.actor_in_num % 4), (48 * 7) - (48 * 4) * int((gachahero.actor_in_num / 4)), 48, 48, Framework.Window_W / 4, Framework.Window_H / 2, 64, 64)
    rssmgr.font.font.draw(50, 50, '(Gold: %d)' % Resource.Money, (0, 0, 0))
    rssmgr.font.font.draw(Framework.Window_W / 4 * 3, Framework.Window_H / 2 + 20 * 2 - 20 * 0, '체력: %d' % gachahero.hp, (0, 0, 0))
    rssmgr.font.font.draw(Framework.Window_W / 4 * 3, Framework.Window_H / 2 + 20 * 2 - 20 * 1, '공격력: %d' % gachahero.atk, (0, 0, 0))
    rssmgr.font.font.draw(Framework.Window_W / 4 * 3, Framework.Window_H / 2 + 20 * 2 - 20 * 2, '속도: %d' % gachahero.speed, (0, 0, 0))
    if (gachahero.job == 0):
        rssmgr.font.font.draw(Framework.Window_W / 4 * 3, Framework.Window_H / 2 + 20 * 2 - 20 * 3, '클래스: 전사', (0, 0, 0))
    if (gachahero.job == 1):
        rssmgr.font.font.draw(Framework.Window_W / 4 * 3, Framework.Window_H / 2 + 20 * 2 - 20 * 3, '클래스: 도적', (0, 0, 0))
    if (gachahero.job == 2):
        rssmgr.font.font.draw(Framework.Window_W / 4 * 3, Framework.Window_H / 2 + 20 * 2 - 20 * 3, '클래스: 마법사', (0, 0, 0))
    if (gachahero.job == 3):
        rssmgr.font.font.draw(Framework.Window_W / 4 * 3, Framework.Window_H / 2 + 20 * 2 - 20 * 3, '클래스: 사제', (0, 0, 0))
    for i in range(0, 2):
        gachahero.skill[i].draw()
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
