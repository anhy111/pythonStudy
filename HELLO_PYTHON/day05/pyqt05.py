import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from random import random

form_class = uic.loadUiType("pyqt05.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)    # 클릭 시 실행할 function
    
    def myclick(self):
        mine = self.leMine.text()
        rnd = random()*2
        com = ""
        result = ""
        
        if rnd > 1:
            com = "홀"
        else:
            com = "짝"
            
        if mine == com:
            result = "승리"
        else:
            result = "패배"
            
        self.leCom.setText(com)
        self.leResult.setText(result)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()