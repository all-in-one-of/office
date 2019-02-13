# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/users/d.liubimov/Documents/CGF_PROJECTS/PUBLISHER/path_widget.ui'
#
# Created: Tue Feb 12 10:44:31 2019
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from qt_import import *


class Ui_PathWidget(object):
    """
    Widget, содержащий поля ответов сервера: PublishEvent Name, GroupID, Version, LinkedVersion;
    """
    def setupUi(self, PathWidget):
        PathWidget.setObjectName("PathWidget")
        # PathWidget.resize(579, 90)
        
        # self.gridLayout = QGridLayout(PathWidget)
        # self.gridLayout.setObjectName("gridLayout")
        # self.scene_lb = QLabel(PathWidget)
        # self.scene_lb.setObjectName("scene_lb")
        # self.gridLayout.addWidget(self.scene_lb, 0, 0, 1, 1)
        # self.scene_le = QLineEdit(PathWidget)
        # self.scene_le.setObjectName("scene_le")
        # self.gridLayout.addWidget(self.scene_le, 0, 1, 1, 1)
        # self.node_lb = QLabel(PathWidget)
        # self.node_lb.setObjectName("node_lb")
        # self.gridLayout.addWidget(self.node_lb, 1, 0, 1, 1)
        # self.node_le = QLineEdit(PathWidget)
        # self.node_le.setObjectName("node_le")
        # self.gridLayout.addWidget(self.node_le, 1, 1, 1, 1)
        
        self.formLayout = QFormLayout(PathWidget)
        self.formLayout.setObjectName("formLayout")
        self.scene_lb = QLabel(PathWidget)
        self.scene_lb.setObjectName("scene_lb")
        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.scene_lb)
        self.scene_le = QLineEdit(PathWidget)
        self.scene_le.setObjectName("scene_le")
        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.scene_le)
        self.node_lb = QLabel(PathWidget)
        self.node_lb.setObjectName("node_lb")
        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.node_lb)
        self.node_le = QLineEdit(PathWidget)
        self.node_le.setObjectName("node_le")
        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.node_le)

        self.retranslateUi(PathWidget)
        QtCore.QMetaObject.connectSlotsByName(PathWidget)

    def retranslateUi(self, PathWidget):
        PathWidget.setWindowTitle("Paths Widget")
        self.scene_lb.setText("Scene path")
        self.node_lb.setText("Node path")

