#use blocks to create maps
import sys
from PySide.QtCore import *
from PySide.QtGui import *

class GridBtn():
    def __init__(self):
        self.button = QPushButton("0", self)

    def change_val(self, val):
        self.button = QPushButton(val, self)

class MainWindow(QMainWindow):
    def __init__(self, app):
        #create the main window
        super(MainWindow, self).__init__()
        self.setGeometry(500, 300, 500, 300)
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

        self.statusBar()

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu("&File")
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
        self.grid_x = 3
        self.grid_y = 3
        
        for x in range(self.grid_x):
            for y in range(self.grid_y):
                grid_btn = GridBtn()
                self.button_grid_layout.addWidget(grid_btn.button,x,y)
        
        self.column = QHBoxLayout()
        self.column.addWidget(self.texture_list)
        self.column.addLayout(self.button_grid_layout)
        self.show()

    def file_open(self):
        name = QFileDialog.getOpenFileName(self, "Open File", "C:/","*.vmt")
        file = open(name, "r")
        lines = []

        for line in file:
            lines.append(line)
            for letter in line:
                #TODO: Use Anson's functions to decipher the vmt file, to then open
                #the file into the program
                pass
        
        #with file:
            #text = file.read()
            
    def file_save(self):
        name = QFileDialog.getSaveFileName(self, "Save File", "//", "*.vmt")
        file = open(name, "w")
        text = self.textEdit.toPlainText()
        file.write(text)
        file.close()

    def close_application(self):
        choice = QMessageBox.question(self, "Exit",
                                      "Are you sure you want to exit?",
                                      QMessageBox.Yes | QMessageBox.No,
                                      QMessageBox.No)
        if choice == QMessageBox.Yes:
            sys.exit()
        else:
            pass

app = QApplication(sys.argv)
gui = MainWindow(app)
app.exec_()
