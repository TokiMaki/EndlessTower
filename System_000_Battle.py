import Project_SceneFrameWork as FrameWork
import Scene000_Battle as Scn_Battle
import ObjectDate001_Actor as obj_Actor
import ObjectDate002_Monster as obj_Monster
import ObjectDate003_State as obj_State
import ObjectDate005_Effect as obj_Effect
import random

who = 0
Sel_Skill = 0
Sel_Monster = None
agro = 0
Timer = 0

def turn_check():
    for i in range(0, len(obj_Actor.hero), 1):
        if (obj_Actor.hero[i].Acgauge >= 100):
            obj_Actor.hero[i].myturn = 1

    if (obj_Monster.monster.Acgauge >= 100):
        obj_Monster.monster.myturn = 1

    return 0

def All_Die():
    for i in range(0, len(obj_Actor.hero), 1):
        if obj_Actor.hero[i].cur_state != obj_State.DeadState:
            return False
    return True


def AcgaugeUpdate():
    global who, Sel_Skill, Sel_Monster
    turn_check()
    if (Floor_end() != True and All_Die() != True):

            for i in range(0, len(obj_Actor.hero), 1):
                if obj_Actor.hero[i].cur_state == obj_State.IdleState:
                    obj_Actor.hero[i].Acgauge += obj_Actor.hero[i].speed

            if obj_Monster.monster.state != 1:
                obj_Monster.monster.Acgauge += obj_Monster.monster.speed

            for i in range(0, len(obj_Actor.hero), 1):
                if (obj_Actor.hero[i].myturn == 1):
                    ActorAction(obj_Actor.hero[i])
                    print(str(i) + "플레이어의 턴")

            if (obj_Monster.monster.myturn == 1):
                MonsterAction(obj_Monster.monster)
                print("몬스터의 턴")

    elif (Floor_end()):
            for i in range(0, len(obj_Actor.hero), 1):
                if obj_Actor.hero[i].cur_state != obj_State.DeadState and obj_Actor.hero[i].cur_state != obj_State.VictoryState:
                    obj_Actor.hero[i].cur_state = obj_State.VictoryState


def ActorAction(Actor):
    global Sel_Skill, Sel_Monster
    # Sel_Skill = Skill_Sel(Scn_Battle.x, Scn_Battle.y, Sel_Skill)
    # Sel_Monster = Monster_Target_Sel(Sel_Monster, Scn_Battle.x, Scn_Battle.y)
        #if (Actor.cur_state != obj_State.BasicAttackState):
    if(Actor.cur_state == obj_State.IdleState):
        Actor.target = 0
        '''
        if (Actor.skill[1].cooltime > Actor.skill[1].skillturn):
            Actor.event_que.append(Skill_Kind(Actor.skill[0].updown_num, Actor.skill[0].left_num))
            Actor.skill[1].skillturn += 1
        else:
        '''
        Actor.now_skill = 1
        Actor.event_que.append(Skill_Kind(Actor.skill[1].updown_num, Actor.skill[1].left_num))
        Actor.skill[1].skillturn = 0
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
    if (Monster.stage == 5):
        for i in range(0, 5):
            while (True):
                agro = random.randint(0, len(obj_Actor.hero) - 1)
                if (obj_Actor.hero[agro].cur_state != obj_State.DeadState):
                    Monster.effect.append(obj_Effect.Mon_Effect(agro, 7, Monster.atk))
                    break

    else:
        while (True):
            agro = random.randint(0, len(obj_Actor.hero) - 1)
            if (obj_Actor.hero[agro].cur_state != obj_State.DeadState):
                Monster.effect.append(obj_Effect.Mon_Effect(agro, 0, Monster.atk))
                break
    if (obj_Actor.hero[agro].cur_state != obj_State.DeadState):
        obj_Actor.hero[agro].hp -= Monster.atk
        print(str(agro) + "플레이어의 체력 : " + str(obj_Actor.hero[agro].hp))
        Monster.myturn = 0
        Monster.Acgauge = 0

def Skill_Sel(x, y, Sel_Skill):
    for act in obj_Actor.hero:
        for i in range(0, 2):
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

def Skill_Kind(Skill_updown, Skill_left):
    for i in range(0, 6, 1):
        if (Skill_updown == obj_State.BasicAttack_Skill_Kind[i][0] and Skill_left == obj_State.BasicAttack_Skill_Kind[i][1]):
            return obj_State.BasicAttackState
    for i in range(0, 5, 1):
        if (Skill_updown == obj_State.Magic_Skill_Kind[i][0] and Skill_left == obj_State.Magic_Skill_Kind[i][1]):
            return obj_State.MagicState


def Monster_Target_Sel(Sel_Monster, x, y):
    for mon in obj_Monster.monster:
        if Inpoint(mon, x, y):
            Scn_Battle.x = 0
            Scn_Battle.y = 0
            return mon.position
    return Sel_Monster

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
    if (obj_Monster.monster.state == 0):
        return False

    return True