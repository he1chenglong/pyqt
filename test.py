# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.py'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox,QInputDialog,QLineEdit

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

        #self.myButton =QtWidgets.QPushButton(self)
        #self.myButton.setObjectName("myButton")
        self.myButton.setText("Test")
        #self.myButton.clicked.connect(self.msg)
        self.myButton.clicked.connect(self.input)

    def input(self):
        #doubleNum,ok1 = QInputDialog.getDouble(self, "标题","计数:", 37.56, -10000, 10000, 2)
        #print("input "+doubleNum)
        # self.val=doubleNum
        # intNum,ok2 = QInputDialog.getInt(self, "标题","计数:", 37, -10000, 10000, 2)
        # stringNum,ok3 = QInputDialog.getText(self, "标题","姓名:",QLineEdit.Normal, "王尼玛")
        # print(stringNum)
        items = ["Spring", "Summer", "Fall", "Winter"]
        item, ok4 = QInputDialog.getItem(self, "标题","Season:", items, 1, True)
        text, ok5 = QInputDialog.getMultiLineText(self, "标题", "Address:", "John Doe\nFreedom Street")
        print(text)




    def msg(self):
        reply = QMessageBox.information(self,"标题","消息",QMessageBox.Yes|QMessageBox.No)


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
