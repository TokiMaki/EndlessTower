import platform
import os

if platform.architecture()[0] == '32bit':
    os.environ["PYSDL2_DLL_PATH"] = "SDL2\\x86"
else:
    os.environ["PYSDL2_DLL_PATH"] = "SDL2\\x64"


import Project_SceneFrameWork
import Scene000_Battle
import Scene001_Gacha
import Scene004_Title
from pico2d import *

open_canvas(Project_SceneFrameWork.Window_W, Project_SceneFrameWork.Window_H)
Project_SceneFrameWork.run(Scene004_Title)
