# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.py'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtCore, QtGui, QtWidgets
from untitled  import Ui_MainWindow
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
        self.textEdit.setText("")
        self.textEdit.append("正在打印，请稍后")
        self._signal.emit("结束了吗，快回答")


    def mySignal(self,string):
        print(string)
        self.textEdit.append("打印结束")

if __name__=="__main__":
    app=QtWidgets.QApplication(sys.argv)
    myshow=mywindow()
    myshow.show()
    sys.exit(app.exec_())
