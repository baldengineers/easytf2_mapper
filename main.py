#use blocks to create maps
import sys
from PySide.QtCore import *
from PySide.QtGui import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setGeometry(50,50,500,300)
        self.setWindowTitle("Easy TF2 Mapper")
        self.setWindowIcon(QIcon("map.ico"))
        self.show()

app = QApplication(sys.argv)
GUI = MainWindow()
sys.exit(app.exec_())
