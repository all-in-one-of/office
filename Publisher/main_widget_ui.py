# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/users/d.liubimov/Documents/CGF_PROJECTS/PUBLISHER/main_widget.ui'
#
# Created: Tue Feb 12 10:44:03 2019
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from qt_import import *

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        self.dialog = Dialog

        Dialog.setObjectName("Dialog")
        Dialog.setMinimumSize(600, 200)
        Dialog.resize(700, 200)
        self.gridLayout_main = QGridLayout(Dialog)
        self.gridLayout_main.setObjectName("gridLayout_main")
        self.toolBox = QToolBox(Dialog)
        self.toolBox.setObjectName("toolBox")
        
        self.page_top = QWidget()
        # self.page_top.setGeometry(QtCore.QRect(0, 0, 587, 375))
        self.page_top.setObjectName("page_top")
        
        self.gridLayout_top = QGridLayout(self.page_top)
        self.gridLayout_top.setObjectName("gridLayout_top")
        
        self.toolBox.addItem(self.page_top, "")

        self.page_bottom = QWidget()
        # self.page_bottom.setGeometry(QtCore.QRect(0, 0, 587, 375))
        self.page_bottom.setObjectName("page_bottom")
        
        self.gridLayout_bottom = QGridLayout(self.page_bottom)
        self.gridLayout_bottom.setObjectName("gridLayout_bottom")

        self.desc_pte = QPlainTextEdit(self.page_bottom)
        self.desc_pte.setObjectName("desc_pte")
        self.gridLayout_bottom.addWidget(self.desc_pte, 0, 0, 1, 1)
        self.toolBox.addItem(self.page_bottom, "")
        self.gridLayout_main.addWidget(self.toolBox, 0, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_main.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.toolBox.setCurrentIndex(1)

        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle("CGF Publisher")
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_top), "Task Information")
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_bottom), "Input Description")
