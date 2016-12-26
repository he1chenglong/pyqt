# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Children.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ChildrenForm(object):
    def setupUi(self, ChildrenForm):
        ChildrenForm.setObjectName("ChildrenForm")
        ChildrenForm.resize(400, 300)
        self.checkBox = QtWidgets.QCheckBox(ChildrenForm)
        self.checkBox.setGeometry(QtCore.QRect(90, 60, 71, 16))
        self.checkBox.setObjectName("checkBox")
        self.radioButton = QtWidgets.QRadioButton(ChildrenForm)
        self.radioButton.setGeometry(QtCore.QRect(100, 100, 89, 16))
        self.radioButton.setObjectName("radioButton")

        self.retranslateUi(ChildrenForm)
        QtCore.QMetaObject.connectSlotsByName(ChildrenForm)

    def retranslateUi(self, ChildrenForm):
        _translate = QtCore.QCoreApplication.translate
        ChildrenForm.setWindowTitle(_translate("ChildrenForm", "Form"))
        self.checkBox.setText(_translate("ChildrenForm", "CheckBox"))
        self.radioButton.setText(_translate("ChildrenForm", "RadioButton"))

