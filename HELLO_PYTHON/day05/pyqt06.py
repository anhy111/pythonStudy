import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from random import random

form_class = uic.loadUiType("pyqt06.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)    # 클릭 시 실행할 function
    
    def myclick(self):
        dan = self.le.text()
        dan = int(dan)
        
        result = ""
        result += str(dan) + " * 1 = " + str(dan * 1) + "\n"
        result += str(dan) + " * 2 = " + str(dan * 2) + "\n"
        result += str(dan) + " * 3 = " + str(dan * 3) + "\n"
        result += str(dan) + " * 4 = " + str(dan * 4) + "\n"
        result += str(dan) + " * 5 = " + str(dan * 5) + "\n"
        result += str(dan) + " * 6 = " + str(dan * 6) + "\n"
        result += str(dan) + " * 7 = " + str(dan * 7) + "\n"
        result += str(dan) + " * 8 = " + str(dan * 8) + "\n"
        result += str(dan) + " * 9 = " + str(dan * 9) + "\n"
        
        self.te.setText(result)
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()