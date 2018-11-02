from pico2d import *
import ObjectDate001_Actor as Obj_Actor
import ObjectDate003_State as Obj_State
import game_world
import Project_SceneFrameWork as Framework
import Resource_Manager as rssmgr

space = 0

def enter():
    for i in range(0, len(Obj_Actor.hero), 1):
        game_world.add_object(Obj_Actor.hero[i], 1)


def exit():
    game_world.clear()


def update(frame_time):
    for game_object in game_world.all_objects():
        game_object.update(frame_time)


def draw(frame_time):
    clear_canvas()
    if (len(Obj_Actor.hero) - 8 * space >= 8):
        for i in range(0 + space * 8, 0 + space * 8 + 8, 1):
            rssmgr.Actor[Obj_Actor.hero[i].actor_num].image.clip_draw(48 * Obj_Actor.hero[i].frame + (48 * 3) * (Obj_Actor.hero[i].actor_in_num % 4),
                                                                      (48 * 7) - (48 * 4) * int((Obj_Actor.hero[i].actor_in_num / 4)), 48, 48, Framework.Window_W - (Framework.Window_W / 8 * int(i % 2)), Framework.Window_H - (Framework.Window_H / 4 * int(i / 2)))
    else:
        for i in range(0 + space * 8, len(Obj_Actor.hero), 1):
            rssmgr.Actor[Obj_Actor.hero[i].actor_num].image.clip_draw(48 * Obj_Actor.hero[i].frame + (48 * 3) * (Obj_Actor.hero[i].actor_in_num % 4),
                                                                      (48 * 7) - (48 * 4) * int((Obj_Actor.hero[i].actor_in_num / 4)), 48, 48, Framework.Window_W - (Framework.Window_W / 8 * int(i % 2)), Framework.Window_H - (Framework.Window_H / 4 * int(i / 2)))

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
