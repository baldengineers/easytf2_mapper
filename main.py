#!/usr/bin/env python3
import sys
sys.path.append("prefabs/")
import os.path
import os
from PySide.QtCore import *
from PySide.QtGui import *
import importlib
import createPrefab
from PIL import Image
from PIL.ImageQt import ImageQt
import generateSkybox
import light_create
import subprocess
import pickle
import pprint
import random
import glob
import webbrowser
import wave
import zipfile
'''check todo every time you open this'''
#TODO: more prefabs, mo betta
class GridBtn(QWidget):
    def __init__(self, parent, x, y, btn_id):
        super(GridBtn, self).__init__()
        self.button = QPushButton("", parent)
        self.x = 32*x
        self.y = 20+(32*y)
        self.button.move(self.x,self.y)
        self.button.resize(32,32)
        self.button.setFixedSize(32, 32)
        self.button.pressed.connect(lambda: self.click_func(parent, x, y,
                                                            btn_id))
        self.button.setMouseTracking(True)
        self.button.installEventFilter(self)
        self.button.show()

    def reset_icon(self):
        self.button.setIcon(QIcon())

    def click_func(self, parent, x, y, btn_id):
        self.checkForAlt()
        global rotation, currentfilename
        if toggle != 0:
            self.button.setIcon(QIcon())
            totalblocks[level][btn_id] = ''
            entity_list[level][btn_id] = ''
            iconlist[level][btn_id] = ''
        else:
            print((x,y))
            global world_id_num
            global id_num
            global entity_num
            global entity_list
            global placeholder_list
            global icon
            global rotation
            global totalblocks
            global entity_list
            global levels
            #print(totalblocks)
            #print(btn_id)
            #eval() turns the string into a variable name.
            moduleName = eval(prefab_list[parent.tile_list.currentRow()])
            #print(rotation)
            try:
                try:
                    try:
                        try:
                            create = moduleName.createTile(x, y, id_num, world_id_num, entity_num, placeholder_list, rotation, level)
                        except Exception as e:
                            #print(str(e))
                            create = moduleName.createTile(x, y, id_num, world_id_num, entity_num, placeholder_list, rotation, level)
                    except Exception as e:
                        #print(str(e))
                        create = moduleName.createTile(x, y, id_num, world_id_num, level)
                except Exception as e:
                    #print(str(e))
                    create = moduleName.createTile(x, y, id_num, world_id_num, entity_num, placeholder_list, level)
            except Exception as e:
                create = moduleName.createTile(x, y, id_num, world_id_num, rotation, level)
                #print(str(e))
            #create = test_prefab.createTile(x, y, id_num, world_id_num)
            id_num = create[1]
            world_id_num = create[2]
            try:
                entity_num = create[3]
                placeholder_list = create[5]
                #print("placeholder list: ", placeholder_list)
            except IndexError:
                pass
            #if parent.comboBox.currentIndex() != 0:
                #create2 = ground_prefab.createTile(x, y, id_num, world_id_num)
                #world_id_num +=1
                #create = create + create2
                #print(create)
                #print(id_num)
                #print(world_id_num)
                
            #else:
                #pass
                #print(create)
                #print(id_num)
                #print(world_id_num)
                #this is obsolete -anson
            ###
            ###
            try:
                #print(rotation)
                current_prefab_icon_list = open('prefab_template/rot_prefab_list.txt', 'r+')
                current_prefab_icon_list = current_prefab_icon_list.readlines()
                current_prefab_icon_list = current_prefab_icon_list[parent.tile_list.currentRow()]
                if "\n" in current_prefab_icon_list:
                    current_prefab_icon_list = current_prefab_icon_list[:-1]
                current_prefab_icon_list = open('prefab_template/iconlists/'+current_prefab_icon_list, 'r+')
                current_prefab_icon_list = current_prefab_icon_list.readlines()
                icon = current_prefab_icon_list[rotation]
                if "\n" in icon:
                    icon = icon[:-1]
                #print(icon)
                self.button.setIcon(QIcon(icon))
                self.button.setIconSize(QSize(32,32))
            except Exception as e:
                print(str(e))
                icon = prefab_icon_list[parent.tile_list.currentRow()]
                self.button.setIcon(QIcon(icon))
                self.button.setIconSize(QSize(32,32))

            #print(iconlist,level, btn_id)
            iconlist[level][btn_id] = icon
            totalblocks[level][btn_id] = create[0]
            #print(btn_id)
            #print(iconlist)
            
            try:
                entity_list[level][btn_id] = create[4]
                #print(create[4])
            except Exception as e:
                print(str(e))
            #print(level)
            if "*" not in currentfilename:
                currentfilename = currentfilename+'*'
                parent.setWindowTitle("Easy TF2 Mapper - ["+currentfilename+"]")
    def checkForAlt(self):
        modifiers = QApplication.keyboardModifiers()
        if modifiers == Qt.ControlModifier:
            global toggle
            toggle = 1
        else:
            global toggle
            toggle = 0
        
