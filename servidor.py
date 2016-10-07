#! /usr/bin/env python

import sys
from PyQt4 import QtCore, QtGui, uic

class ImageDialog(QtGui.QDialog):
     def __init__(self):
        QtGui.QDialog.__init__(self)
        # Set up the user interface from Designer.
        self.ui = uic.loadUi("servidor.ui")
        self.ui.tableWidget.horizontalHeader().hide()
        self.ui.tableWidget.verticalHeader().hide()
        self.ui.tableWidget.setRowCount(5)
        self.ui.tableWidget.setColumnCount(5)
        self.ui.tableWidget.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)
        self.ui.tableWidget.verticalHeader().setResizeMode(QtGui.QHeaderView.Stretch)
        self.ui.show()

app = QtGui.QApplication(sys.argv)
window = ImageDialog()
sys.exit(app.exec_())