import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from random import random

form_class = uic.loadUiType("pyqt04.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)    # 클릭 시 실행할 function
    
    def myclick(self):
        lottoArr = list(range(1, 46))

        for i in range(len(lottoArr)):
            ran = int(random()*len(lottoArr))
            
            temp = lottoArr[ran]
            lottoArr[ran] = lottoArr[i]
            lottoArr[i] = temp
        
        self.le1.setText(str(lottoArr[0]))
        self.le2.setText(str(lottoArr[1]))
        self.le3.setText(str(lottoArr[2]))
        self.le4.setText(str(lottoArr[3]))
        self.le5.setText(str(lottoArr[4]))
        self.le6.setText(str(lottoArr[5]))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()