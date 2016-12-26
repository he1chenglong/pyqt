from PyQt5 import QtCore, QtGui, QtWidgets
from Children import Ui_ChildrenForm

class ChildrenForm(QtWidgets.QMainWindow,Ui_ChildrenForm):
    def __init__(self):
        super(ChildrenForm,self).__init__()
        self.setupUi(self)