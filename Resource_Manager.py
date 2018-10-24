from pico2d import *

Actor = None
Actor1 = None
Monster = None
Skill = None
Skill_sel = None

def Upload_data():
    global Actor, Actor1, Monster, Skill, Skill_sel
    if Actor is None:
        Actor = [Actor1_sound_data() for i in range(4)]
        Actor[0].image = load_image('Resource\\Actor\\Actor1.png')
        Actor[1].image = load_image('Resource\\Actor\\Actor2.png')
        Actor[2].image = load_image('Resource\\Actor\\Actor3.png')
        Actor[3].image = load_image('Resource\\Actor\\Actor4.png')


    if Actor1 is None:
        Actor1 = [Actor1_sound_data() for i in range(8)]
        Actor1[0].image = load_image('Resource\\Actor\\Actor1_1.png')
        Actor1[1].image = load_image('Resource\\Actor\\Actor1_2.png')
        Actor1[2].image = load_image('Resource\\Actor\\Actor1_3.png')
        Actor1[3].image = load_image('Resource\\Actor\\Actor1_4.png')
        Actor1[4].image = load_image('Resource\\Actor\\Actor1_5.png')
        Actor1[5].image = load_image('Resource\\Actor\\Actor1_6.png')
        Actor1[6].image = load_image('Resource\\Actor\\Actor1_7.png')
        Actor1[7].image = load_image('Resource\\Actor\\Actor1_8.png')

    if Monster is None:
        Monster = [Monster_sound_data() for i in range(2)]
        Monster[0].image = load_image('Resource\\Monster\\Monster.png')
        Monster[1].image = load_image('Resource\\Monster\\Damage3.png')
    if Skill is None:
        Skill = Skill_sound_date()
        Skill.image = load_image('Resource\\Skill\\IconSet.png')
    if Skill_sel is None:
        Skill_sel = image_data()
        Skill_sel.image = load_image('Resource\\Skill\\skill_sel.png')


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
