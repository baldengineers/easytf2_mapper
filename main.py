#use blocks to create maps
import sys
import os.path
from PySide.QtCore import *
from PySide.QtGui import *
import importlib
import createPrefab
import light_create
'''check todo every time you open this'''
#TODO: more prefabs when the entitiy prefab is done
#TODO: THE CREATEPREFAB NEEDS TO ADD THE ENTITIES PART OF A CUSTOM PREFAB
#TODO: TEXTURES JESUS CHRIST ITS AN EYESORE IN HAMMER
#TODO: skybox modeling. choosing a skybox is done.

class GridBtn(QWidget):
    def __init__(self, self_global, x, y, btn_id):
        super(GridBtn, self).__init__()
        self.button = QPushButton("", self_global)
        self.x = 32*x
        self.y = 20+(32*y)
        #self.button.move(self.x,self.y)
        #self.button.resize(32,32)
        self.button.setFixedSize(32, 32)
        self.button.clicked.connect(lambda: self.click_func(self_global, x, y,
                                                            btn_id))
        self.button.show()

    def reset_icon(self):
        self.button.setIcon(QIcon())

    def click_func(self, self_global, x, y, btn_id):
        self.checkForAlt()
        if toggle != 0:
            self.button.setIcon(QIcon())
            totalblocks[btn_id] = 'EMPTY_SLOT'
            entity_list[btn_id] = 'NO_ENTITY'
        else:
            print((x,y))
            global world_id_num
            global id_num
            global entity_num
            global entity_list
            global placeholder_list
            #eval() turns the string into a variable name.
            moduleName = eval(prefab_list[self_global.tile_list.currentRow()])
            try:
                create = moduleName.createTile(x, y, id_num, world_id_num, entity_num, placeholder_list)
            except TypeError:
                create = moduleName.createTile(x, y, id_num, world_id_num)
            #create = test_prefab.createTile(x, y, id_num, world_id_num)
            id_num = create[1]
            world_id_num = create[2]
            try:
                entity_num = create[3]
                placeholder_list = create[5]
                print("placeholder list: ", placeholder_list)
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

            icon = prefab_icon_list[self_global.tile_list.currentRow()]
            self.button.setIcon(QIcon(icon))
            self.button.setIconSize(QSize(32,32))

            totalblocks[btn_id] = create[0]
            try:
                entity_list[btn_id] = create[4]
            except:
                print("didnt work")

    def checkForAlt(self):
        modifiers = QApplication.keyboardModifiers()
        if modifiers == Qt.AltModifier:
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

        changeLightAction = QAction("&Change Lighting", self)
        changeLightAction.setShortcut("Ctrl+j")
        changeLightAction.setStatusTip("Change the environment lighting of the map.")
        changeLightAction.triggered.connect(self.change_light)
        
        exportAction = QAction("&Export", self)
        exportAction.setShortcut("Ctrl+e")
        exportAction.setStatusTip("Export as .vmf")
        exportAction.triggered.connect(self.file_export)

        gridAction = QAction("&Set Grid Size", self)
        gridAction.setShortcut("Ctrl+G")
        gridAction.setStatusTip("Set Grid Height and Width. RESETS ALL BLOCKS.")
        gridAction.triggered.connect(self.grid_change)

        createPrefabAction = QAction("&Prefab", self)
        #createPrefabAction.setShortcut("")
        createPrefabAction.setStatusTip("WILL CLEAR GRID! View the readme for a good idea on formatting.")
        createPrefabAction.triggered.connect(self.create_prefab)

        refreshPrefab = QAction("&Refresh Prefab List", self)
        refreshPrefab.setStatusTip("Refresh the list of prefabs, done after creating a new one.")
        refreshPrefab.triggered.connect(self.importprefabs)

        changeSkybox = QAction("&Change Skybox", self)
        changeSkybox.setStatusTip("Change the skybox of the map.")
        changeSkybox.setShortcut("Ctrl+s")
        changeSkybox.triggered.connect(self.change_skybox)
        self.statusBar()
        
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu("&File")
        optionsMenu = mainMenu.addMenu("&Options")
        createMenu = mainMenu.addMenu("&Create")
        
        fileMenu.addAction(newAction)
        #fileMenu.addAction(openAction)
        #fileMenu.addAction(saveAction)
        fileMenu.addAction(exportAction)
        fileMenu.addAction(exitAction)

        optionsMenu.addAction(gridAction)
        optionsMenu.addAction(changeLightAction)
        #optionsMenu.addAction(refreshPrefab)
        optionsMenu.addAction(changeSkybox)

        createMenu.addAction(createPrefabAction)
        
        self.home()

    def closeEvent(self, event):
        #closeEvent runs close_application when the x button is pressed
        event.ignore()
        self.close_application()
        
    def home(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        
        self.tile_list = QListWidget()

        for index, text in enumerate(prefab_text_list):
            item = QListWidgetItem(QIcon(prefab_icon_list[index]), text)
            self.tile_list.addItem(item)

        self.button_grid_layout = QGridLayout()
        self.button_grid_layout.setSpacing(0)

        self.column = QHBoxLayout()
        self.column.addLayout(self.button_grid_layout)
        self.column.addStretch(1)
        self.column.addWidget(self.tile_list)
        #self.column.addStretch(1)
        
        self.row = QVBoxLayout(self.central_widget)
        self.row.addLayout(self.column)
        self.row.addStretch(1)
        #self.row.addStretch(1)
        
        self.grid_change()
        
        self.show()
        
    def file_open(self):
        name = QFileDialog.getOpenFileName(self, "Open File", "C:/","*.sav")
        file = open(name, "r")
        openlines = file.readlines()
        openlinesstr = "".join(openlines)
        
        #now, it imports the vmf, and has two versions of it; the importlines which has each
        #line as a string in a list, and importlinesstr, which makes it one big string
            
    def file_save(self):
        name = QFileDialog.getSaveFileName(self, "Save File", "C:/", "*.sav")
        file = open(name[1], "w")
        text = self.textEdit.toPlainText()
        file.write(text)
        file.close()

    def file_export(self):
        global world_id_num, count_btns, currentlight, skybox, skybox2_list, entity_list
        #skybox = skybox_list[skybox2_list.currentRow()]
        currentlight = currentlight.replace("world_idnum",str(world_id_num))
        entity_list[count_btns] = currentlight
        name = QFileDialog.getSaveFileName(self, "Export .vmf", "output/", "Valve Map File (*.vmf)")
        file = open(name[0], "w")
        import export
        wholething = export.execute(totalblocks, entity_list, skybox)
        print(wholething)
        file.write(wholething)
        file.close()
        QMessageBox.information(self, "File Exported",
                                "The .vmf has been outputted to %s" %(name[0]) + " Open it in hammer to compile as a .bsp")
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
        
    def grid_change(self):
        self.count=0
        self.btn_id_count = 0
        text = QInputDialog.getText(self,("Get Grid Y"),
                                     ("Grid Height:"))                                    
        text2 = QInputDialog.getText(self,("Get Grid X"),
                                     ("Grid Width:"))
        try:
            self.grid_y = int(text[0])
            self.grid_x = int(text2[0])
        except ValueError:
            #TODO: Instead of a print statement, we need to bring up a window, alerting the user
            QMessageBox.critical(self, "Error", "Please enter a number.")
            self.grid_change()

        self.removeButtons()
        #self.removeDropdown()

        print(self.grid_y)
        print(self.grid_x)
        if self.grid_y >= 23:
            print("y value too big! Please print a number. (less than 23)")
            self.grid_change()
        elif self.grid_x >= 26:
            print("x value too big! Please print a number. (less than 26)")
            self.grid_change()

        for x in range(self.grid_x):
            for y in range(self.grid_y):
                #print("test") #testing if works
                grid_btn = GridBtn(self, x, y, self.btn_id_count)
                self.button_grid_layout.addWidget(grid_btn.button,y,x) #needs to be like this because grid_layout is counter-intuitive
                #self.button_grid_layout.setColumnMinimumWidth(y, 32)
                
                grid_list.append(grid_btn)
                totalblocks.append("EMPTY_SLOT") #This is so that there are no problems with replacing list values
                self.btn_id_count += 1
                global count_btns
                count_btns += 1
                entity_list.append("NO_ENTITY")
            #self.button_grid_layout.setRowMinimumHeight(x, 32)
        entity_list.append("lighting slot")
        #print(totalblocks)

                
        self.count += 1
        #self.comboBox = QComboBox(self)
        #self.comboBox.resize(128, 16)
        #for item in prefab_text_list:
        #    self.comboBox.addItem(item)
        #self.comboBox.move(32*self.count+2, 22)
        #self.comboBox.show()
            
    #def removeDropdown(self):
     #   try:
      #      self.comboBox.deleteLater()
       #     del totalblocks[:]
        #    global world_id_num
         #   world_id_num = 2
        #except:
         #   print('ok')
    #def clearlist(self):
     #    grid_list=[]
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
        self.window = QWidget()
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
        self.window.show()
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
        name = QFileDialog.getOpenFileName(self, "Choose .vmf File", "C:/","*.vmf")
        prefab_icon = QFileDialog.getOpenFileName(self, "Choose Prefab Icon", "C:/","*.jpg")
        prefab_name = QInputDialog.getText(self,"Prefab Name",
                                     "Name of Prefab (e.g. wall_prefab):")
        prefab_text = QInputDialog.getText(self, "Prefab Text",
                                           "Prefab Text (e.g. Wall Tile)")
        QMessageBox.information(self, "Files Created, restart to see the prefab.",
                                createPrefab.create(name[0], prefab_name[0],
                                                    prefab_text[0], prefab_icon[0]))
        #self.importprefabs()

#define some global variables
id_num = 1
world_id_num = 2
entity_num = 1
toggle = 0
btn_id_count = 0
grid_list=[]
totalblocks = []
skybox_list=[]
skybox_icon_list=[]
prefab_list = []
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
    "_light" "255 255 255 200"
    "_lightHDR" "-1 -1 -1 1"
    "_lightscaleHDR" "1"
    "angles" "0 0 0"
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
#if the user does not change the lighting, it sticks with this.
#if the user does not choose a skybox it sticks with this

prefab_file = open("prefab_template\prefab_list.txt")
prefab_text_file = open("prefab_template\prefab_text_list.txt")
prefab_icon_file = open("prefab_template\prefab_icon_list.txt")

skybox_file = open("prefab_template\skybox_list.txt")
skybox_icon = open("prefab_template\skybox_icons.txt")

for line in prefab_file.readlines():
    prefab_list.append(line[:-1] if line.endswith("\n") else line)# need to do this because reading the file generates a \n after every line

for line in prefab_text_file.readlines():
    prefab_text_list.append(line[:-1] if line.endswith("\n") else line)

for line in prefab_icon_file.readlines():
    prefab_icon_list.append(line[:-1] if line.endswith("\n") else line)

for file in [prefab_file, prefab_text_file, prefab_icon_file]:
    file.close()

for line in skybox_file.readlines():
    skybox_list.append(line[:-1] if line.endswith("\n") else line)# need to do this because reading the file generates a \n after every line

for line in skybox_icon.readlines():
    skybox_icon_list.append(line[:-1] if line.endswith("\n") else line)

for file in [skybox_file,skybox_icon]:
    file.close()

#imports that need prefab_list to be defined

for item in prefab_list:
    globals()[item] = importlib.import_module(item)
    print("import", item)   
#Main Program
app = QApplication(sys.argv)
gui = MainWindow()
app.exec_()
