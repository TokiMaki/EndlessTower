from pico2d import *

Actor = None
Actor1 = None
Monster = None
Weapon = None
Skill = None
Skill_sel = None
font = None
battle_background = None
actor_maneger_background = None

def Upload_data():
    global Actor, Actor1, Monster, Skill, Skill_sel, font, battle_background, actor_maneger_background, Weapon
    if Actor is None:
        Actor = [Actor1_sound_data() for i in range(3)]
        Actor[0].image = load_image('Resource\\Actor\\Actor1.png')
        Actor[1].image = load_image('Resource\\Actor\\Actor2.png')
        Actor[2].image = load_image('Resource\\Actor\\Actor4.png')


    if Actor1 is None:
        Actor1 = [[], [], []]
        for i in range (0, 3, 1):
            Actor1[i] = [Actor1_sound_data() for j in range(8)]

        Actor1[0][0].image = load_image('Resource\\Actor\\Actor1_1.png')
        Actor1[0][1].image = load_image('Resource\\Actor\\Actor1_2.png')
        Actor1[0][2].image = load_image('Resource\\Actor\\Actor1_3.png')
        Actor1[0][3].image = load_image('Resource\\Actor\\Actor1_4.png')
        Actor1[0][4].image = load_image('Resource\\Actor\\Actor1_5.png')
        Actor1[0][5].image = load_image('Resource\\Actor\\Actor1_6.png')
        Actor1[0][6].image = load_image('Resource\\Actor\\Actor1_7.png')
        Actor1[0][7].image = load_image('Resource\\Actor\\Actor1_8.png')
        Actor1[1][0].image = load_image('Resource\\Actor\\Actor2_1.png')
        Actor1[1][1].image = load_image('Resource\\Actor\\Actor2_2.png')
        Actor1[1][2].image = load_image('Resource\\Actor\\Actor2_3.png')
        Actor1[1][3].image = load_image('Resource\\Actor\\Actor2_4.png')
        Actor1[1][4].image = load_image('Resource\\Actor\\Actor2_5.png')
        Actor1[1][5].image = load_image('Resource\\Actor\\Actor2_6.png')
        Actor1[1][6].image = load_image('Resource\\Actor\\Actor2_7.png')
        Actor1[1][7].image = load_image('Resource\\Actor\\Actor2_8.png')
        Actor1[2][0].image = load_image('Resource\\Actor\\Actor4_1.png')
        Actor1[2][1].image = load_image('Resource\\Actor\\Actor4_2.png')
        Actor1[2][2].image = load_image('Resource\\Actor\\Actor4_3.png')
        Actor1[2][3].image = load_image('Resource\\Actor\\Actor4_4.png')
        Actor1[2][4].image = load_image('Resource\\Actor\\Actor4_5.png')
        Actor1[2][5].image = load_image('Resource\\Actor\\Actor4_6.png')
        Actor1[2][6].image = load_image('Resource\\Actor\\Actor4_7.png')
        Actor1[2][7].image = load_image('Resource\\Actor\\Actor4_8.png')

    if Weapon is None:
        Weapon = Weapon_sound_data()
        Weapon.image = load_image('Resource\\Actor\\Weapons1.png')

    if Monster is None:
        Monster = [Monster_sound_data() for i in range(2)]
        Monster[0].image = load_image('Resource\\Monster\\Monster.png')
        Monster[1].image = load_image('Resource\\Monster\\Damage3.png')

    if battle_background is None:
        battle_background = [image_data() for i in range(3)]
        battle_background[0].image = load_image('Resource\\background\\Cobblestones3.png')
        battle_background[1].image = load_image('Resource\\background\\Cobblestones4.png')
        battle_background[2].image = load_image('Resource\\background\\Cobblestones5.png')

    if actor_maneger_background is None:
        actor_maneger_background = [image_data() for i in range(2)]
        actor_maneger_background[0].image = load_image('Resource\\background\\Castle1.png')
        actor_maneger_background[1].image = load_image('Resource\\background\\Town5.png')

    if Skill is None:
        Skill = Skill_sound_date()
        Skill.image = load_image('Resource\\Skill\\IconSet.png')

    if Skill_sel is None:
        Skill_sel = image_data()
        Skill_sel.image = load_image('Resource\\Skill\\skill_sel.png')

    if font is None:
        font = font_date()
        font.font = load_font('Resource\\Font\\malgunbd.TTF', 16)


class image_data():
    def __init__(self):
        self.image = None

class Actor1_sound_data(image_data):
    def __init__(self):
        super(Actor1_sound_data, self).__init__()
        self.sound = None

class Monster_sound_data(image_data):
    def __init__(self):
        super(Monster_sound_data, self).__init__()
        self.sound = None

class Skill_sound_date(image_data):
    def __init__(self):
        super(Skill_sound_date, self).__init__()
        self.sound = None

class Weapon_sound_data(image_data):
    def __init__(self):
        super(Weapon_sound_data, self).__init__()
        self.sound = None

class font_date():
    def __init__(self):
        self.font = None