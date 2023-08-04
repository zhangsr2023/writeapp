# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'planUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(713, 429)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton.setEnabled(True)
        self.commandLinkButton.setGeometry(QtCore.QRect(10, 10, 193, 41))
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(70, 90, 591, 251))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.spinBox = SpinBox(self.gridLayoutWidget)
        self.spinBox.setObjectName("spinBox")
        self.gridLayout.addWidget(self.spinBox, 1, 1, 1, 2)
        self.comboBox = ComboBox(self.gridLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout.addWidget(self.comboBox, 0, 1, 1, 2)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.radioButton = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioButton.setEnabled(True)
        self.radioButton.setObjectName("radioButton")
        self.buttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.radioButton)
        self.gridLayout.addWidget(self.radioButton, 2, 1, 1, 1)
        self.radioButton_2 = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioButton_2.setObjectName("radioButton_2")
        self.buttonGroup.addButton(self.radioButton_2)
        self.gridLayout.addWidget(self.radioButton_2, 2, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)
        self.radioButton_3 = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioButton_3.setObjectName("radioButton_3")
        self.buttonGroup_2 = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup_2.setObjectName("buttonGroup_2")
        self.buttonGroup_2.addButton(self.radioButton_3)
        self.gridLayout.addWidget(self.radioButton_3, 3, 1, 1, 1)
        self.radioButton_4 = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioButton_4.setObjectName("radioButton_4")
        self.buttonGroup_2.addButton(self.radioButton_4)
        self.gridLayout.addWidget(self.radioButton_4, 3, 2, 1, 1)
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(570, 10, 121, 71))
        self.lcdNumber.setObjectName("lcdNumber")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(480, 30, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.pushButton = PrimaryPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(230, 350, 241, 32))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 713, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.actiondelete = QtWidgets.QAction(MainWindow)
        self.actiondelete.setObjectName("actiondelete")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "计划生成"))
        self.commandLinkButton.setText(_translate("MainWindow", "开始当前计划"))
        self.label.setText(_translate("MainWindow", "选择词库："))
        self.label_3.setText(_translate("MainWindow", "背诵模式："))
        self.label_2.setText(_translate("MainWindow", "每天单词数量："))
        self.radioButton.setText(_translate("MainWindow", "普通"))
        self.radioButton_2.setText(_translate("MainWindow", "强记忆"))
        self.label_5.setText(_translate("MainWindow", "校对模式："))
        self.radioButton_3.setText(_translate("MainWindow", "背中文"))
        self.radioButton_4.setText(_translate("MainWindow", "背英文"))
        self.label_4.setText(_translate("MainWindow", "剩余天数"))
        self.pushButton.setText(_translate("MainWindow", "生成新计划"))
        self.actiondelete.setText(_translate("MainWindow", "c"))
from qfluentwidgets import ComboBox, PrimaryPushButton, SpinBox
