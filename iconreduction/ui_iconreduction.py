# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_iconreduction.ui'
#
# Created: Thu Feb 27 11:33:27 2014
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_IconReduction(object):
    def setupUi(self, IconReduction):
        IconReduction.setObjectName(_fromUtf8("IconReduction"))
        IconReduction.resize(268, 85)
        self.buttonBox = QtGui.QDialogButtonBox(IconReduction)
        self.buttonBox.setGeometry(QtCore.QRect(10, 50, 251, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.label = QtGui.QLabel(IconReduction)
        self.label.setGeometry(QtCore.QRect(10, 10, 171, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(IconReduction)
        self.label_2.setGeometry(QtCore.QRect(10, 30, 171, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(IconReduction)
        self.label_3.setGeometry(QtCore.QRect(90, 30, 171, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(IconReduction)
        self.label_4.setGeometry(QtCore.QRect(90, 10, 171, 17))
        self.label_4.setObjectName(_fromUtf8("label_4"))

        self.retranslateUi(IconReduction)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), IconReduction.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), IconReduction.reject)
        QtCore.QMetaObject.connectSlotsByName(IconReduction)

    def retranslateUi(self, IconReduction):
        IconReduction.setWindowTitle(QtGui.QApplication.translate("IconReduction", "IconReduction", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("IconReduction", "Version:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("IconReduction", "Date:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("IconReduction", "Feb 2014", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("IconReduction", "0.1", None, QtGui.QApplication.UnicodeUTF8))

