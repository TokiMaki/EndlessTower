from pico2d import *

Actor1 = None
Monster = None
Skill = None

def Upload_data():
    global Actor1, Monster, Skill
    if Actor1 is None:
        Actor1 = Actor_sound_data()
        Actor1.image = load_image('Resource\\Actor\\Actor1_1.png')
    if Monster is None:
        Monster = Monster_sound_data()
        Monster.image = load_image('Resource\\Monster\\Monster.png')
    if Skill is None:
        Skill = Skill_sound_date()
        Skill.image = load_image('Resource\\Skill\\IconSet.png')


class image_data():
    def __init__(self):
        self.image = None


class Actor_sound_data(image_data):
    def __init__(self):
        super(Actor_sound_data, self).__init__()
        self.sound = None

class Monster_sound_data(image_data):
    def __init__(self):
        super(Monster_sound_data, self).__init__()
        self.sound = None

class Skill_sound_date(image_data):
    def __init__(self):
        super(Skill_sound_date, self).__init__()
        self.sound = None
