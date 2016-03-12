#use blocks to create maps
import sys
sys.path.append("prefabs/")
import os.path
from PySide.QtCore import *
from PySide.QtGui import *
import importlib
import createPrefab
from PIL import Image
import generateSkybox
import light_create
import subprocess
import pickle
'''check todo every time you open this'''
#TODO: more prefabs, mo betta
class GridBtn(QWidget):
    def __init__(self, self_global, x, y, btn_id):
        super(GridBtn, self).__init__()
        self.button = QPushButton("", self_global)
        self.x = 32*x
        self.y = 20+(32*y)
        self.button.move(self.x,self.y)
        self.button.resize(32,32)
        self.button.setFixedSize(32, 32)
        self.button.pressed.connect(lambda: self.click_func(self_global, x, y,
                                                            btn_id))
        self.button.setMouseTracking(True)
        self.button.installEventFilter(self)
        self.button.show()

    def reset_icon(self):
        self.button.setIcon(QIcon())

    def click_func(self, self_global, x, y, btn_id):
        self.checkForAlt()
        global rotation
        if toggle != 0:
            self.button.setIcon(QIcon())
            totalblocks[btn_id] = 'EMPTY_SLOT'
            entity_list[btn_id] = 'NO_ENTITY'
            iconlist[btn_id] = ''
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
            #print(totalblocks)
            #print(btn_id)
            #eval() turns the string into a variable name.
            moduleName = eval(prefab_list[self_global.tile_list.currentRow()])
            #print(rotation)
            try:
                try:
                    try:
                        create = moduleName.createTile(x, y, id_num, world_id_num, entity_num, placeholder_list, rotation)
                    except Exception as e:
                        print(str(e))
                        create = moduleName.createTile(x, y, id_num, world_id_num)
                except Exception as e:
                    print(str(e))
                    create = moduleName.createTile(x, y, id_num, world_id_num, entity_num, placeholder_list)
            except Exception as e:
                create = moduleName.createTile(x, y, id_num, world_id_num, rotation)
                print(str(e))
            #create = test_prefab.createTile(x, y, id_num, world_id_num)
            id_num = create[1]
            world_id_num = create[2]
            try:
                entity_num = create[3]
                placeholder_list = create[5]
                #print("placeholder list: ", placeholder_list)
            except IndexError:
                pass
            #if self_global.comboBox.currentIndex() != 0:
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
                current_prefab_icon_list = current_prefab_icon_list[self_global.tile_list.currentRow()]
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
                icon = prefab_icon_list[self_global.tile_list.currentRow()]
                self.button.setIcon(QIcon(icon))
                self.button.setIconSize(QSize(32,32))


            totalblocks[btn_id] = create[0]
            iconlist[btn_id] = icon
            try:
                entity_list[btn_id] = create[4]
            except:
                pass

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
        saveAction.setStatusTip("Save File as .vmf")
        saveAction.triggered.connect(self.file_save)

        newAction = QAction("&New", self)
        newAction.setShortcut("Ctrl+n")
        newAction.setStatusTip("Create a New File")
        #newAction.triggered.connect()

        hammerAction = QAction("&Open Hammer",self)
        hammerAction.setShortcut("Ctrl+H")
        hammerAction.setStatusTip("Opens up Hammer.")
        hammerAction.triggered.connect(lambda: self.open_hammer(0,"null"))

        changeLightAction = QAction("&Change Lighting", self)
        changeLightAction.setShortcut("Ctrl+J")
        changeLightAction.setStatusTip("Change the environment lighting of the map.")
        changeLightAction.triggered.connect(self.change_light)
        
        exportAction = QAction("&Export", self)
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
        gridAction.triggered.connect(lambda: self.grid_change(0,0,True,False,True))

        createPrefabAction = QAction("&Prefab", self)
        createPrefabAction.setShortcut("Ctrl+I")
        createPrefabAction.setStatusTip("View the readme for a good idea on formatting Hammer Prefabs.")
        createPrefabAction.triggered.connect(self.create_prefab)

        #refreshPrefab = QAction("&Refresh Prefab List", self)
        #refreshPrefab.setStatusTip("Refresh the list of prefabs, done after creating a new one.")
        #refreshPrefab.triggered.connect(self.importprefabs)

        changeSkybox = QAction("&Change Skybox", self)
        changeSkybox.setStatusTip("Change the skybox of the map.")
        changeSkybox.setShortcut("Ctrl+B")
        changeSkybox.triggered.connect(self.change_skybox)
        self.statusBar()
        
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu("&File")
        optionsMenu = mainMenu.addMenu("&Options")
        createMenu = mainMenu.addMenu("&Create")
        
        #fileMenu.addAction(newAction)
        fileMenu.addAction(openAction)
        fileMenu.addAction(saveAction)
        fileMenu.addAction(exportAction)
        fileMenu.addAction(exitAction)
        fileMenu.addAction(hammerAction)

        optionsMenu.addAction(gridAction)
        optionsMenu.addAction(changeSkybox)
        optionsMenu.addAction(removeAction)
        
        createMenu.addAction(createPrefabAction)
        
        self.home()
        self.change_skybox()
    def open_hammer(self,loaded,file):
        self.open_file()
        if "loaded_first_time" not in self.files:
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

                
                QMessageBox.critical(self, "Error", "Hammer executable/batch moved or renamed!")
                self.file.close()
                os.remove("startupcache/startup.su")
                self.open_hammer(0,"null")
    def open_file(self):
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
            self.remove_prefab()
        removeText.reset(num)

    def closeEvent(self, event):
        #closeEvent runs close_application when the x button is pressed
        event.ignore()
        self.close_application()
        
    def home(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        #self.labelLayout = QHBoxLayout(self)

        self.scrollArea = QScrollArea(self)
        self.scrollArea.setBackgroundRole(QPalette.Light)


    
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



        self.buttonLabel = QLabel("Rotation:",self)
        #self.currentLabel = QLabel("Current Rotation:",self)
        self.listLabel = QLabel("List of prefabs:",self)
        self.gridLabel = QLabel("Grid:",self)

        #self.labelLayout.addWidget(self.gridLabel)
        #self.labelLayout.addWidget(self.listLabel)
        #self.labelLayout.setContentsMargins(0,0,0,0)
        #self.labelLayout.setSpacing(10)

        self.current = QPushButton("",self)
        self.current.setIcon(QIcon(''))
        self.current.setIconSize(QSize(40,40))
        self.current.setFixedSize(QSize(40,40))

        self.level = QPushButton(self)
        self.level.setText("Level:")
        self.level.setFixedSize(QSize(150,30))
        self.level.clicked.connect(self.level_select)
        self.rotateCW = QPushButton("",self)
        self.rotateCW.setIcon(QIcon('icons/rotate_cw.jpg'))
        self.rotateCW.setIconSize(QSize(40,40))
        self.rotateCW.setFixedSize(QSize(40,40))

        self.rotateCCW = QPushButton("",self)
        self.rotateCCW.setIcon(QIcon('icons/rotate_ccw.jpg'))
        self.rotateCCW.setIconSize(QSize(40,40))
        self.rotateCCW.setFixedSize(QSize(40,40))

        #sets rotation value. 0 = right, 1 = down, 2 = left, 3 = right
        self.rotateCW.clicked.connect(lambda:self.rotateCW_func())
        self.rotateCCW.clicked.connect(lambda:self.rotateCCW_func())
        
        self.button_rotate_layout = QHBoxLayout()
        self.button_rotate_layout.addWidget(self.buttonLabel)
        self.button_rotate_layout.addWidget(self.rotateCCW)
        #self.button_rotate_layout.addWidget(self.currentLabel)
        self.button_rotate_layout.addWidget(self.current)
        self.button_rotate_layout.addWidget(self.rotateCW)
        self.button_rotate_layout.addWidget(self.level)

        self.button_rotate_layout.addStretch(1)
                               
        self.tile_list = QListWidget()
        self.tile_list.setMaximumWidth(200)


        
        for index, text in enumerate(prefab_text_list):
            item = QListWidgetItem(QIcon(prefab_icon_list[index]), text)
            self.tile_list.addItem(item)

        self.tile_list.currentItemChanged.connect(self.changeIcon)
        #contains label and list vertically
        self.tile_list_layout = QVBoxLayout()
        self.tile_list_layout.addWidget(self.listLabel)
        self.tile_list_layout.addWidget(self.tile_list)
        
        self.button_grid_layout = QGridLayout()
        self.button_grid_layout.setSpacing(0)
        #self.layout_grid = QBoxLayout()
        
        self.grid_widget = QWidget()
        self.grid_widget.setLayout(self.button_grid_layout)
        self.scrollArea.setWidget(self.grid_widget)
        self.scrollArea.ensureWidgetVisible(self.grid_widget)
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
            self.popup = QMessageBox(self)
            self.popup.setGeometry(100,100,500,250)
            self.popup.setWindowTitle("First Launch")
            self.popup.setInformativeText("You haven't launched this before! Try looking at the <a href=\"https://github.com/baldengineers/easytf2_mapper/wiki/Texture-bug\">wiki</a> for help!")
            self.popup.setText("First Launch!")
            self.popup.exec_()
            f.write("startup")
            f.close
        else:
            pass
        
        self.grid_change(0,0,True, False, True)
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

        #testing
        levels = 3
        #
        self.levellist = QListWidget()
        self.levellist.setIconSize(QSize(200, 25))
        try:
            for i in range(levels-1):
                item = QListWidgetItem(QIcon("icons/level.jpg"),"Level "+str(i))
                self.levellist.addItem(item)
        except Exception as e:
            print(str(e))
            pass
        self.layoutl = QHBoxLayout()
        self.layoutl.addWidget(self.levellist)
        self.windowl.setGeometry(150,150,400,300)
        self.windowl.setWindowTitle("Choose a level")
        self.windowl.setWindowIcon(QIcon("icons/icon.ico"))
        self.windowl.setLayout(self.layoutl)
        self.windowl.exec_()
        

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

 
        
        
    def file_open(self):
        global grid_list
        name = QFileDialog.getOpenFileName(self, "Open File", "/","*.ezm")
        file = open(name[0], "rb")
        #del totalblocks, entity_list,iconlist,grid_list
        iconlist=[]
        while True:
            #try:
            header = pickle.load(file)
            if "grid_size" in header:
                openlines = pickle.load(file)
                self.grid_change(openlines[0],openlines[1],False, True, True)
            elif "totalblocks" in header:
                openlines = pickle.load(file)
                for item in openlines:
                    totalblocks.append(item)
            elif "entity_list" in header:
                openlines = pickle.load(file)
                for item in openlines:
                    entity_list.append(item)
            elif "icon_list" in header:
                global grid_list
                openlines = pickle.load(file)
                print(openlines)
                for item in openlines:
                    iconlist.append(item)
                for index, icon in enumerate(iconlist):
                    #print(iconlist)
                    if "icons" in icon:
                        print(index)
                        grid_list[index].button.setIcon(QIcon(icon))
                        grid_list[index].button.setIconSize(QSize(32,32))
            elif "skybox2_list" in header:
                openlines = pickle.load(file)
                skybox2_list.setCurrentRow(openlines)
            else:
                #print('breaking (bad) XD')
                break
            #except Exception as e:
                #print(e)
                #break
        self.change_skybox()
        #print("totalblocks: ", totalblocks)
        #print("entity_list: ", entity_list)
        #openlines = file.readlines()
        #openlinesstr = "".join(openlines)
        file.close()
        
        #now, it imports the vmf, and has two versions of it; the importlines which has each
        #line as a string in a list, and importlinesstr, which makes it one big string
            
    def file_save(self):
        global grid_x, grid_y, iconlist
        gridsize_list = (grid_x,grid_y)
        skybox_sav = skybox2_list.currentRow()
        name = QFileDialog.getSaveFileName(self, "Save File", "/", "*.ezm")
        file = open(name[0], "wb")
        level = 1 #change this to actually do something once we add levels
        pickle.dump("<grid_size>", file)
        pickle.dump(gridsize_list, file)
        pickle.dump("<totalblocks_l%d>" %(level), file)
        pickle.dump(totalblocks, file)
        pickle.dump("<entity_list_l%d>" %(level), file)
        pickle.dump(entity_list, file)
        pickle.dump("<icon_list_l%d>" %(level), file)
        pickle.dump(iconlist, file)
        print(iconlist)
        pickle.dump("<skybox>", file)
        pickle.dump(skybox_sav, file)
        #text = self.textEdit.toPlainText()
        #file.write(text)
        file.close()
        QMessageBox.information(self, "File Saved", "File saved as %s" %(name[0]))
        

    def file_export(self):
        global id_num, grid_y, grid_x, world_id_num, count_btns, currentlight, skybox, skybox2_list, entity_list, skybox_light_list, skybox_angle_list
        skyboxgeolist = []
        skyboxz = QInputDialog.getText(self,("Set Skybox Height"),("Skybox Height(hammer units, 512 minimum recommended):"))
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
        entity_list[count_btns] = currentlight
        name = QFileDialog.getSaveFileName(self, "Export .vmf", "output/", "Valve Map File (*.vmf)")
        file = open(name[0], "w")
        import export
        wholething = export.execute(totalblocks, entity_list, skybox,skyboxgeolist)
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
        
    def grid_change(self,xvar,yvar,var,var2,var3):
        global totalblocks,entity_list,grid_list,iconlist
        if var2 == True:
            sxvar = xvar
            syvar = yvar
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

            self.okay_btn = QPushButton("OK",self)
            self.okay_btn.clicked.connect(lambda: self.grid_change_func(self.text.displayText(), self.text2.displayText()))

            self.form = QFormLayout()
            self.form.addRow("Set Grid Width:",self.text)
            self.form.addRow("Set Grid Height:",self.text2)
            self.form.addRow(self.okay_btn)

            self.window.setLayout(self.form)
            self.window.setWindowTitle("Set Grid Size")
            self.window.exec_()
        elif var2 == True:
            self.grid_change_func(sxvar,syvar)
            #print('test')
        '''
        text = QInputDialog.getText(self,("Get Grid Y"),
                                     ("Grid Height:"))                                    
        text2 = QInputDialog.getText(self,("Get Grid X"),
                                     ("Grid Width:"))
        '''
    def grid_change_func(self,x,y):
        count_btns = 0
        self.count = 0
        global grid_y, grid_x
        try:
            self.window.deleteLater()
        except:
            pass

        try:
            self.grid_y = int(y)
            self.grid_x = int(x)
        except ValueError:
            #TODO: Instead of a print statement, we need to bring up a window, alerting the user
            QMessageBox.critical(self.window, "Error", "Please enter a number.")
            self.grid_change(0,0,False,False,True)

        self.removeButtons()
        #self.removeDropdown()

        #print(self.grid_y)
        #print(self.grid_x)

        for x in range(self.grid_x):
            for y in range(self.grid_y):
                #print("test") #testing if works
                grid_btn = GridBtn(self, x, y, self.btn_id_count)
                self.button_grid_layout.addWidget(grid_btn.button,y,x) #needs to be like this because grid_layout is counter-intuitive
                #self.button_grid_layout.setColumnMinimumWidth(y, 32)
                #self.layout_grid.addWidget(grid_btn.button,x,y)
                
                grid_list.append(grid_btn)
                totalblocks.append("EMPTY_SLOT") #This is so that there are no problems with replacing list values
                self.btn_id_count += 1
                global count_btns
                count_btns += 1
                entity_list.append("NO_ENTITY")
                iconlist.append("")
            #self.button_grid_layout.setRowMinimumHeight(x, 32)
        entity_list.append("lighting slot")
        #print(totalblocks)

        #print(entity_list)        
        self.count += 1
        grid_y = self.grid_y
        grid_x = self.grid_x

        self.scrollArea.deleteLater()
        self.scrollArea = QScrollArea(self)
        self.scrollArea.setBackgroundRole(QPalette.Light)

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


        
        self.gridLayout.addWidget(self.scrollArea)
        self.button_grid_all.addLayout(self.gridLayout)
        #print(grid_list)
        #print(iconlist)
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
            sys.exit()
        else:
            pass

    def create_prefab(self):
        '''
        name = QFileDialog.getOpenFileName(self, "Choose .vmf File", "C:/","*.vmf")
        prefab_icon = QFileDialog.getOpenFileName(self, "Choose Prefab Icon", "C:/","*.jpg")
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
        self.vmfBrowse.clicked.connect(lambda: self.vmfTextEdit.setText(QFileDialog.getOpenFileName(self, "Choose .vmf File", "C:/","*.vmf")[0]))
        
        self.iconBrowse = QPushButton("Browse",self)
        self.iconBrowse.clicked.connect(lambda: self.iconTextEdit.setText(QFileDialog.getOpenFileName(self, "Choose .jpg File", "C:/","*.jpg")[0]))

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

        self.okay_btn.clicked.connect(lambda: self.create_run_func())

        self.rotCheckBox = QCheckBox()
        
        
        self.form = QFormLayout()
        self.form.addRow("Prefab Text:", self.textLineEdit)
        self.form.addRow("Prefab Name:", self.nameLineEdit)
        self.form.addRow("VMF file (.vmf):", self.vmfLayout)
        self.form.addRow("Icon (.jpg):", self.iconLayout)
        self.form.addRow("Make Rotations?", self.rotCheckBox)
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

        self.ext_list = ["_right.jpg","_down.jpg","_left.jpg","_up.jpg"]
        self.icondir = str(self.nameLineEdit.displayText())
        with open("prefab_template/rot_prefab_list.txt", "a") as g:
            g.write(self.icondir+"_icon_list.txt\n")
        g.close()
        self.imageRot = Image.open(self.iconTextEdit.displayText())
        self.imageRot.save("icons/"+self.icondir+"_right.jpg")
        self.imageRot2 = Image.open(self.iconTextEdit.displayText())
        self.imageRot2 = self.imageRot2.rotate(270)
        self.imageRot2.save("icons/"+self.icondir+"_down.jpg")
        self.imageRot3 = Image.open(self.iconTextEdit.displayText())
        self.imageRot3 = self.imageRot3.rotate(180)
        self.imageRot3.save("icons/"+self.icondir+"_left.jpg")
        self.imageRot4 = Image.open(self.iconTextEdit.displayText())
        self.imageRot4 = self.imageRot4.rotate(90)
        self.imageRot4.save("icons/"+self.icondir+"_up.jpg")
        f = open("prefab_template/iconlists/"+self.icondir+"_icon_list.txt","w+")
        for i in self.ext_list:
            f.write("icons/"+self.icondir+i+"\n")
        f.close()
        
        QMessageBox.information(self, "Files Created, restart to see the prefab.",
                                                                      createPrefab.create(self.vmfTextEdit.displayText(), self.nameLineEdit.displayText(),
                                                                        self.textLineEdit.displayText(), self.iconTextEdit.displayText(), self.rotCheckBox.isChecked()))
        
        
        
        #self.importprefabs()

#define some global variables
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
placeholder_list = []
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
#skyboxlight = '255 255 255 200'
#skyboxangle = '0 0 0'
#if the user does not change the lighting, it sticks with this.
#if the user does not choose a skybox it sticks with this

prefab_file = open("prefab_template\prefab_list.txt")
prefab_text_file = open("prefab_template\prefab_text_list.txt")
prefab_icon_file = open("prefab_template\prefab_icon_list.txt")

skybox_file = open("prefab_template\skybox_list.txt")
skybox_icon = open("prefab_template\skybox_icons.txt")
skybox_light = open("prefab_template\skybox_light.txt")
skybox_angle = open("prefab_template\skybox_angle.txt") 

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
global rotation
#Main Program
app = QApplication(sys.argv)
gui = MainWindow()
app.exec_()
