import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from random import random

form_class = uic.loadUiType("pyqt10.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)    # 클릭 시 실행할 function
        self.pb2.clicked.connect(self.reset)    # 클릭 시 실행할 function
        self.com = ""
        self.ranNum()
    
    def reset(self):
        self.le.setText("")
        self.te.setText("")
        self.ranNum()

    def myclick(self):
        mine = self.le.text()
        # str_old = self.te.toPlainText()
        strike = self.getStrike(mine)
        ball = self.getBall(mine)
        self.te.append(mine + " " + strike + "S " + ball + "B")
        self.le.setText("");
        if strike == "3":
            self.te.append("게임종료")

    def ranNum(self):
        arr10 = [0,1,2,3,4,5,6,7,8,9]
        
        for i in range(100):
            rnd = int(random()*10)
            
            temp = arr10[0]
            arr10[0] = arr10[rnd]
            arr10[rnd] = temp
            
        self.com = str(arr10[0]) + str(arr10[1]) + str(arr10[2])
        print(self.com)

    def getStrike(self, mine):
        cnt = 0
        if self.com[0] == mine[0]: cnt += 1
        if self.com[1] == mine[1]: cnt += 1
        if self.com[2] == mine[2]: cnt += 1
        
        return str(cnt)
    
    def getBall(self, mine):
        cnt = 0
        
        if self.com[0] == mine[1] or self.com[0] == mine[2]: cnt += 1
        if self.com[1] == mine[0] or self.com[1] == mine[2]: cnt += 1
        if self.com[2] == mine[0] or self.com[2] == mine[1]: cnt += 1
        
        
        return str(cnt)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()