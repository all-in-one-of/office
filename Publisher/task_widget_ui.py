# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/users/d.liubimov/Documents/CGF_PROJECTS/PUBLISHER/task_widget.ui'
#
# Created: Tue Feb 12 10:45:26 2019
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from qt_import import *


class Ui_task_data(object):
    """
    Widget, содержащий информацию полей task из shotgun;
    """
    def setupUi(self, task_data):
        task_data.setObjectName("task_data")
        # task_data.resize(583, 129)
        self.gridLayout = QGridLayout(task_data)
        self.gridLayout.setObjectName("gridLayout")
        self.entity_lb = QLabel(task_data)
        self.entity_lb.setObjectName("entity_lb")
        self.gridLayout.addWidget(self.entity_lb, 0, 0, 1, 1)
        self.entity_le = QLineEdit(task_data)
        self.entity_le.setObjectName("entity_le")
        self.gridLayout.addWidget(self.entity_le, 0, 1, 1, 1)
        self.line = QFrame(task_data)
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 0, 2, 3, 1)
        self.project_lb = QLabel(task_data)
        self.project_lb.setObjectName("project_lb")
        self.gridLayout.addWidget(self.project_lb, 0, 3, 1, 1)

        self.project_cbx = QComboBox(task_data)
        self.project_cbx.setObjectName("project_cbx")
        self.gridLayout.addWidget(self.project_cbx, 0, 4, 1, 1)

        self.asset_lb = QLabel(task_data)
        self.asset_lb.setObjectName("asset_lb")
        self.gridLayout.addWidget(self.asset_lb, 1, 0, 1, 1)
        self.asset_le = QLineEdit(task_data)
        self.asset_le.setObjectName("asset_le")
        self.gridLayout.addWidget(self.asset_le, 1, 1, 1, 1)
        self.task_lb = QLabel(task_data)
        self.task_lb.setObjectName("task_lb")
        self.gridLayout.addWidget(self.task_lb, 1, 3, 1, 1)
        self.task_le = QLineEdit(task_data)
        self.task_le.setObjectName("task_le")
        self.gridLayout.addWidget(self.task_le, 1, 4, 1, 1)
        self.contype_lb = QLabel(task_data)
        self.contype_lb.setObjectName("contype_lb")
        self.gridLayout.addWidget(self.contype_lb, 2, 0, 1, 1)
        self.contype_le = QLineEdit(task_data)
        self.contype_le.setObjectName("contype_le")
        self.gridLayout.addWidget(self.contype_le, 2, 1, 1, 1)
        self.artist_lb = QLabel(task_data)
        self.artist_lb.setObjectName("artist_lb")
        self.gridLayout.addWidget(self.artist_lb, 2, 3, 1, 1)
        self.artist_le = QLineEdit(task_data)
        self.artist_le.setObjectName("artist_le")
        self.gridLayout.addWidget(self.artist_le, 2, 4, 1, 1)

        self.retranslateUi(task_data)
        QtCore.QMetaObject.connectSlotsByName(task_data)

    def retranslateUi(self, task_data):
        task_data.setWindowTitle("Task Widget")
        self.entity_lb.setText("Entity")
        self.project_lb.setText("Project")
        self.asset_lb.setText("Base asset")
        self.task_lb.setText("Task")
        self.contype_lb.setText("Content type")
        self.artist_lb.setText("Artist")

