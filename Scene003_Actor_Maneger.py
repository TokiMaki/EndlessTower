from pico2d import *
import ObjectDate001_Actor as Obj_Actor
import ObjectDate003_State as Obj_State
import ObjectDate004_Background as Obj_Background
import Scene001_Gacha as Sc_Gacha
import game_world
import Project_SceneFrameWork as Framework
import Resource_Manager as rssmgr

space = 0
sel = None
x, y = 0, 0

def enter():
    for i in range(0, len(Obj_Actor.hero), 1):
        game_world.add_object(Obj_Actor.hero[i], 1)

    background = Obj_Background.Background(1)
    game_world.add_object(background, 0)



def exit():
    game_world.clear()


def update(frame_time):
    global x, y, sel

    for game_object in game_world.all_objects():
        game_object.update(frame_time)

    sel = point_in_rect(x, y)


def draw(frame_time):
    global sel
    clear_canvas()

    for game_object in game_world.background_objects():
        game_object.draw()

    if (len(Obj_Actor.hero) - 10 * space >= 10):
        for i in range(0 + space * 10, 0 + space * 10 + 10, 1):
            rssmgr.Actor[Obj_Actor.hero[i].actor_num].image.clip_draw(48 * int(Obj_Actor.hero[i].frame) + (48 * 3) * (Obj_Actor.hero[i].actor_in_num % 4),
                                                                      (48 * 7) - (48 * 4) * int((Obj_Actor.hero[i].actor_in_num / 4)), 48, 48,
                                                                      Framework.Window_W / 8 * 6 + (Framework.Window_W / 8 * int((i - 10 * space)  % 2)), Framework.Window_H / 6 * 5 - (Framework.Window_H / 6 * int((i - 10 * space) / 2)))
    else:
        for i in range(0 + space * 10, len(Obj_Actor.hero), 1):
            rssmgr.Actor[Obj_Actor.hero[i].actor_num].image.clip_draw(48 * int(Obj_Actor.hero[i].frame) + (48 * 3) * (Obj_Actor.hero[i].actor_in_num % 4),
                                                                      (48 * 7) - (48 * 4) * int((Obj_Actor.hero[i].actor_in_num / 4)), 48, 48,
                                                                      Framework.Window_W / 8 * 6 + (Framework.Window_W / 8 * int((i - 10 * space) % 2)), Framework.Window_H / 6 * 5 - (Framework.Window_H / 6 * int((i - 10 * space) / 2)))

    if (sel != None):
        rssmgr.Skill_sel.image.clip_draw(0, 0, 32, 32, Framework.Window_W / 8 * 6 + (Framework.Window_W / 8 * int(sel % 2)), Framework.Window_H / 6 * 5 - (Framework.Window_H / 6 * int(sel / 2)), 64, 64)

        rssmgr.font[0].font.draw(Framework.Window_W / 10 * 1, Framework.Window_H / 2 + 24 * 2 + 24 * 1,
                                 '레벨: %d' % Obj_Actor.hero[sel + space * 10].level, (0, 128, 0))
        rssmgr.font[0].font.draw(Framework.Window_W / 10 * 1, Framework.Window_H / 2 + 24 * 2 - 24 * 0, '체력: %d' % Obj_Actor.hero[sel + space * 10].maxhp, (128, 0, 0))
        rssmgr.font[0].font.draw(Framework.Window_W / 10 * 1, Framework.Window_H / 2 + 24 * 2 - 24 * 1, '공격력: %d' % Obj_Actor.hero[sel + space * 10].atk, (0, 0, 0))
        rssmgr.font[0].font.draw(Framework.Window_W / 10 * 1, Framework.Window_H / 2 + 24 * 2 - 24 * 2, '속도: %d' % Obj_Actor.hero[sel + space * 10].speed, (0, 0, 0))

        if (Obj_Actor.hero[sel + space * 10].job == 0):
            rssmgr.font[0].font.draw(Framework.Window_W / 10 * 1, Framework.Window_H / 2 + 24 * 2 - 24 * 3, '클래스: 전사',
                                  (0, 0, 128))
        if (Obj_Actor.hero[sel + space * 10].job == 1):
            rssmgr.font[0].font.draw(Framework.Window_W / 10 * 1, Framework.Window_H / 2 + 24 * 2 - 24 * 3, '클래스: 도적',
                                  (0, 0, 128))
        if (Obj_Actor.hero[sel + space * 10].job == 2):
            rssmgr.font[0].font.draw(Framework.Window_W / 10 * 1, Framework.Window_H / 2 + 24 * 2 - 24 * 3, '클래스: 마법사',
                                  (0, 0, 128))
        if (Obj_Actor.hero[sel + space * 10].job == 3):
            rssmgr.font[0].font.draw(Framework.Window_W / 10 * 1, Framework.Window_H / 2 + 24 * 2 - 24 * 3, '클래스: 사제',
                                  (0, 0, 128))

    if (Obj_Actor.actor != None):
        for i in range (0, len(Obj_Actor.actor), 1):
            if (Obj_Actor.actor[i] != []):
                rssmgr.Actor1[Obj_Actor.actor[i].actor_num][Obj_Actor.actor[i].actor_in_num].image.clip_draw(64 * int(Obj_Actor.hero[i].frame), 320 - 64 * 0, 64, 64, Obj_Actor.actor[i].x - 400, Obj_Actor.actor[i].y)

    update_canvas()


