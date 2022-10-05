import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from random import random

form_class = uic.loadUiType("pyqt07.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)    # 클릭 시 실행할 function
    
    def myclick(self):
        mine = self.le_mine.text()
        rnd = random()*3
        com = ""
        result = ""
        
        if rnd > 2:
            com = "보"
        elif rnd > 1:
            com = "가위"
        else:
            com = "바위"
            
        # if mine == com:
        #     result = "무승부"
        # elif mine == "가위" and com == "바위": 
        #     result = "패배"
        # elif mine == "바위" and com == "보":
        #     result = "패배"
        # elif mine == "보" and com == "가위":
        #     result = "패배"
        # else:
        #     result = "승리"
        
        if com == "바위" and mine == "바위": result = "비김"
        elif com == "바위" and mine == "보": result = "이김"
        elif com == "바위" and mine == "가위": result = "짐"
        
        if com == "가위" and mine == "바위": result = "짐"
        elif com == "가위" and mine == "보": result = "이김"
        elif com == "가위" and mine == "가위": result = "비김"
        
        if com == "보" and mine == "바위": result = "이김"
        elif com == "보" and mine == "보": result = "비김"
        elif com == "보" and mine == "가위": result = "짐"
            
        self.le_com.setText(com)
        self.le_result.setText(result)
        
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()