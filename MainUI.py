# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(731, 450)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 140, 521, 271))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayoutWidget = QtWidgets.QWidget(self.tab)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 10, 481, 221))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.pushButton_2 = PrimaryPushButton(self.gridLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 4, 0, 1, 3)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 2, 1, 1)
        self.PrimaryToolButton = PrimaryToolButton(self.gridLayoutWidget)
        self.PrimaryToolButton.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.PrimaryToolButton.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.PrimaryToolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.PrimaryToolButton.setAutoRaise(False)
        self.PrimaryToolButton.setArrowType(QtCore.Qt.NoArrow)
        self.PrimaryToolButton.setObjectName("PrimaryToolButton")
        self.gridLayout.addWidget(self.PrimaryToolButton, 3, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 3, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 2)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.tab_2)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(30, 10, 451, 238))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 2, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 6, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 3, 0, 1, 3)
        self.lineEdit_6 = LineEdit(self.gridLayoutWidget_2)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout_2.addWidget(self.lineEdit_6, 5, 1, 1, 2)
        self.lineEdit_5 = LineEdit(self.gridLayoutWidget_2)
        self.lineEdit_5.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout_2.addWidget(self.lineEdit_5, 2, 1, 1, 2)
        self.lineEdit_7 = LineEdit(self.gridLayoutWidget_2)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.gridLayout_2.addWidget(self.lineEdit_7, 6, 1, 1, 2)
        self.lineEdit_3 = LineEdit(self.gridLayoutWidget_2)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_2.addWidget(self.lineEdit_3, 0, 1, 1, 2)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)
        self.lineEdit_4 = LineEdit(self.gridLayoutWidget_2)
        self.lineEdit_4.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout_2.addWidget(self.lineEdit_4, 1, 1, 1, 2)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 1, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 5, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_2.addWidget(self.pushButton_3, 7, 0, 1, 3)
        self.tabWidget.addTab(self.tab_2, "")
        self.toolBox = QtWidgets.QToolBox(self.centralwidget)
        self.toolBox.setGeometry(QtCore.QRect(540, 150, 161, 261))
        self.toolBox.setObjectName("toolBox")
        self.page = QtWidgets.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 100, 30))
        self.page.setObjectName("page")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.page)
        self.commandLinkButton.setGeometry(QtCore.QRect(0, 0, 141, 71))
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.pushButton_4 = PrimaryPushButton(self.page)
        self.pushButton_4.setGeometry(QtCore.QRect(0, 70, 141, 32))
        self.pushButton_4.setObjectName("pushButton_4")
        self.toolBox.addItem(self.page, "")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 161, 209))
        self.page_2.setObjectName("page_2")
        self.pushButton = QtWidgets.QPushButton(self.page_2)
        self.pushButton.setGeometry(QtCore.QRect(0, 0, 131, 41))
        self.pushButton.setObjectName("pushButton")
        self.commandLinkButton_3 = QtWidgets.QCommandLinkButton(self.page_2)
        self.commandLinkButton_3.setGeometry(QtCore.QRect(0, 50, 161, 41))
        self.commandLinkButton_3.setObjectName("commandLinkButton_3")
        self.label_11 = QtWidgets.QLabel(self.page_2)
        self.label_11.setGeometry(QtCore.QRect(10, 170, 171, 41))
        self.label_11.setObjectName("label_11")
        self.toolBox.addItem(self.page_2, "")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 731, 141))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 731, 22))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menutest = QtWidgets.QMenu(self.menubar)
        self.menutest.setObjectName("menutest")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        MainWindow.setMenuBar(self.menubar)
        self.actionD = QtWidgets.QAction(MainWindow)
        self.actionD.setObjectName("actionD")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionsettings = QtWidgets.QAction(MainWindow)
        self.actionsettings.setObjectName("actionsettings")
        self.actionadd = QtWidgets.QAction(MainWindow)
        self.actionadd.setObjectName("actionadd")
        self.actiond = QtWidgets.QAction(MainWindow)
        self.actiond.setObjectName("actiond")
        self.actionopen = QtWidgets.QAction(MainWindow)
        self.actionopen.setObjectName("actionopen")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionD_2 = QtWidgets.QAction(MainWindow)
        self.actionD_2.setObjectName("actionD_2")
        self.actionopen_2 = QtWidgets.QAction(MainWindow)
        self.actionopen_2.setObjectName("actionopen_2")
        self.actionFeedBack = QtWidgets.QAction(MainWindow)
        self.actionFeedBack.setObjectName("actionFeedBack")
        self.actionsettings_2 = QtWidgets.QAction(MainWindow)
        self.actionsettings_2.setObjectName("actionsettings_2")
        self.menu.addAction(self.actionD)
        self.menu.addAction(self.actionD_2)
        self.menu.addAction(self.actionopen_2)
        self.menutest.addAction(self.actionAbout)
        self.menu_3.addAction(self.actionsettings_2)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menutest.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.toolBox.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "用户名："))
        self.label_2.setText(_translate("MainWindow", "密码："))
        self.pushButton_2.setText(_translate("MainWindow", "登录"))
        self.label_3.setText(_translate("MainWindow", "有疑问可前往帮助"))
        self.label_10.setText(_translate("MainWindow", "忘记密码（开发中）"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "登录"))
        self.label_7.setText(_translate("MainWindow", "确认密码："))
        self.label_9.setText(_translate("MainWindow", "答案："))
        self.label_6.setText(_translate("MainWindow", "专属问题设置（只能设置一个问题）："))
        self.label_4.setText(_translate("MainWindow", "用户名(英文)："))
        self.label_5.setText(_translate("MainWindow", "密码："))
        self.label_8.setText(_translate("MainWindow", "问题："))
        self.pushButton_3.setText(_translate("MainWindow", "注册"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "注册"))
        self.commandLinkButton.setText(_translate("MainWindow", "普通背单词\n"
"（Beta版推出）"))
        self.pushButton_4.setText(_translate("MainWindow", "我的计划"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("MainWindow", "功能"))
        self.pushButton.setText(_translate("MainWindow", "帮助(功能开发中)"))
        self.commandLinkButton_3.setText(_translate("MainWindow", "用户管理（更改、删除）"))
        self.label_11.setText(_translate("MainWindow", "今日已背单词：未登录"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("MainWindow", "设置"))
        self.menu.setTitle(_translate("MainWindow", "词库管理"))
        self.menutest.setTitle(_translate("MainWindow", "关于"))
        self.menu_3.setTitle(_translate("MainWindow", "settings"))
        self.actionD.setText(_translate("MainWindow", "add"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionsettings.setText(_translate("MainWindow", "settings"))
        self.actionadd.setText(_translate("MainWindow", "add"))
        self.actiond.setText(_translate("MainWindow", "d"))
        self.actionopen.setText(_translate("MainWindow", "open"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionD_2.setText(_translate("MainWindow", "D"))
        self.actionopen_2.setText(_translate("MainWindow", "open"))
        self.actionFeedBack.setText(_translate("MainWindow", "FeedBack"))
        self.actionsettings_2.setText(_translate("MainWindow", "settings"))
from qfluentwidgets import LineEdit, PrimaryPushButton, PrimaryToolButton
