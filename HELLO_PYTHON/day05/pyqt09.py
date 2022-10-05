import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("pyqt09.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb1.clicked.connect(lambda: self.myclick(self.pb1))    # 클릭 시 실행할 function
        self.pb2.clicked.connect(lambda: self.myclick(self.pb2))    # 클릭 시 실행할 function
        self.pb3.clicked.connect(lambda: self.myclick(self.pb3))    # 클릭 시 실행할 function
        self.pb4.clicked.connect(lambda: self.myclick(self.pb4))    # 클릭 시 실행할 function
        self.pb5.clicked.connect(lambda: self.myclick(self.pb5))    # 클릭 시 실행할 function
        self.pb6.clicked.connect(lambda: self.myclick(self.pb6))    # 클릭 시 실행할 function
        self.pb7.clicked.connect(lambda: self.myclick(self.pb7))    # 클릭 시 실행할 function
        self.pb8.clicked.connect(lambda: self.myclick(self.pb8))    # 클릭 시 실행할 function
        self.pb9.clicked.connect(lambda: self.myclick(self.pb9))    # 클릭 시 실행할 function
        self.pb0.clicked.connect(lambda: self.myclick(self.pb0))    # 클릭 시 실행할 function
        self.pb_call.clicked.connect(self.mycall)
    

    def myclick(self,pb):
        str_old = self.le.text()
        num = pb.text()
        self.le.setText(str_old + num)

    def mycall(self):
        str_tel = self.le.text()
        QMessageBox.information(self,'Information Title','Calling\n' + str_tel)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()