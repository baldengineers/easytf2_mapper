#use blocks to create maps
import sys
from PySide.QtCore import *
from PySide.QtGui import *
import 

class GridBtn(QMainWindow):
    def __init__(self, self_global, x, y):
        super(GridBtn, self).__init__()
        self.button = QPushButton("0", self_global)
        self.x = 32*x
        self.y = 20+(32*y)
        self.button.move(self.x,self.y)
        self.button.resize(32,32)
        self.button.clicked.connect(lambda: self.click_func(x,y))
        self.button.show()

    def change_val(self, val):
        self.button = QPushButton(val, self_global)

    def click_func(self, x, y):
        print((x,y))
        prefab_list[gui.comboBox.currentIndex()].createTile(x, y)
   

class MainWindow(QMainWindow):
    def __init__(self):
        #create the main window
        super(MainWindow, self).__init__()
        self.setGeometry(100, 25, 875, 750)
        self.setWindowTitle("Easy TF2 Mapper")
        self.setWindowIcon(QIcon("map.ico"))

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

        gridAction = QAction("&Set Grid Size", self)
        gridAction.setShortcut("Ctrl+G")
        gridAction.setStatusTip("Set Grid Height and Width. RESETS ALL BLOCKS.")
        gridAction.triggered.connect(self.grid_change)


        self.statusBar()

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu("&File")
        optionsMenu = mainMenu.addMenu("&Options")
        optionsMenu.addAction(gridAction)
        fileMenu.addAction(newAction)
        fileMenu.addAction(openAction)
        fileMenu.addAction(saveAction)
        fileMenu.addAction(exitAction)
        
        self.home()

    def closeEvent(self, event):
        #closeEvent runs close_application when the x button is pressed
        event.ignore()
        self.close_application()
        
    def home(self):
        self.texture_list = QListWidget()
        self.texture_list.addItem("texture")
        
        self.button_grid_layout = QGridLayout()
        #TODO: Manually set grid x and grid y

        self.column = QHBoxLayout()
        #self.column.addWidget(self.texture_list)
        self.column.addLayout(self.button_grid_layout)
        
        self.grid_change()
        
        self.show()


    def file_open(self):
        name = QFileDialog.getOpenFileName(self, "Open File", "C:/","*.sav")
        file = open(name, "r")
        openlines = file.readlines()
        openlinesstr = "".join(openlines)
        
        #now, it imports the vmt, and has two versions of it; the importlines which has each
        #line as a string in a list, and importlinesstr, which makes it one big string
            
    def file_save(self):
        name = QFileDialog.getSaveFileName(self, "Save File", "//", "*.sav")
        file = open(name, "w")
        text = self.textEdit.toPlainText()
        file.write(text)
        file.close()

    def file_export(self):
        name = QFileDialog.getSaveFileName(self, "Save File", "//", "*.vmf")
        file = open(name, "w")
        
    def removeButtons(self):

        for i in reversed(range(self.button_grid_layout.count())):
            widget = self.button_grid_layout.takeAt(i).widget()

            if widget is not None:
                widget.deleteLater()

        #for i in reversed(range(self.button_grid_layout.count())):
            #self.button_grid_layout.itemAt(i).widget().setParent(None)

        #for grid_button in grid_list:
            #grid_button.button.close()

        self.clearlist()
        
    def grid_change(self):
        self.removeButtons()
        self.removeDropdown()
        self.count=0
        text = QInputDialog.getText(self,("Get Grid Y"),
                                     ("Grid Height:"))                                    
        text2 = QInputDialog.getText(self,("Get Grid X"),
                                     ("Grid Width:"))
        try:
            self.grid_y = int(text[0])
            self.grid_x = int(text2[0])
        except ValueError:
            #TODO: Instead of a print statement, we need to bring up a window, alerting the user
            print("Please enter a number.")
            self.grid_change()
            self.removeDropdown()
        

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
                grid_btn = GridBtn(self, x, y)
                self.button_grid_layout.addWidget(grid_btn.button,x,y)
                
                grid_list.append(grid_btn)
            self.count += 1
        self.comboBox = QComboBox(self)
        self.comboBox.resize(64, 16)
        for item in prefab_text_list:
            self.comboBox.addItem(item)
        self.comboBox.move(32*self.count+2, 22)
        self.comboBox.show()
            
    def removeDropdown(self):
        try:
            self.comboBox.deleteLater()
        except:
            print('ok')
    def clearlist(self):
        grid_list=[]
        
    def close_application(self):
        choice = QMessageBox.question(self, "Exit",
                                      "Are you sure you want to exit?",
                                      QMessageBox.Yes | QMessageBox.No,
                                      QMessageBox.No)
        if choice == QMessageBox.Yes:
            sys.exit()
        else:
            pass

#define some global variables
grid_list=[]
prefab_list = ["ground_prefab", "wall_prefab"] # As we get more prefabs, add the filenames to this list
prefab_text_list = ["1. Blank Tile", "2. Wall Tile"] # As we get more prefabs, add the text that will be in the comboBox to this list
# Indexes for prefab_list and prefab_text_list should match

#imports that need prefab_list to be defined
for item in prefab_list:
    import item

#Main Program
app = QApplication(sys.argv)
gui = MainWindow()
app.exec_()
