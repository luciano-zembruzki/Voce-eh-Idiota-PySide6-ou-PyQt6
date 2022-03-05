import sys
from PySide6 import QtWidgets
from PySide6.QtWidgets import QLabel

import random

from main_ui import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        
        self.button_no.clicked.connect(self.moveButton)
        self.pushButton.clicked.connect(self.euSabiaIdiota)
        
    def moveButton(self):
          print("Hello")
          self.button_no.move(random.randint(0,300), random.randint(0,300))
          
          
    def euSabiaIdiota(self):
          self.label.setText("Eu sabia!!!")
          self.pushButton.setEnabled(False)
          self.button_no.setEnabled(False)


app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
