#panda imports
from direct.showbase.ShowBase import ShowBase
from panda3d.core import *
from direct.filter.CommonFilters import CommonFilters
from direct.task import Task

# a bit of qts
from PyQt4.QtCore import * 
from PyQt4.QtGui import * 

#libs imports
import __builtin__
import os, sys

#lucrezia imports
from grid.grid import Grid

#from utils.once import Once
from parser.parser import Parser
from resourcemanager.resourcemanager import ResourceManager
from extract.extract import ExtractTitle
from configmanager.configmanager import ConfigManager
from audio.audioManager import AudioManager
from gui.menuParent import MainMenu
from gui.baloonmanager import BaloonManager
from camera.camera import CustomCamera
from utils.fadeout import FadeOut
from intro.intro import Intro
from script.script import Script
from persistence.persistence import Persistence

#editors import
from editor.grid import ThreeAxisGrid
from editor.editorcamera import EditorCamera

#gui imports
from editor.gui.QTTest import QTTest
from editor.gui.GuiManager import GuiManager
from editor.gui.SceneGraphBrowser import SceneGraphBrowser

__builtin__.resourceManager = ResourceManager()
__builtin__.configManager = ConfigManager()
#configmanager.loadConfig()

#fullscreen e grandezza finestra
loadPrcFileData("","""
gl-debug false
fullscreen 0
win-size 1366 768
text-encoding utf8
show-frame-rate-meter 1
sync-video 1
framebuffer-srgb #t
""")

'''
ingoing:
editor_loadmap [filename]
outgoing:
'''
class MyApp(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)
        
        self.editormode = True
        
        base.win.setClearColor((0, 0, 0, 1))
        base.win.setClearColorActive(True)
        lang="ita"

        '''
        #ortho camera lens
        lens = OrthographicLens()
        lens.setFilmSize(12, 9)  #TODO: quattro terzi, fixare, spostare tutto nella classe telecamera e adattare in base allo schermo utente
        base.cam.node().setLens(lens)
        base.cam.setY(-5)
        base.cam.setP(-355)
        '''
        
        #enabling shader system (and ppl)
        render.setShaderAuto()
        #base.oobe()
        
        #defining global variables
        # TAKE CARE: these must be objects created form classes which
        # structure has been built with globalness in mind!!
        #
        # for completeness: add minus 'p' before class name for naming variables
        __builtin__.main = self
        __builtin__.pGrid = Grid()
        __builtin__.extract = ExtractTitle()
        __builtin__.baloons = BaloonManager()
        #__builtin__.configManager = ConfigManager() 
        __builtin__.audioManager = AudioManager()
        
        
        __builtin__.editorCamera = EditorCamera()
        __builtin__.customCamera = __builtin__.editorCamera
        #careful, refactor? here for compatibility between game engine and editor engine
        
        __builtin__.script = Script()
        __builtin__.persistence = Persistence()
        
        self.prepareEditor()
        
        self.accept("editor_loadmap", self.loadMap)
        
    def pandaCallback(self):
		taskMgr.step()
    
    def loadMap(self, filename):
        pGrid.changeMapHelper(str(filename),'0,0')
    
    # this instantiates the three axis grid
    def prepareEditor(self):
        self.threeaxisgrid = ThreeAxisGrid(50,0,50,1,1)
        tagnodepath = self.threeaxisgrid.create()
        tagnodepath.setY(-0.1)
        tagnodepath.setLightOff()
        tagnodepath.reparentTo(render)
        tagnodepath.setLightOff()
        base.setBackgroundColor(1,1,1)

w = MyApp()

app = QApplication(sys.argv)

# left panel
q = QTTest(w.pandaCallback)
q.show()

# right panel
s = SceneGraphBrowser()
s.show()


app.exec_()

w.run()
