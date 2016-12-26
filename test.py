# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.py'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox,QInputDialog,QLineEdit,QFileDialog
from ChildrenForm import ChildrenForm

from untitled  import Ui_MainWindow
import sys
import time

class mywindow(QtWidgets.QWidget,Ui_MainWindow):
    _signal =QtCore.pyqtSignal(str)
    def __init__(self):
        super(mywindow,self).__init__()
        self.setupUi(self)

        self.child=ChildrenForm()

        self.fileOpen.triggered.connect(self.openMsg) #菜单的点击事件是triggered

        self.actionTst.triggered.connect(self.childShow)#点击actionTst,子窗口就会显示在主窗口的MaingridLayout中

        self.pushButton.clicked.connect(self.myPrint)
        self._signal.connect(self.mySignal)

        #self.myButton =QtWidgets.QPushButton(self)
        #self.myButton.setObjectName("myButton")
        self.myButton.setText("Test")
        #self.myButton.clicked.connect(self.msg)
        # self.myButton.clicked.connect(self.input)
        self.myButton.clicked.connect(self.fileopen)  #菜单的点击事件是triggered

    def childShow(self):
        self.MaingridLayout.addWidget(self.child)
        # self.child.show()
        pass


    # 菜单操作的例子
    def openMsg(self):
        file,ok=QFileDialog.getOpenFileName(self,"打开","C:/","All Files (*);;Text Files (*.txt)")
        self.statusbar.showMessage(file)                   #在状态栏显示文件地址

    # 文件打开 对话框的 例子
    def fileopen(self):
        directory1 = QFileDialog.getExistingDirectory(self,"选取文件夹","C:/")
        print(directory1)
        fileName1, filetype = QFileDialog.getOpenFileName(self,
                                                          "选取文件",
                                                          "C:/",
                                                          "All Files (*);;Text Files (*.txt)")
        print(fileName1,filetype)
        files, ok1 = QFileDialog.getOpenFileNames(self,
                                                  "多选取文件",
                                                  "C:/",
                                                  "All Files (*);;Text Files (*.txt)")
        print(files,ok1)
        fileName2, ok2 = QFileDialog.getSaveFileName(self,
                                                     "保存文件",
                                                     "C:/",
                                                     "All Files (*);;Text Files (*.txt)")
        print(files,ok1)

    # 输入对话框的例子
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



    # 弹出 对话框 示例
    def msg(self):
        reply = QMessageBox.information(self,"标题","消息",QMessageBox.Yes|QMessageBox.No)

    # 信号 和 槽  自己发送信号 的例子
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
