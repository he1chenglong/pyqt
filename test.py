# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.py'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtCore, QtGui, QtWidgets
from test1 import Ui_MainWindow
import sys
import time

class mywindow(QtWidgets.QWidget,Ui_MainWindow):
    _signal =QtCore.pyqtSignal(str)
    def __init__(self):
        super(mywindow,self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.myPrint)
        self._signal.connect(self.mySignal)

    def myPrint(self):
        print("helloword")


    def mySignal(self,string):
        print(string)

if __name__=="__main__":
    app=QtWidgets.QApplication(sys.argv)
    myshow=mywindow()
    myshow.show()
    sys.exit(app.exec_())
