import Project_SceneFrameWork as FrameWork
import Scene000_Battle as Scn_Battle
import ObjectDate001_Actor as obj_Actor
import ObjectDate002_Monster as obj_Monster
import ObjectDate003_State as obj_State
import random

who = 0
Sel_Skill = 0
Sel_Monster = None
agro = 0
Timer = 0

def Whos_turn():
    for i in range(0, len(obj_Actor.actor), 1):
        if (obj_Actor.actor[i].Acgauge >= 100):
            obj_Actor.actor[i].myturn = 1
            return 1
    for i in range(0, 4, 1):
        if (obj_Monster.monster[i].Acgauge >= 100):
            obj_Monster.monster[i].myturn = 1
            return 1
    return 0


def AcgaugeUpdate():
    global who, Sel_Skill, Sel_Monster
    who = Whos_turn()
    if (Floor_end() != True):
        if (who == 0):
            for i in range(0, len(obj_Actor.actor), 1):
                if obj_Actor.actor[i].cur_state == obj_State.IdleState:
                    obj_Actor.actor[i].Acgauge += obj_Actor.actor[i].speed
            for i in range(0, len(obj_Monster.monster), 1):
                if obj_Monster.monster[i].state != 1:
                    obj_Monster.monster[i].Acgauge += obj_Monster.monster[i].speed
        if (who == 1):
            for i in range(0, len(obj_Actor.actor), 1):
                if (obj_Actor.actor[i].myturn == 1):
                    ActorAction(obj_Actor.actor[i])
                    print(str(i) + "플레이어의 턴")
            for i in range(0, 4, 1):
                if (obj_Monster.monster[i].myturn == 1):
                    MonsterAction(obj_Monster.monster[i])
                    print(str(i) + "몬스터의 턴")
    elif (Floor_end()):
            for i in range(0, len(obj_Actor.actor), 1):
                if obj_Actor.actor[i].cur_state != obj_State.DeadState and obj_Actor.actor[i].cur_state != obj_State.VictoryState:
                    obj_Actor.actor[i].cur_state = obj_State.VictoryState


def ActorAction(Actor):
    global Sel_Skill, Sel_Monster
    Sel_Skill = Skill_Sel(Scn_Battle.x, Scn_Battle.y, Sel_Skill)
    Sel_Monster = Monster_Target_Sel(Scn_Battle.x, Scn_Battle.y)
    if (Sel_Monster != None and obj_Monster.monster[Sel_Monster].state != 1):
        if (Actor.cur_state != obj_State.AttackState):
            Actor.event_que.append(obj_State.AttackState)
        '''
        obj_Monster.monster[Sel_Monster].hp -= Actor.atk
        print(str(Sel_Monster) + "몬스터의 체력 : " + str(obj_Monster.monster[Sel_Monster].hp))
        Actor.myturn = 0
        Actor.Acgauge = 0
        Sel_Skill = 0
        Sel_Monster = None
        '''

def MonsterAction(Monster):
    global agro
    while (True):
        temp = plat_lotto()
        if 0 <= temp and temp <= 40:
            agro = 0
        elif 40 <= temp and temp <= 65:
            agro = 1
        elif 65 <= temp and temp <= 90:
            agro = 2
        elif 90 <= temp and temp <= 100:
            agro = 3
        if (agro < len(obj_Actor.actor)):
            if (obj_Actor.actor[agro].cur_state != obj_State.DeadState):
                break
    if (obj_Actor.actor[agro].cur_state != obj_State.DeadState):
        obj_Actor.actor[agro].hp -= Monster.atk
        print(str(agro) + "플레이어의 체력 : " + str(obj_Actor.actor[agro].hp))
        Monster.myturn = 0
        Monster.Acgauge = 0

def Skill_Sel(x, y, Sel_Skill):
    for act in obj_Actor.actor:
        for i in range(0, 3):
            if Inpoint(act.skill[i], x, y):
                Scn_Battle.x = 0
                Scn_Battle.y = 0
                return act.skill[i].kind
    return Sel_Skill
    '''
    if (FrameWork.Window_W - (64 * 3) - 32 <= x and FrameWork.Window_W - (64 * 3) + 32 >= x and 64 - 32 <= y and 64 + 32 >= y):
        return 0
    if (FrameWork.Window_W - (64 * 2) - 32 <= x and FrameWork.Window_W - (64 * 2) + 32 >= x and 64 - 32 <= y and 64 + 32 >= y):
        return 1
    if (FrameWork.Window_W - (64 * 1) - 32 <= x and FrameWork.Window_W - (64 * 1) + 32 >= x and 64 - 32 <= y and 64 + 32 >= y):
        return 2
    return Sel_Skill
    '''

def Monster_Target_Sel(x, y):
    for mon in obj_Monster.monster:
        if Inpoint(mon, x, y):
            Scn_Battle.x = 0
            Scn_Battle.y = 0
            return mon.position
        '''
    if (350 - 32 <= x and 350 + 32 >= x and FrameWork.Window_H / 2 - 32 <= y and FrameWork.Window_H / 2 + 32 >= y):
        Scn_Battle.x = 0
        Scn_Battle.y = 0
        return 0
    if (250 - 32 <= x and 250 + 32 >= x and FrameWork.Window_H / 2 + 64 - 32 <= y and FrameWork.Window_H / 2 + 64 + 32 >= y):
        Scn_Battle.x = 0
        Scn_Battle.y = 0
        return 1
    if (250 - 32 <= 250 + 32 >= x and FrameWork.Window_H / 2 - 64 - 32 <= y and FrameWork.Window_H / 2 - 64 + 32 >= y):
        Scn_Battle.x = 0
        Scn_Battle.y = 0
        return 2
    if (150 - 32 <= 150 + 32 >= x and FrameWork.Window_H / 2 - 32 <= y and FrameWork.Window_H / 2 + 32 >= y):
        Scn_Battle.x = 0
        Scn_Battle.y = 0
        return 3
        '''

def Skill_Act(left, up):
    pass

def plat_lotto():
    num = random.randint(0, 100)
    return num




def Inpoint(a, x, y):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    if left_a > x:
        return False
    if right_a < x:
        return False
    if top_a < y:
        return False
    if bottom_a > y:
        return False
    return True

def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()
    if left_a > right_b:
        return False
    if right_a < left_b:
        return False
    if top_a < bottom_b:
        return False
    if bottom_a > top_b:
        return False
    return True

def Floor_end():
    for i in range (0, len(obj_Monster.monster), 1):
        if (obj_Monster.monster[i].state != 1):
            return False

    return True