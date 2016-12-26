# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

def sinTest():
    print("按钮文本改变")
    btn.setText("按钮文本改变")

app =QApplication([])

main =QWidget()

main.resize(200,100)
btn =QPushButton("按钮文本",main)
btn.clicked.connect(sinTest)

main.show()
app.exec_()
