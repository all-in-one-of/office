# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/users/d.liubimov/Documents/CGF_PROJECTS/PUBLISHER/publish_widget.ui'
#
# Created: Tue Feb 12 10:44:59 2019
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from qt_import import *


class Ui_publish_data(object):
    """
    Widget, содержащий поля ответов сервера: PublishEvent Name, GroupID, Version, LinkedVersion;
    """
    def setupUi(self, publish_data):
        publish_data.setObjectName("publish_data")
        # publish_data.resize(581, 90)
        self.gridLayout = QGridLayout(publish_data)
        self.gridLayout.setObjectName("gridLayout")
        self.name_lb = QLabel(publish_data)
        self.name_lb.setMinimumSize(QtCore.QSize(88, 0))
        self.name_lb.setObjectName("name_lb")
        self.gridLayout.addWidget(self.name_lb, 0, 0, 1, 1)
        self.name_le = QLineEdit(publish_data)
        self.name_le.setObjectName("name_le")
        self.gridLayout.addWidget(self.name_le, 0, 1, 1, 1)
        self.line_3 = QFrame(publish_data)
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout.addWidget(self.line_3, 0, 2, 2, 1)
        self.ver_lb = QLabel(publish_data)
        self.ver_lb.setObjectName("ver_lb")
        self.gridLayout.addWidget(self.ver_lb, 0, 3, 1, 1)
        self.ver_le = QLineEdit(publish_data)
        self.ver_le.setObjectName("ver_le")
        self.gridLayout.addWidget(self.ver_le, 0, 4, 1, 1)
        self.groupid_lb = QLabel(publish_data)
        self.groupid_lb.setObjectName("groupid_lb")
        self.gridLayout.addWidget(self.groupid_lb, 1, 0, 1, 1)
        self.groupid_le = QLineEdit(publish_data)
        self.groupid_le.setObjectName("groupid_le")
        self.gridLayout.addWidget(self.groupid_le, 1, 1, 1, 1)
        self.linkver_lb = QLabel(publish_data)
        self.linkver_lb.setObjectName("linkver_lb")
        self.gridLayout.addWidget(self.linkver_lb, 1, 3, 1, 1)
        self.verlink_le = QLineEdit(publish_data)
        self.verlink_le.setObjectName("verlink_le")
        self.gridLayout.addWidget(self.verlink_le, 1, 4, 1, 1)

        self.retranslateUi(publish_data)
        QtCore.QMetaObject.connectSlotsByName(publish_data)

    def retranslateUi(self, publish_data):
        publish_data.setWindowTitle("Publish Widget")
        self.name_lb.setText("Publish Event")
        self.ver_lb.setText("Version")
        self.groupid_lb.setText("GroupID")
        self.linkver_lb.setText("Linked Version")

