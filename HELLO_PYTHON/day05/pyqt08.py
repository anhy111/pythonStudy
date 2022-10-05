import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from random import random

form_class = uic.loadUiType("pyqt08.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)    # 클릭 시 실행할 function
    
    def myclick(self):
        first = self.le_first.text()
        last = self.le_last.text()
        
        first = int(first)
        last = int(last)
        str = ""
        
        for i in range(first, last+1):
            str += self.countOfStar(i) + "\n"
    
        self.te.setText(str)
    
    
    def countOfStar(self, cnt):
        str = ""
        for i in range(cnt):
            str += "*"
        return str
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()