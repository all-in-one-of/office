# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/users/d.liubimov/Documents/CGF_PROJECTS/PUBLISHER/variant_widget.ui'
#
# Created: Tue Feb 12 13:19:41 2019
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from qt_import import *

class Ui_variants_widget(object):
    def setupUi(self, variants_widget):
        variants_widget.setObjectName("variants_widget")
        # variants_widget.resize(389, 92)
        self.formLayout = QFormLayout(variants_widget)
        self.formLayout.setObjectName("formLayout")
        self.variant_lb = QLabel(variants_widget)
        self.variant_lb.setObjectName("variant_lb")
        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.variant_lb)
        self.variant_cbx = QComboBox(variants_widget)
        self.variant_cbx.setObjectName("variant_cbx")
        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.variant_cbx)
        self.count_lb = QLabel(variants_widget)
        self.count_lb.setObjectName("count_lb")
        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.count_lb)
        self.count_cbx = QComboBox(variants_widget)
        self.count_cbx.setObjectName("count_cbx")
        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.count_cbx)

        self.retranslateUi(variants_widget)
        QtCore.QMetaObject.connectSlotsByName(variants_widget)

    def retranslateUi(self, variants_widget):
        variants_widget.setWindowTitle("Variants_Widget")
        self.variant_lb.setText("Variant")
        self.count_lb.setText("Count")