class MainWindow(QMainWindow):
    def __init__(self):
        #create the main window
        super(MainWindow, self).__init__()
        self.setGeometry(100, 25, 875, 750)
        self.setWindowTitle("Easy TF2 Mapper")
        self.setWindowIcon(QIcon("icons\icon.ico"))
        namelist = ['gravelpit','2fort','upward','mvm']
        palette = QPalette()
        palette.setBrush(QPalette.Background,QBrush(QPixmap("icons/backgrounds/background_"+namelist[random.randint(0,3)]+".jpg")))
        self.setPalette(palette)
        #self.setStyleSheet("image: url(icons/backgrounds/background_mvm.jpg); background-repeat: stretch;")
        #self.resizeEvent(self.resizefunc)
        #self.resizeEvent(palette.setBrush(QPalette.Background,QBrush(QPixmap("icons/backgrounds/background_"+namelist[random.randint(0,3)]+".jpg").scaled(self.size()))))


        #create menubar
        exitAction = QAction("&Exit", self)
        exitAction.setShortcut("Ctrl+Q")
        exitAction.setStatusTip("Exit Application")
        exitAction.triggered.connect(self.close_application)

        openAction = QAction("&Open", self)
        openAction.setShortcut("Ctrl+O")
        openAction.setStatusTip("Open .vmf file")
        openAction.triggered.connect(self.file_open)

        saveAction = QAction("&Save", self)
        saveAction.setShortcut("Ctrl+S")
        saveAction.setStatusTip("Save File as .ezm save, allowing for use by others/you later.")
        saveAction.triggered.connect(self.file_save)
        
        saveAsAction = QAction("&Save As", self)
        saveAsAction.setShortcut("Ctrl+Shift+S")
        saveAsAction.setStatusTip("Save File as .ezm save, allowing for use by others/you later.")
        saveAsAction.triggered.connect(lambda: self.file_save(False, True))
        
        helpAction = QAction("&Wiki",self)
        helpAction.triggered.connect(lambda: webbrowser.open_new_tab('http://github.com/baldengineers/easytf2_mapper/wiki')
        
        tutorialAction = QAction("&Reference Guide",self)
        tutorialAction.setStatusTip("Quick reference guide on the TF2Mapper website.")
        tutorialAction.triggered.connect(lambda: webbrowser.open_new_tab('http://tf2mapper.com/tutorial.html')



        newAction = QAction("&New", self)
        newAction.setShortcut("Ctrl+n")
        newAction.setStatusTip("Create a New File")
        newAction.triggered.connect(lambda: self.grid_change(0,0,0,True,False,True))

        hammerAction = QAction("&Open Hammer",self)
        hammerAction.setShortcut("Ctrl+H")
        hammerAction.setStatusTip("Opens up Hammer.")
        hammerAction.triggered.connect(lambda: self.open_hammer(0,"null"))

        changeHammer = QAction("&Change Hammer Directory",self)
        changeHammer.setShortcut("Ctrl+Shift+H")
        changeHammer.setStatusTip("Changes default hammer directory.")
        changeHammer.triggered.connect(lambda: self.open_hammer(0,"null",True))

        changeLightAction = QAction("&Change Lighting", self)
        changeLightAction.setShortcut("Ctrl+J")
        changeLightAction.setStatusTip("Change the environment lighting of the map.")
        changeLightAction.triggered.connect(self.change_light)
        
        exportAction = QAction("&as .VMF", self)
        exportAction.setShortcut("Ctrl+E")
        exportAction.setStatusTip("Export as .vmf")
        exportAction.triggered.connect(self.file_export)
        
        removeAction = QAction("&Remove Last Prefab(s)",self)
        removeAction.setShortcut("Ctrl+R")
        removeAction.setStatusTip("Delete a variable amount of prefabs from the end of the list")
        removeAction.triggered.connect(self.remove_prefabs)

        gridAction = QAction("&Set Grid Size", self)
        gridAction.setShortcut("Ctrl+G")
        gridAction.setStatusTip("Set Grid Height and Width. RESETS ALL BLOCKS.")
        gridAction.triggered.connect(lambda: self.grid_change(0,0,0,True,False,True))

        createPrefabAction = QAction("&Create Prefab", self)
        createPrefabAction.setShortcut("Ctrl+I")
        createPrefabAction.setStatusTip("View the readme for a good idea on formatting Hammer Prefabs.")
        createPrefabAction.triggered.connect(self.create_prefab)

        consoleAction = QAction("&Open Dev Console", self)
        consoleAction.setShortcut("`")
        consoleAction.setStatusTip("Run functions/print variables manually")
        consoleAction.triggered.connect(self.open_console)

        #refreshPrefab = QAction("&Refresh Prefab List", self)
        #refreshPrefab.setStatusTip("Refresh the list of prefabs, done after creating a new one.")
        #refreshPrefab.triggered.connect(self.importprefabs)

        changeSkybox = QAction("&Change Skybox", self)
        changeSkybox.setStatusTip("Change the skybox of the map.")
        changeSkybox.setShortcut("Ctrl+B")
        changeSkybox.triggered.connect(self.change_skybox)
        
        importPrefab = QAction("&Prefab",self)
        importPrefab.setStatusTip("Import a prefab in a .zip file. You can find some user-made ones at http://tf2mapper.com")
        importPrefab.setShortcut("Ctrl+Shift+I")
        importPrefab.triggered.connect(self.import_prefab)
        
        self.statusBar()

        
        
        mainMenu = self.menuBar()
        helpMenu = mainmenu.addMenu("&Help")
        
        fileMenu = mainMenu.addMenu("&File")
        optionsMenu = mainMenu.addMenu("&Options")
        toolsMenu = mainMenu.addMenu("&Tools")
        #createMenu = mainMenu.addMenu("&Create")
        
        fileMenu.addAction(newAction)
        fileMenu.addAction(openAction)
        fileMenu.addAction(saveAction)
        fileMenu.addAction(saveAsAction)
        fileMenu.addSeparator()
        
        helpMenu.addAction(tutorialAction)
        helpMenu.addAction(helpAction)
        
        #fileMenu.addAction(exportAction)
        #fileMenu.addAction(importPrefab)
        importMenu = fileMenu.addMenu("&Import")
        importMenu.addAction(importPrefab)

        exportMenu = fileMenu.addMenu("&Export")
        exportMenu.addAction(exportAction)
        
        fileMenu.addSeparator()
        
        fileMenu.addAction(exitAction)

        optionsMenu.addAction(gridAction)
        optionsMenu.addAction(changeSkybox)
        optionsMenu.addAction(changeHammer)
        #optionsMenu.addAction(removeAction)
        
        toolsMenu.addAction(createPrefabAction)
        toolsMenu.addAction(hammerAction)
        toolsMenu.addSeparator()
        toolsMenu.addAction(consoleAction)
        
        self.home()
        self.change_skybox()
        self.level_select()


        
    def open_hammer(self,loaded,file,reloc = False):
        self.open_file()
        if "loaded_first_time" not in self.files or reloc:
            self.file.close()
            self.open_file(True)
            hammer_location = QFileDialog.getOpenFileName(self, "Find Hammer Location", "C:/","Hammer Executable (*.exe *.bat)")
            hammer_location = str(hammer_location[0])
            self.file.write("loaded_first_time\n")
            self.file.write(hammer_location)
            self.file.close()
            if loaded == 1:
                subprocess.Popen(hammer_location +" "+ file)
                #print("work")
            else:
                subprocess.Popen(hammer_location)
        else:
            
            try:
                if loaded == 1:
                    subprocess.Popen(self.fileloaded[1] + " "+file)
                    #print("work")
                else:
                    subprocess.Popen(self.fileloaded[1])
            except Exception as e:
                print(str(e))
                self.pootup = QMessageBox()
                self.pootup.setText("ERROR!")
                self.pootup.setInformativeText("Hammer executable/batch moved or renamed!")
                self.pootup.exec_()

                self.file.close()
                os.remove("startupcache/startup.su")
                self.open_hammer(0,"null")

    def open_file(self,reloc = False):
        if reloc:
            os.remove("startupcache/startup.su")
        
        try:
            self.file = open("startupcache/startup.su", "r+")
        except:
            self.file = open("startupcache/startup.su", "w+")
        self.fileloaded = self.file.readlines()
        self.files = "".join(self.fileloaded)

    def remove_prefabs(self):
        import removeText
        num = QInputDialog.getText(self,("Remove Prefabs"),("Remove x number of prefabs from the back of the list. REQUIRES RESTART"))
        try:
            num = int(num[0])
        except:
            QMessageBox.critical(self, "Error", "Please enter a number.")
            self.remove_prefabs()
        removeText.reset(num)

    def closeEvent(self, event):
        #closeEvent runs close_application when the x button is pressed
        event.ignore()
        self.close_application()
        
    def home(self):
        #test
        global levels
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        #self.labelLayout = QHBoxLayout(self)
        #self.palette = QPalette()
        #self.palette.setColor(QPalette.Shadow, QColor('grey'))

        self.scrollArea = QScrollArea()
        
        #self.scrollArea.setAttribute(Qt.WA_TranslucentBackground)
        #self.scrollArea.setStyleSheet("background-color:transparent;")

        self.scrollArea.setStyleSheet("background-color: rgb(50, 50, 50, 100);")

        self.scrollArea.setBackgroundRole(QPalette.Light)
        #self.scrollArea.setAutoFillBackground(False)


    
        try:
            self.scrollArea.setGeometry(QRect(0, 0, self.grid_x*32, self.grid_y*32))
        except:
            self.scrollArea.setGeometry(QRect(0,0,580,580))
        try:
            if self.grid_x > 16:
                self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
            if self.grid_y > 16:
                self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        except:
            pass


        actiondict = {}
        self.buttonLabel = QLabel("Rotation:",self)
        #self.currentLabel = QLabel("Current Rotation:",self)
        self.listLabel = QLabel("List of prefabs:",self)
        self.gridLabel = QLabel("Work Area:",self)
        
        self.divider = QFrame(self)
        self.divider.setFrameShape(QFrame.VLine)
        self.divider.setLineWidth(10)

        self.dividerH = QFrame(self)
        self.dividerH.setFrameShape(QFrame.HLine)
        self.dividerH.setLineWidth(10)
        

        #self.labelLayout.addWidget(self.gridLabel)
        #self.labelLayout.addWidget(self.listLabel)
        #self.labelLayout.setContentsMargins(0,0,0,0)
        #self.labelLayout.setSpacing(10)

        self.current = QPushButton("",self)
        self.current.setIcon(QIcon(''))
        self.current.setIconSize(QSize(40,40))
        self.current.setFixedSize(QSize(40,40))
        self.current.setFlat(True)
        self.current.clicked.connect(self.heavy)

        self.level = QPushButton(self)

        self.level.setText("Level: 1")
        
        self.level.setFixedSize(QSize(150,30))
        #self.level.setMenu(self.levelMenu)
        self.level.clicked.connect(self.level_select)

        self.levelup = QToolButton(self)
        self.levelup.setIcon(QIcon('icons/up.png'))
        self.levelup.setIconSize(QSize(20,20))
        self.levelup.clicked.connect(lambda: self.change_level(True, True))
        self.levelup.setAutoRaise(True)

        self.leveldown = QToolButton(self)
        self.leveldown.setIcon(QIcon('icons/down.png'))
        self.leveldown.setIconSize(QSize(20,20))
        self.leveldown.clicked.connect(lambda: self.change_level(True, False))
        self.leveldown.setAutoRaise(True)
        
        self.rotateCW = QToolButton(self)
        self.rotateCW.setIcon(QIcon('icons/rotate_cw.png'))
        self.rotateCW.setIconSize(QSize(40,40))
        self.rotateCW.setFixedSize(QSize(40,40))
        self.rotateCW.setAutoRaise(True)

        self.rotateCCW = QToolButton(self)
        self.rotateCCW.setIcon(QIcon('icons/rotate_ccw.png'))
        self.rotateCCW.setIconSize(QSize(40,40))
        self.rotateCCW.setFixedSize(QSize(40,40))
        self.rotateCCW.setAutoRaise(True)

        #sets rotation value. 0 = right, 1 = down, 2 = left, 3 = right
        self.rotateCW.clicked.connect(self.rotateCW_func)
        self.rotateCCW.clicked.connect(self.rotateCCW_func)
        
        self.button_rotate_layout = QHBoxLayout()
        self.button_rotate_layout.addWidget(self.buttonLabel)
        self.button_rotate_layout.addWidget(self.rotateCCW)
        #self.button_rotate_layout.addWidget(self.currentLabel)
        self.button_rotate_layout.addWidget(self.current)
        self.button_rotate_layout.addWidget(self.rotateCW)
        self.button_rotate_layout.addWidget(self.divider)
        self.button_rotate_layout.addWidget(self.level)
        self.button_rotate_layout.addWidget(self.levelup)
        self.button_rotate_layout.addWidget(self.leveldown)
        
        self.button_rotate_layout.addStretch(1)
                               
        self.tile_list = QListWidget()
        self.tile_list.setMaximumWidth(200)
        self.tile_list.setStyleSheet("QListWidget { background-color: rgb(50, 50, 50, 100); }")

        self.up_tool_btn = QToolButton(self)
        self.up_tool_btn.setIcon(QIcon('icons/up.png'))
        self.up_tool_btn.clicked.connect(self.prefab_list_up)
        
        self.down_tool_btn = QToolButton(self)
        self.down_tool_btn.setIcon(QIcon('icons/down.png'))
        self.down_tool_btn.clicked.connect(self.prefab_list_down)
        
        self.del_tool_btn = QToolButton(self)
        self.del_tool_btn.setIcon(QIcon('icons/delete.png'))
        self.del_tool_btn.clicked.connect(lambda: self.prefab_list_del(self.tile_list.currentRow(), self.tile_list.currentItem()))

        self.add_tool_btn = QToolButton(self)
        self.add_tool_btn.setIcon(QIcon('icons/add.png'))
        self.add_tool_btn.clicked.connect(self.create_prefab)
        
        self.tile_toolbar = QToolBar()
        self.tile_toolbar.addWidget(self.up_tool_btn)
        self.tile_toolbar.addSeparator()
        self.tile_toolbar.addWidget(self.down_tool_btn)
        self.tile_toolbar.addSeparator()
        self.tile_toolbar.addWidget(self.del_tool_btn)
        self.tile_toolbar.addSeparator()
        self.tile_toolbar.addWidget(self.add_tool_btn)

        
        for index, text in enumerate(prefab_text_list):
            item = QListWidgetItem(QIcon(prefab_icon_list[index]), text)
            self.tile_list.addItem(item)

        self.tile_list.currentItemChanged.connect(self.changeIcon)
        #contains label and list vertically
        self.tile_list_layout = QVBoxLayout()
        self.tile_list_layout.addWidget(self.listLabel)
        self.tile_list_layout.addWidget(self.tile_list)
        self.tile_list_layout.addWidget(self.tile_toolbar)
        
        self.button_grid_layout = QGridLayout()
        self.button_grid_layout.setSpacing(0)
        #self.layout_grid = QBoxLayout()
        
        self.grid_widget = QWidget()
        self.grid_widget.setLayout(self.button_grid_layout)
        self.scrollArea.setWidget(self.grid_widget)
        #self.scrollArea.ensureWidgetVisible(self.grid_widget)
        self.scrollArea.setWidgetResizable(True)

        #self.scrollFrame = QLabel(self.scrollArea)
        #self.scrollFrame.setFrameStyle(QFrame.Panel | QFrame.Raised)
        #self.scrollFrame.setGeometry(QRect(0,0,580,580))
        #self.scrollFrameLayout = QVBoxLayout()
        #self.scrollFrameLayout.addWidget(self.scrollFrame)
        #self.scrollFrameLayout.addWidget(self.scrollArea)
        #contains label and grid vertically
        self.gridLayout = QVBoxLayout()
        self.gridLayout.addWidget(self.gridLabel)
        self.gridLayout.addWidget(self.scrollArea)
        self.button_grid_all = QVBoxLayout()
        #self.button_grid_all.addStretch(0)
        #self.button_grid_all.setSpacing(0)
        self.button_grid_all.addLayout(self.button_rotate_layout)
        self.button_grid_all.addWidget(self.dividerH)
        self.button_grid_all.addLayout(self.gridLayout)
        #self.button_grid_all.addStretch(1)
        #self.button_grid_all.addWidget(self.scrollArea)
        
        self.column = QHBoxLayout()
        self.column.addLayout(self.button_grid_all)
        #self.column.addStretch(1)
        self.column.addLayout(self.tile_list_layout)
        #self.column.addLayout(self.button_rotate_layout)
        #self.column.addStretch(1)
        
        self.row = QVBoxLayout(self.central_widget)
        #self.row.addLayout(self.labelLayout)
        self.row.addLayout(self.column)
        #self.row.addLayout(self.button_rotate_layout)
        #self.row.addStretch(1)
        #self.row.addStretch(1)
        
        try:
            f = open('startupcache/firsttime.su', 'r+')
            lines = f.readlines()
        except:
            f = open('startupcache/firsttime.su','w+')
            lines = f.readlines()
            
        if "startup" not in lines:
            '''
            self.popup = QMessageBox(self)
            self.popup.setGeometry(100,100,500,250)
            self.popup.setWindowTitle("First Launch")
            self.popup.setInformativeText("You haven't launched this before! Try looking at the <a href=\"https://github.com/baldengineers/easytf2_mapper/wiki/Texture-bug\">wiki</a> for help!")
            self.popup.setText("First Launch!")
            self.popup.exec_()
            #this is obsolete - jony
            '''

            QMessageBox.information(self, "First Launch", "First Launch!\n\nYou haven't launched this before! Try looking at the <a href=\"https://github.com/baldengineers/easytf2_mapper/wiki/Texture-bug\">wiki</a> for help!")
            f.write("startup")
            f.close
            subprocess.Popen("associconwin.bat")
            #WILL ONLY WORK IN REDIST FORM
        else:
            pass
        
        self.grid_change(0,0,0,True, False, True)
        '''
        while True:
            try:
                if self.tile_list.currentItemChanged:
                    self.changeIcon()
            except:
                pass
        '''
        
        self.show()

    def level_select(self):
        self.windowl = QDialog(self)
        global levels
        #testing
        #
        self.levellist = QListWidget()
        self.levellist.setIconSize(QSize(200, 25))
        try:
            for i in range(levels):
                item = QListWidgetItem(QIcon("icons/level.jpg"),"Level "+str(i+1))
                self.levellist.addItem(item)
        except Exception as e:
            print(str(e))
            pass

        self.levellist.itemClicked.connect(lambda: self.change_level(False, False))
        self.layoutl = QHBoxLayout()
        self.layoutl.addWidget(self.levellist)
        self.windowl.setGeometry(150,150,400,300)
        self.windowl.setWindowTitle("Choose a level")
        self.windowl.setWindowIcon(QIcon("icons/icon.ico"))
        self.windowl.setLayout(self.layoutl)
        self.windowl.exec_()

    def change_level(self, but = False, up = False):
        global level, levels
        if not but:
            self.file_save(True)
            level = int(self.levellist.currentRow()) #+1 X First level should be 0
            print(level)
            self.file_open(True)
            self.windowl.close()
            self.level.setText("Level: " + str(level+1))
        if up:
            self.file_save(True)
            if level != levels-1:
                level = int(level+1)
            else:
                pass
            print(level)
            self.file_open(True)
            self.level.setText("Level: " + str(level+1))
        elif not up and but:
            self.file_save(True)
            if level != 0:
                level = int(level-1)
            else:
                pass
            print(level)
            self.file_open(True)
            self.level.setText("Level: " + str(level+1))            
        #print(totalblocks)
        #print(iconlist)
        #change grid to grid for level
        

    def rotateCW_func(self):
        global rotation
        if rotation < 3:
            rotation = rotation + 1
        else:
            rotation = 0
        self.changeIcon()

    def rotateCCW_func(self):
        global rotation
        if rotation == 0:
            rotation = 3
        else:
            rotation = rotation - 1
        self.changeIcon()

    def prefab_list_up(self):
        currentRow = self.tile_list.currentRow()
        #print(currentRow)

        if currentRow > 0:
            currentItem = self.tile_list.takeItem(currentRow)
            self.tile_list.insertItem(currentRow - 1, currentItem)
            self.tile_list.setCurrentRow(currentRow - 1)
            self.update_list_file(currentRow, currentRow - 1)
            self.changeIcon()

    def prefab_list_down(self):
        currentRow = self.tile_list.currentRow()
        #print(currentRow)
        #print(self.tile_list.count())
        if currentRow < self.tile_list.count() - 1:
            currentItem = self.tile_list.takeItem(currentRow)
            self.tile_list.insertItem(currentRow + 1, currentItem)
            self.tile_list.setCurrentRow(currentRow + 1)
            self.update_list_file(currentRow, currentRow + 1)
            self.changeIcon()

    def update_list_file(self, old_index, new_index):
        file_list = ["prefab_template/prefab_list.txt", "prefab_template/prefab_icon_list.txt", "prefab_template/prefab_text_list.txt"]
        list_list = [prefab_list, prefab_icon_list, prefab_text_list]

        for l in list_list:
            l.insert(new_index, l.pop(old_index))

            with open(file_list[list_list.index(l)], "w") as file:

                if list_list.index(l) == 0:   
                    rot_file = open("prefab_template/rot_prefab_list.txt", "w")

                for item in l:
                    file.write(item + "\n")

                    if list_list.index(l) == 0: 
                        rot_file.write(item + "_icon_list.txt" + "\n")

        #stupid icon lists, making me add more lines of code to my already concise function
         

    def prefab_list_del(self, currentprefab, currentText):
        self.restartCheck = QCheckBox()
        self.restartCheck.setText("Restart after deletion?")

        choice = QMessageBox.question(self,"Delete Prefab (DO NOT DELETE STOCK PREFABS)","Are you sure you want to delete \"%s\"?\nThis is mainly for developers." %(prefab_text_list[currentprefab]),
                             QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        
        #choice.addWidget(self.restartCheck)
        #self.layout = choice.layout()
        #self.layout.addWidget(QMessageBox.Yes)
        #self.layout.addWidget(QMessageBox.No)
        #self.layout.addWidget(self.restartCheck)
        #choice.show()        
        if choice == QMessageBox.Yes:
            text_list = ['prefab_template/prefab_text_list.txt','prefab_template/rot_prefab_list.txt',
                 'prefab_template/prefab_list.txt', 'prefab_template/prefab_icon_list.txt']

            for cur in text_list:
                file = open(cur, 'r+')
                cur_list = file.readlines()
                file.seek(0)
                file.truncate()
                
                del cur_list[currentprefab]
                cur_str = "".join(cur_list)
                file.write(cur_str)
                file.close()
            
            restart_btn = QPushButton("Restart")
            later_btn = QPushButton("Later")
            choice = QMessageBox(self)
            choice.setIcon(QMessageBox.Question)
            choice.setWindowTitle("Prefab Successfully Deleted")
            choice.setText("Program must be restarted for changes to take effect.")
            choice.setInformativeText("Restart? You will lose any unsaved progress.")
            choice.addButton(restart_btn, QMessageBox.YesRole)
            choice.addButton(later_btn, QMessageBox.NoRole)
            choice.setDefaultButton(later_btn)
            #print(choice.exec_())
                              
            if choice.exec_() == 0:
                try:
                    subprocess.Popen('EasyTF2Mapper.exe')
                except:
                    subprocess.Popen('python main.py')
                sys.exit()
            else:
                pass
            
        else:
            del choice

    def changeIcon(self):
        global rotation
        
        try:
            current_prefab_icon_list2 = open('prefab_template/rot_prefab_list.txt', 'r+')
            current_prefab_icon_list2 = current_prefab_icon_list2.readlines()
            current_prefab_icon_list2 = current_prefab_icon_list2[self.tile_list.currentRow()]
            if "\n" in current_prefab_icon_list2:
                current_prefab_icon_list2 = current_prefab_icon_list2[:-1]
            current_prefab_icon_list2 = open('prefab_template/iconlists/'+current_prefab_icon_list2, 'r+')
            current_prefab_icon_list2 = current_prefab_icon_list2.readlines()
            icon2 = current_prefab_icon_list2[rotation]
            if "\n" in icon2:
                icon2 = icon2[:-1]
            self.current.setIcon(QIcon(icon2))
            self.current.setIconSize(QSize(32,32))
        except Exception as e:
            print(str(e))
            icon = prefab_icon_list[self.tile_list.currentRow()]
            self.current.setIcon(QIcon(icon))
            self.current.setIconSize(QSize(32,32))
            
        '''
        im_rot = Image.open(prefab_icon_list[self.tile_list.currentRow()])
        im_rot = im_rot.rotate(360-(rotation*90))
        data = im_rot.tobytes('raw')#('raw', 'RGBA')
        im_rot_qt = QImage(data, im_rot.size[0], im_rot.size[1], QImage.Format_ARGB32)
        im_rot.close()
        icon = QPixmap.fromImage(im_rot_qt)
        self.current.setIcon(QIcon(icon))
        self.current.setIconSize(QSize(32,32))
        '''             
        

 
        
        
    def file_open(self, tmp = False, first = False):
        global grid_list, iconlist, level, totalblocks,entity_list, currentfilename, file_loaded, latest_path
        print(latest_path)
        if not tmp:
            name = QFileDialog.getOpenFileName(self, "Open File", latest_path,"*.ezm")
            latest_path,file = str(name[0]),open(name[0], "rb")
            level = 0
            #del totalblocks, entity_list,iconlist,grid_list
            iconlist=[]
            while True:
                #try:
                header = pickle.load(file)
                if "levels" in header:
                    openlines = pickle.load(file)
                    levelcountload = openlines
                    
                elif "grid_size" in header:
                    openlines = pickle.load(file)
                    self.grid_change(openlines[0],openlines[1],openlines[2],False, True, True)
                elif "totalblocks" in header:
                    totalblocks=[]
                    openlines = pickle.load(file)
                    for item in openlines:
                        #print(item)
                        totalblocks.append(item)
                elif "entity_list" in header:
                    entity_list=[]
                    openlines = pickle.load(file)
                    
                    for item in openlines:
                        entity_list.append(item)
                elif "icon_list" in header:
                    global grid_list
                    iconlist=[]
                    openlines = pickle.load(file)
                    #print(openlines)

                    for item in openlines:
                        iconlist.append(item)
                    for index, icon in enumerate(iconlist[0]):
                        #print(iconlist)
                        if "icons" in icon:
                            #print(index)
                            grid_list[index].button.setIcon(QIcon(icon))
                            grid_list[index].button.setIconSize(QSize(32,32))
                elif "skybox2_list" in header:
                    openlines = pickle.load(file)
                    skybox2_list.setCurrentRow(openlines)
                else:
                    break
                #print(iconlist)
                #print(totalblocks)
            #print(iconlist)
            #print(totalblocks)
        
            for i in range(levelcountload):
                file = open("leveltemp/level" + str(i)+".tmp", "wb")
                pickle.dump(iconlist[i], file)
                file.close()
              
            self.change_skybox()
            file.close()
            self.setWindowTitle("Easy TF2 Mapper - [" + str(name[0]) + "]")
            currentfilename = str(name[0])
            file_loaded = True
            
        else:
            try:
                file = open("leveltemp/level" + str(level)+".tmp", "rb")
                iconlist[level] = pickle.load(file)
                file.close()
                #print(grid_list)
                for index, icon in enumerate(iconlist[level]):
                    #print(icon)
                    grid_list[index].button.setIcon(QIcon(icon))
                    grid_list[index].button.setIconSize(QSize(32,32))
            except Exception as e:
                print(str(e))
        
        #print(totalblocks)
        #print("totalblocks: ", totalblocks)
        #print("entity_list: ", entity_list)
        #openlines = file.readlines()
        #openlinesstr = "".join(openlines)
        
        #now, it imports the vmf, and has two versions of it; the importlines which has each
        #line as a string in a list, and importlinesstr, which makes it one big string
            
    def file_save(self, tmp = False, saveAs = False):
        global grid_x, grid_y, iconlist, levels, level, currentfilename, file_loaded, latest_path
        print(latest_path)
        gridsize_list = (grid_x,grid_y,levels)
        skybox_sav = skybox2_list.currentRow()
        if not tmp:
            if not file_loaded or saveAs:
                name = QFileDialog.getSaveFileName(self, "Save File", latest_path, "*.ezm")[0]
                latest_path = name
            else:
                if "*" in currentfilename:
                    name = currentfilename[:-1]
                else:
                    name = currentfilename
            #print(name)
            file = open(name, "wb")
            pickle.dump("<levels>",file)
            pickle.dump(levels,file)
            pickle.dump("<grid_size>", file)
            pickle.dump(gridsize_list, file)
            #for i in range(levels):
            pickle.dump("<totalblocks>", file)
            pickle.dump(totalblocks, file)
            pickle.dump("<entity_list>", file)
            pickle.dump(entity_list, file)
            pickle.dump("<icon_list>", file)
            pickle.dump(iconlist, file)
            print(iconlist)
            pickle.dump("<skybox>", file)
            pickle.dump(skybox_sav, file)
            file.close()
            QMessageBox.information(self, "File Saved", "File saved as %s" %(name))

            self.setWindowTitle("Easy TF2 Mapper - [" + name + "]")

            currentfilename = name
            file_loaded = True
        else:
            try:#writes tmp file to save the icons for each level
                file = open("leveltemp/level" + str(level)+".tmp", "wb")
                pickle.dump(iconlist[level], file)
                file.close()
            except Exception as e:
                
                print(str(e))
        #text = self.textEdit.toPlainText()
        #file.write(text)
        
        

    def file_export(self):
        global id_num, grid_y, grid_x, world_id_num, count_btns, currentlight, skybox, skybox2_list, entity_list, skybox_light_list, skybox_angle_list, latest_path
        skyboxgeolist = []
        skyboxz = QInputDialog.getText(self,("Set Skybox Height"),("Skybox Height(hammer units, %d minimum recommended):" %(levels*512)))
        try:
            skyboxz = int(skyboxz[0])
        except:
            QMessageBox.critical(self, "Error", "Please enter a number.")
            self.file_export()
        #generate skybox stuff now
        create = generateSkybox.createSkyboxLeft(grid_x,grid_y,skyboxz,id_num,world_id_num)
        skyboxgeolist.append(create[0])
        id_num = create[1]
        world_id_num = create[2]
        create = generateSkybox.createSkyboxNorth(grid_x,grid_y,skyboxz,id_num,world_id_num)
        skyboxgeolist.append(create[0])
        id_num = create[1]
        world_id_num = create[2]
        create = generateSkybox.createSkyboxRight(grid_x,grid_y,skyboxz,id_num,world_id_num)
        skyboxgeolist.append(create[0])
        id_num = create[1]
        world_id_num = create[2]
        create = generateSkybox.createSkyboxTop(grid_x,grid_y,skyboxz,id_num,world_id_num)
        skyboxgeolist.append(create[0])
        id_num = create[1]
        world_id_num = create[2]
        create = generateSkybox.createSkyboxSouth(grid_x,grid_y,skyboxz,id_num,world_id_num)
        skyboxgeolist.append(create[0])
        print(count_btns)
        print(len(entity_list))
        #print(totalblocks)
        skybox = skybox_list[skybox2_list.currentRow()]
        skyboxlight = skybox_light_list[skybox2_list.currentRow()]
        skyboxangle = skybox_angle_list[skybox2_list.currentRow()]

        try:
            currentlight = currentlight.replace("world_idnum",str(world_id_num))
            currentlight = currentlight.replace("CURRENT_LIGHT",skyboxlight)
            currentlight = currentlight.replace("CURRENT_ANGLE",skyboxangle)
        except:
            QMessageBox.critical(self, "Error", "Please choose a skybox.")
            self.change_skybox()
        entity_list[0][levels] = currentlight
        latest_path = latest_path.replace(".ezm",".vmf")
        name = QFileDialog.getSaveFileName(self, "Export .vmf", latest_path, "Valve Map File (*.vmf)")
        file = open(name[0], "w")
        import export
        wholething = export.execute(totalblocks, entity_list, levels, skybox,skyboxgeolist)
        #print(wholething)
        file.write(wholething)
        file.close()
        popup = QMessageBox(self, "File Exported",
                                "The .vmf has been outputted to %s" %(name[0]) + " Open it in hammer to compile as a .bsp. Check out the wiki (https://github.com/baldengineers/easytf2_mapper/wiki/Texture-bug) for fixing errors with textures.")
        popup.setWindowTitle("File Exported")
        popup.setText("The .vmf has been outputted to %s" %(name[0]))
        popup.setInformativeText(" Open it in hammer to compile as a .bsp. Check out the wiki <a href=\"https://github.com/baldengineers/easytf2_mapper/wiki/Texture-bug\">here</a> for fixing errors with textures.")
        hammerButton = popup.addButton("Open Hammer",QMessageBox.ActionRole)
        exitButton = popup.addButton("OK",QMessageBox.ActionRole)
        popup.exec_()
        if popup.clickedButton() == hammerButton:
            self.open_hammer(1,name[0])
        if popup.clickedButton() == exitButton:
            popup.deleteLater()
            
    def removeButtons(self):

        for i in reversed(range(self.button_grid_layout.count())):
            widget = self.button_grid_layout.takeAt(i).widget()

            if widget is not None:
                widget.deleteLater()

        #for i in reversed(range(self.button_grid_layout.count())):
            #self.button_grid_layout.itemAt(i).widget().setParent(None)

        #for grid_button in grid_list:
            #grid_button.button.close()

        #self.clearlist()
        
    def grid_change(self,xvar,yvar,zvar,var,var2,var3):
        global totalblocks,entity_list,grid_list,iconlist
        if var2 == True:
            sxvar = xvar
            syvar = yvar
            szvar = zvar
        else:
            pass
        self.count = 0
        count_btns=0
        if var3 == True:
            try:
                del entity_list
                del totalblocks
                del iconlist
                del grid_list
                entity_list = []
                iconlist = []
                totalblocks = []
                grid_list = []
            except Exception as e:
                print(str(e))
                pass

        #gridsize_list = []
        self.btn_id_count = 0
        if var == True:
            self.window = QDialog(self)

            self.text = QLineEdit()
            self.text2 = QLineEdit()
            self.text3 = QLineEdit()

            self.okay_btn = QPushButton("OK",self)
            self.okay_btn.clicked.connect(lambda: self.grid_change_func(self.text.displayText(), self.text2.displayText(), self.text3.displayText()))

            self.form = QFormLayout()
            self.form.addRow("Set Grid Width:",self.text)
            self.form.addRow("Set Grid Height:",self.text2)
            self.form.addRow("Set Amount of Levels:",self.text3)
            self.form.addRow(self.okay_btn)

            self.window.setLayout(self.form)
            self.window.setWindowTitle("Set Grid Size")
            self.window.exec_()
        elif var2 == True:
            self.grid_change_func(sxvar,syvar,szvar)
            #print('test')
        '''
        text = QInputDialog.getText(self,("Get Grid Y"),
                                     ("Grid Height:"))                                    
        text2 = QInputDialog.getText(self,("Get Grid X"),
                                     ("Grid Width:"))
        '''

    def grid_change_func(self,x,y,z):
        level = 0
        levels = 1
        count_btns = 0
        self.count = 0
        global grid_y, grid_x, levels, file_loaded, currentfilename, level
        file_loaded = False
        try:
            self.window.deleteLater()
        except:
            pass

        try:
            self.grid_y = int(y)
            self.grid_x = int(x)
            levels = int(z)
        except ValueError:
            #TODO: Instead of a print statement, we need to bring up a window, alerting the user
            QMessageBox.critical(self.window, "Error", "Please enter a number.")
            self.grid_change(0,0,0,False,False,True)

        self.removeButtons()
        #self.removeDropdown()

        #print(self.grid_y)
        #print(self.grid_x)

        for z in range(levels):
            totalblocks.append([])
            entity_list.append([])
            iconlist.append([])
            self.btn_id_count=0
            count_btns=0
            #print(totalblocks)
        
            for x in range(self.grid_x):
                
                for y in range(self.grid_y):
                    totalblocks[z].append("") #This is so that there are no problems with replacing list values
                    
                    global count_btns
                    count_btns += 1
                    entity_list[z].append("")
                    iconlist[z].append("")
        for x in range(self.grid_x):
            for y in range(self.grid_y):
                grid_btn = GridBtn(self, x, y, self.btn_id_count)
                self.button_grid_layout.addWidget(grid_btn.button,y,x)
                self.btn_id_count += 1
                grid_list.append(grid_btn)
        entity_list.append("lighting slot")
        #pprint.pprint(totalblocks)

        #print(entity_list)        
        self.count += 1
        count_btns = self.grid_x*self.grid_y
        grid_y = self.grid_y
        grid_x = self.grid_x

        self.scrollArea.deleteLater()
        self.scrollArea = QScrollArea()
        self.scrollArea.setBackgroundRole(QPalette.Light)
        #self.scrollArea.setBackgroundRole(QPalette.Light)
        
        #self.scrollArea.setStyleSheet("background-color:transparent;")
        self.scrollArea.setStyleSheet("background-color: rgb(50, 50, 50, 100);")


        self.grid_widget = QWidget()
        self.grid_widget.setLayout(self.button_grid_layout)
        self.scrollArea.setWidget(self.grid_widget)
        self.scrollArea.ensureWidgetVisible(self.grid_widget)
        self.scrollArea.setWidgetResizable(True)
        
        #if not self.grid_y > 16 and not self.grid_x > 16:
            #self.scrollArea.setGeometry(QRect(0,0,self.grid_x*32+32, self.grid_y*32+32))
        self.button_grid_layout.setRowStretch(self.grid_y + 1, 1)
        self.button_grid_layout.setColumnStretch(self.grid_x + 1, 1)
            #self.button_grid_all.addStretch(1)
            #print('don\'t restrict size')
        '''
        elif self.grid_y > 16 and self.grid_x > 16:
            #self.scrollArea.setGeometry(QRect(0,0,16*32+32, 16*32+32))
            #print('restrict both')
            #self.button_grid_all.takeAt(2)
            pass
        elif self.grid_y > 16:
            self.button_grid_layout.setColumnStretch(self.grid_x + 1, 1)
            #self.scrollArea.setGeometry(QRect(0,0,self.grid_x*32+32, 16*32+32))
            #print('restrict y')
        elif self.grid_x > 16:
            self.button_grid_layout.setRowStretch(self.grid_y + 1, 1)
            #self.button_grid_all.addStretch(1)
            #self.scrollArea.setGeometry(QRect(0,0,16*32+32, self.grid_y*32+32))
        '''
        #self.scrollFrameLayout.addWidget(self.scrollArea)

        for i in range(levels):
            file = open("leveltemp/level" + str(i)+".tmp", "wb")
            pickle.dump(iconlist[i], file)
            file.close()
        
        self.gridLayout.addWidget(self.scrollArea)
        self.button_grid_all.addLayout(self.gridLayout)
        #print(grid_list)
        #print(iconlist)
        self.setWindowTitle("Easy TF2 Mapper ")
        return grid_list

    def change_light(self):
        r_input = QInputDialog.getText(self, ("Red light level 0-255"),
                                       ("Put in the red light ambiance level, 0-255:"))
        g_input = QInputDialog.getText(self, ("Green light level 0-255"),
                                       ("Put in the green light ambiance level, 0-255:"))
        b_input = QInputDialog.getText(self, ("Blue light level 0-255"),
                                       ("Put in the blue light ambiance level, 0-255:"))
        light_input = QInputDialog.getText(self, ("Brightness level"),
                                       ("Put in the brightness level desired:"))
        try:
            global r_input, g_input, b_input, light_input, world_id_num
            r_input = int(r_input[0])
            g_input = int(g_input[0])
            b_input = int(b_input[0])
            light_input = int(light_input[0])
            if r_input > 255 or g_input > 255 or b_input > 255:
                print("Error. Put in a number below 256 for each color input")
            else:
                pass
        except ValueError:
            QMessageBox.critical(self, "Error", "Please enter a number.")
            self.change_light()

        global currentlight
        currentlight = light_create.replacevalues(r_input,g_input,b_input,light_input,world_id_num)

    def change_skybox(self):
        self.window = QDialog(self)
        global skybox2_list
        skybox2_list = QListWidget()
        skybox2_list.setIconSize(QSize(200, 25))
        for index, text in enumerate(skybox_list):
            item = QListWidgetItem(QIcon(skybox_icon_list[index]), text)
            skybox2_list.addItem(item)
        
        self.layout = QHBoxLayout()
        self.layout.addWidget(skybox2_list)
        self.window.setGeometry(150,150,400,300)
        self.window.setWindowTitle("Choose a skybox")
        self.window.setWindowIcon(QIcon("icons\icon.ico"))

        self.window.setLayout(self.layout)
        skybox2_list.itemClicked.connect(self.window.close)
        self.window.exec_()
    '''
    def importprefabs(self):
        prefab_text_list = []
        prefab_icon_list = []
        prefab_list=[]
        prefab_file = open("prefab_template\prefab_list.txt")
        prefab_text_file = open("prefab_template\prefab_text_list.txt")
        prefab_icon_file = open("prefab_template\prefab_icon_list.txt")
        for line in prefab_file.readlines():
            prefab_list.append(line[:-1] if line.endswith("\n") else line)# need to do this because reading the file generates a \n after every line

        for line in prefab_text_file.readlines():
            prefab_text_list.append(line[:-1] if line.endswith("\n") else line)

        for line in prefab_icon_file.readlines():
            prefab_icon_list.append(line[:-1] if line.endswith("\n") else line)

        for file in [prefab_file, prefab_text_file, prefab_icon_file]:
            file.close()
        for item in prefab_list:
            globals()[item] = importlib.import_module(item)
            print("import", item)
        self.home()
    '''
    #fix this later, it has a breaking bugs if it works

    def close_application(self):
        choice = QMessageBox.question(self, "Exit",
                                      "Are you sure you want to exit?",
                                      QMessageBox.Yes | QMessageBox.No,
                                      QMessageBox.No)
        if choice == QMessageBox.Yes:
            folder = 'leveltemp/'
            for f in os.listdir(folder):
                if "level" in f: 
                    print("removing", f)
                    os.remove(folder+f)
                
            sys.exit()
        else:
            pass

    def create_prefab(self):
        '''
        name = QFileDialog.getOpenFileName(self, "Choose .vmf File", "/","*.vmf")
        prefab_icon = QFileDialog.getOpenFileName(self, "Choose Prefab Icon", "/","*.jpg")
        prefab_name = QInputDialog.getText(self,"Prefab Name",
                                     "Name of Prefab (e.g. wall_prefab):")
        prefab_text = QInputDialog.getText(self, "Prefab Text",
                                           "Prefab Text (e.g. Wall Tile)")
        '''
        
        self.window = QDialog(self)
        self.textLineEdit = QLineEdit()
        self.nameLineEdit = QLineEdit()
        
        self.vmfTextEdit = QLineEdit()
        self.iconTextEdit = QLineEdit()
        
        self.vmfBrowse = QPushButton("Browse",self)
        self.vmfBrowse.clicked.connect(lambda: self.vmfTextEdit.setText(QFileDialog.getOpenFileName(self, "Choose .vmf File", "/","*.vmf")[0]))
        
        self.iconBrowse = QPushButton("Browse",self)
        self.iconBrowse.clicked.connect(lambda: self.iconTextEdit.setText(QFileDialog.getOpenFileName(self, "Choose .jpg File", "/","*.jpg")[0]))

        self.vmfLayout = QHBoxLayout()
        self.vmfLayout.addWidget(self.vmfTextEdit)
        self.vmfLayout.addWidget(self.vmfBrowse)
        self.vmfBrowse.setWindowModality(Qt.NonModal)
        
        self.iconLayout = QHBoxLayout()
        self.iconLayout.addWidget(self.iconTextEdit)
        self.iconLayout.addWidget(self.iconBrowse)

        self.okay_btn = QPushButton("Create Prefab", self)
        #self.okay_btn.setFixedSize(100,25)

        self.blankstring = QWidget()

        self.okay_btn_layout = QHBoxLayout()
        self.okay_btn_layout.addStretch(1)
        self.okay_btn_layout.addWidget(self.okay_btn)

        self.okay_btn.clicked.connect(self.create_run_func)

        self.rotCheckBox = QCheckBox()
        self.expCheckBox = QCheckBox()
        self.buggyText = QLabel("This is a pretty buggy tool at this point, and is mostly used by developers. Are you sure you want to do this? \n(exported prefabs can be found in the main directory, where the executable is.")

        
        
        self.form = QFormLayout()
        self.form.addRow(self.buggyText)
        self.form.addRow("Prefab Text:", self.textLineEdit)
        self.form.addRow("Prefab Name:", self.nameLineEdit)
        self.form.addRow("VMF file (.vmf):", self.vmfLayout)
        self.form.addRow("Icon (.jpg):", self.iconLayout)
        self.form.addRow("Make Rotations?", self.rotCheckBox)
        self.form.addRow("Export prefab?", self.expCheckBox)
        for i in range(5):
            self.form.addRow(self.blankstring)
        self.form.addRow(self.okay_btn_layout)

        
        self.window.setGeometry(150,150,400,300)
        self.window.setWindowTitle("Create Prefab")
        self.window.setWindowIcon(QIcon("icons\icon.ico"))
        #self.window.setWindowModality(Qt.WindowModal)

        self.window.setLayout(self.form)
        self.window.exec_()

    def create_run_func(self):
        name_str = self.nameLineEdit.displayText().replace(' ','_')
        form_list,t_list = [self.vmfTextEdit.displayText(),self.textLineEdit.displayText(),self.iconTextEdit.displayText(),self.nameLineEdit.displayText()],[]
        form_dict = {1:'Prefab Text',2:'Prefab Name',3:'VMF file',4:'Icon'}
        if self.vmfTextEdit.displayText() !=  '' and self.textLineEdit.displayText() != '' and self.iconTextEdit.displayText() != '' and self.nameLineEdit.displayText() != '':
            QMessageBox.information(self, "Files Created, restart to see the prefab.",
                                                                          createPrefab.create(self.vmfTextEdit.displayText(), name_str,
                                                                            self.textLineEdit.displayText(), self.iconTextEdit.displayText(), self.rotCheckBox.isChecked(),self.expCheckBox.isChecked()))
            restart_btn = QPushButton("Restart")
            later_btn = QPushButton("Later")
            choice = QMessageBox(self)
            choice.setIcon(QMessageBox.Question)
            choice.setWindowTitle("Prefab Successfully Created")
            choice.setText("Program must be restarted for changes to take effect.")
            choice.setInformativeText("Restart? You will lose any unsaved progress.")
            choice.addButton(restart_btn, QMessageBox.YesRole)
            choice.addButton(later_btn, QMessageBox.NoRole)
            choice.setDefaultButton(later_btn)
            #print(choice.exec_())                  
            if choice.exec_() == 0:
                try:
                    subprocess.Popen('EasyTF2Mapper.exe')
                except:
                    subprocess.Popen('python main.py')
                sys.exit()
            else:
                pass  
        else:
            for index,box in enumerate(form_list):         
                if box == '':          
                    t_list.append(form_dict[index+1])
            err = ", ".join(t_list)
            QMessageBox.critical(self, "Error", "Fill out all sections of the form. ("+err+")")
        #self.importprefabs()

    def import_prefab(self):
        name = QFileDialog.getOpenFileName(self, "Import Zipped Prefab", latest_path,"*.zip")[0]
        prefab_zip = zipfile.ZipFile(name).extractall("")

        with open("info.txt", "r+") as f:
            zip_info = f.readlines()
            with open('prefab_template/rot_prefab_list.txt',"a") as d:
                tempfil = zip_info[0]
                tempfil = tempfil.replace('\n','')
                d.write(tempfil+"_icon_list.txt\n")
            with open('prefab_template/prefab_list.txt',"a") as d:
                tempfil = zip_info[0]
                tempfil = tempfil.replace('\n','')
                d.write(tempfil+'\n')
            with open('prefab_template/prefab_text_list.txt',"a") as d:
                d.write(zip_info[2])
            with open('prefab_template/prefab_icon_list.txt',"a") as d:
                tempfil = zip_info[1]
                tempfil = tempfil.replace('\n','')
                d.write('icons/'+tempfil+'_right.jpg\n')

        os.remove("info.txt")
        
        restart_btn = QPushButton("Restart")
        later_btn = QPushButton("Later")
        choice = QMessageBox(self)
        choice.setIcon(QMessageBox.Question)
        choice.setWindowTitle("Prefab Successfully Imported")
        choice.setText("Program must be restarted for changes to take effect.")
        choice.setInformativeText("Restart? You will lose any unsaved progress.")
        choice.addButton(restart_btn, QMessageBox.YesRole)
        choice.addButton(later_btn, QMessageBox.NoRole)
        choice.setDefaultButton(later_btn)                 
        if choice.exec_() == 0:
            try:
                subprocess.Popen('EasyTF2Mapper.exe')
            except:
                subprocess.Popen('python main.py')
            sys.exit()
        else:
            pass  
        

    def open_console(self):
        #contains dev console where you can manually run functions

        self.console = QDialog()
        self.console.setWindowTitle("Developer Console")

        self.prev_text = QTextEdit("<Bald Engineers Developer Console>")
        self.prev_text.setText('''Developer console for Easy TF2 Mapper version beta 2.6.5. Current commands are:
print <variable>, setlevel <int>, help, restart, exit, func <function>, wiki, py <python function>.\n''')
        self.prev_text.setReadOnly(True)
        
        self.curr_text = QLineEdit()
        self.curr_text_btn = QPushButton("Enter")
        self.curr_text_btn.clicked.connect(self.console_enter)
        
        self.curr_text_layout = QHBoxLayout()
        self.curr_text_layout.addWidget(self.curr_text)
        self.curr_text_layout.addWidget(self.curr_text_btn)
        
        self.console_close_btn = QPushButton("Close")
        self.console_close_btn.clicked.connect(self.console.close)
        
        self.console_form = QFormLayout()
        self.console_form.addRow(self.prev_text)
        self.console_form.addRow(self.curr_text_layout)
        self.console_form.addRow(self.console_close_btn)

        
        self.console.setLayout(self.console_form)
        self.console.show()

    def console_enter(self):
        global level, levels

        """
        try:
            self.prev_text.setText(eval(self.curr_text.displayText()))
        except Exception as e:
            self.prev_text.setText(str(e))
        """
        
            
        command = ""
        char_num = 0
        text = self.curr_text.displayText()
        text_prefix = text + " --> "
        
        '''
        for letter in text:
            if letter != " ":
                command += letter
                char_num += 1
            else:
                break
        '''
        command = text.split()[0]
        
        try:
            value = text.split()[1]
        except IndexError:
            value = ""

        if command == "print":
            #print_var = ""

            #for letter in text[char_num:]:
            #    print_var += letter
                
            try:
                new_text = text_prefix + str(eval(value))
            except Exception as e:
                new_text = text_prefix + str(e)

        elif command == "setlevel":
            try:
                if int(value)-1 < int(levels):
                    level = int(value)-1
                    self.level.setText("Level: " + str(level+1))
                    new_text = text_prefix + "Level set to "+str(value+".")
                else:
                    new_text = text_prefix + "Level "+str(value+" is out of range.")
            except Exception as e:
                new_text = text_prefix + str(e)

        elif command == "help":
            new_text = text_prefix + '''Developer console for Easy TF2 Mapper version beta 2.6.5. Current commands are: print <variable>, func <function>, setlevel <int>, help, restart, exit, func <function>, wiki, py <python function>'''

        elif command == "exit":
            self.close_application()
            
        elif command == "restart":
            try:
                subprocess.Popen('EasyTF2Mapper.exe')
            except:
                subprocess.Popen('python main.py')
            self.close_application()

        elif command == "pootis":
            new_text = '<img src="icons/thedoobs.jpg">'

        elif command == "sterries" or command == "jerries":
            new_text = text_prefix + "Gimme all those berries, berries, berries!"
            

        elif command == "sideshow":
            new_text = ''
            self.sideshow()
        elif command == "func":
            #function_var = ""

            #for letter in text[char_num:]:
            #    function_var += letter
            try:
                eval("self."+value + "()")
                new_text = text_prefix + "Function "+value+" has been run."
            except Exception as e:
                new_text = text_prefix + str(e)

        elif command == "wiki":
            try:
                webbrowser.open("http://github.com/baldengineers/easytf2_mapper/wiki")
                new_text = text_prefix + "Wiki has been opened in your default browser"
            except Exception as e:
                print(str(e))
                
        elif command == "py":
            try:
                new_text = text_prefix + str(eval(value))
            except Exception as e:
                new_text = text_prefix + str(e)
        else:
            new_text = text_prefix + "\"" + command + "\" is not a valid command"

        self.prev_text.append(new_text)
        self.curr_text.setText("")

    def sideshow(self):
        self.sideshowwindow = QLabel()
        movie = QMovie("icons/sideshow.gif")
        self.sideshowwindow.setMovie(movie)
        self.sideshowwindow.setGeometry(350,262,154,103)
        self.sideshowwindow.setWindowTitle("SIDESHOW")
        self.sideshowwindow.setWindowIcon(QIcon("icons/ss.ico"))
        self.sideshowwindow.show()

        movie.start()

    def heavy(self):
        self.heavywindow = QLabel()
        movie = QMovie("icons/heavy.gif")
        self.heavywindow.setMovie(movie)
        self.heavywindow.setGeometry(350,262,150,99)
        self.heavywindow.setWindowTitle("DANCE HEAVY DANCE!")
        self.heavywindow.show()

        movie.start()

#define some global variables
level = 0
id_num = 1
rotation = 0
world_id_num = 2
entity_num = 1
toggle = 0
btn_id_count = 0
grid_list=[]
totalblocks = []
skybox_list=[]
skybox_light_list=[]
iconlist = []
skybox_angle_list=[]
skybox_icon_list=[]
prefab_list = []
gridsize_list = []
count_btns = 0
entity_list=[]
prefab_text_list = []
prefab_icon_list = []
openblocks=[]
placeholder_list = []
currentfilename='Untitled'
file_loaded = False
current_loaded = ''
latest_path='/'
currentlight = '''
entity
{
    "id" "world_idnum"
    "classname" "light_environment"
    "_ambient" "255 255 255 100"
    "_ambientHDR" "-1 -1 -1 1"
    "_AmbientScaleHDR" "1"
    "_light" "CURRENT_LIGHT"
    "_lightHDR" "-1 -1 -1 1"
    "_lightscaleHDR" "1"
    "angles" "CURRENT_ANGLE"
    "pitch" "0"
    "SunSpreadAngle" "0"
    "origin" "0 0 73"
    editor
    {
        "color" "220 30 220"
        "visgroupshown" "1"
        "visgroupautoshown" "1"
        "logicalpos" "[0 500]"
    }
}
'''
skybox = 'sky_tf2_04'
batchtext = '''
set ftypename=Easy TF2 Mapper Save
set extension=.ezm
set pathtoexe="EasyTF2Mapper.exe"
set pathtoicon="icons/icon.ico"

if %pathtoicon%=="" set pathtoicon=%pathtoexe%,0
REG ADD HKEY_CLASSES_ROOT\%extension%\ /t REG_SZ /d %ftypename% /f
REG ADD HKLM\SOFTWARE\Classes\%ftypename%\DefaultIcon\ /t REG_SZ /d %pathtoicon% /f
ftype %ftypename%=%pathtoexe% "%%1" %%*
assoc %extension%=%ftypename%
'''
#skyboxlight = '255 255 255 200'
#skyboxangle = '0 0 0'
#if the user does not change the lighting, it sticks with this.
#if the user does not choose a skybox it sticks with this

prefab_file = open("prefab_template/prefab_list.txt")
prefab_text_file = open("prefab_template/prefab_text_list.txt")
prefab_icon_file = open("prefab_template/prefab_icon_list.txt")

skybox_file = open("prefab_template/skybox_list.txt")
skybox_icon = open("prefab_template/skybox_icons.txt")
skybox_light = open("prefab_template/skybox_light.txt")
skybox_angle = open("prefab_template/skybox_angle.txt") 

for line in prefab_file.readlines():
    prefab_list.append(line[:-1] if line.endswith("\n") else line)# need to do this because reading the file generates a \n after every line

for line in prefab_text_file.readlines():
    prefab_text_list.append(line[:-1] if line.endswith("\n") else line)

for line in prefab_icon_file.readlines():
    prefab_icon_list.append(line[:-1] if line.endswith("\n") else line)

for line in skybox_file.readlines():
    skybox_list.append(line[:-1] if line.endswith("\n") else line)# need to do this because reading the file generates a \n after every line

for line in skybox_icon.readlines():
    skybox_icon_list.append(line[:-1] if line.endswith("\n") else line)

for line in skybox_light.readlines():
    skybox_light_list.append(line[:-1] if line.endswith("\n") else line)

for line in skybox_angle.readlines():
    skybox_angle_list.append(line[:-1] if line.endswith("\n") else line)
    
for file in [prefab_file, prefab_text_file, prefab_icon_file,skybox_file,skybox_icon,skybox_angle,skybox_light]:
    file.close()

#imports that need prefab_list to be defined

for item in prefab_list:
    globals()[item] = importlib.import_module(item)
    print("import", item)
print("\n~~~~~~~~~~~~~~~~~~~~~\nMapper loaded! You may have to alt-tab to find the input values dialog.\n")
global rotation
#Main Program
app = QApplication(sys.argv)
gui = MainWindow()




app.exec_()