def handle_events(frame_time):
    global x, y, space
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            exit()
            Framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            exit()
            Framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_2:
            Framework.change_state(Sc_Gacha)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_LEFT:
            if (space > 0):
                space -= 1
        elif event.type == SDL_KEYDOWN and event.key == SDLK_RIGHT:
            if (len(Obj_Actor.hero) - 10 * space >= 10):
                space += 1
        elif event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
            x = event.x
            y = Framework.Window_H - event.y
            print('(x: %f, y: %f)' % (x, y))


def pause(): pass


def resume(): pass


def point_in_rect(x, y):
    if (len(Obj_Actor.hero) - 10 * space >= 10):
        for i in range(0, 10, 1):
            if (Framework.Window_W / 8 * 6 + (Framework.Window_W / 8 * int(i % 2)) - Framework.Window_W / 16 < x and
                    Framework.Window_W / 8 * 6 + (Framework.Window_W / 8 * int(i % 2)) + Framework.Window_W / 16 > x and
                    Framework.Window_H / 6 * 5 - (Framework.Window_H / 6 * int(i / 2)) - Framework.Window_H / 12 < y and
                    Framework.Window_H / 6 * 5 - (Framework.Window_H / 6 * int(i / 2)) + Framework.Window_H / 12 > y):
                return i
    else:
        for i in range(0, len(Obj_Actor.hero) - 10 * space, 1):
            if (Framework.Window_W / 8 * 6 + (Framework.Window_W / 8 * int(i % 2)) - Framework.Window_W / 16 < x and
                    Framework.Window_W / 8 * 6 + (Framework.Window_W / 8 * int(i % 2)) + Framework.Window_W / 16 > x and
                    Framework.Window_H / 6 * 5 - (Framework.Window_H / 6 * int(i / 2)) - Framework.Window_H / 12 < y and
                    Framework.Window_H / 6 * 5 - (Framework.Window_H / 6 * int(i / 2)) + Framework.Window_H / 12 > y):
                return i
    return None

'''
def point_in_Actor(x, y, actor):
    if (650 - 400 - 64 < x and
            650 - 400 + 64 > x and
            Framework.Window_H / 2 - 64 < y and
            Framework.Window_H / 2 + 64 > y):

        if (Obj_Actor.actor != None):
            for i in range(0, len(Obj_Actor.actor), 1):
                if Obj_Actor.actor[i].position == 0 or Obj_Actor.actor[i] == actor:
                    Obj_Actor.actor.remove(Obj_Actor.actor[i])
                    break

        actor.position = 0
        Obj_Actor.actor.append(actor)

    if (750 - 400 - 64 < x and
            750 - 400 + 64 > x and
            Framework.Window_H / 2 + 64 - 64 < y and
            Framework.Window_H / 2 + 64 + 64 > y):
        if (Obj_Actor.actor != None):
            for i in range(0, len(Obj_Actor.actor), 1):
                if Obj_Actor.actor[i].position == 1 or Obj_Actor.actor[i] == actor:
                    Obj_Actor.actor.remove(Obj_Actor.actor[i])
                    break

        actor.position = 1
        Obj_Actor.actor.append(actor)
    if (750 - 400 - 64 < x and
            750 - 400 + 64 > x and
            Framework.Window_H / 2 - 64 - 64 < y and
            Framework.Window_H / 2 - 64 + 64 > y):
        if (Obj_Actor.actor != None):
            for i in range(0, len(Obj_Actor.actor), 1):
                if Obj_Actor.actor[i].position == 2 or Obj_Actor.actor[i] == actor:
                    Obj_Actor.actor.remove(Obj_Actor.actor[i])
                    break

        actor.position = 2
        Obj_Actor.actor.append(actor)
    if (850 - 400 - 64 < x and
            850 - 400 + 64 > x and
            Framework.Window_H / 2 - 64 < y and
            Framework.Window_H / 2 + 64 > y):
        if (Obj_Actor.actor != None):
            for i in range(0, len(Obj_Actor.actor), 1):
                if Obj_Actor.actor[i].position == 3 or Obj_Actor.actor[i] == actor:
                    Obj_Actor.actor.remove(Obj_Actor.actor[i])
                    break

        actor.position = 3
        Obj_Actor.actor.append(actor)

    actor.position_set()
'''