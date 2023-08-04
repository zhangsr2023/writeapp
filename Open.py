from PyQt5 import QtWidgets, QtCore
import OpenUI
import os
import sqlite3
from PyQt5.QtWidgets import QMessageBox


# import json


class MainWindow(QtWidgets.QMainWindow, OpenUI.Ui_MainWindow):
    def __init__(self, user, data_path, func_enable, parent=None):
        super(MainWindow, self).__init__(parent)
        self.data_path = data_path
        self.user = user
        self.setupUi(self)
        self.setup_combo()  # 加载词库列表到界面
        self.pushButton.clicked.connect(self.open_database)
        self.func = func_enable

    def setup_combo(self):
        List = []
        for i in self.get_database_list():
            List.append(i.replace(".db", ""))
        self.comboBox.addItems(List)

    def open_database(self):
        name = self.comboBox.currentText()
        conn = sqlite3.connect("{}/user/{}/data/{}.db".format(self.data_path, self.user, name))
        cursor = conn.cursor()
        cursor.execute("select * from info")  # 查询 info 表单的数据
        data_1 = cursor.fetchall()
        cursor.execute("select * from word")  # 查询 word 表单的数据
        data = cursor.fetchall()
        # print(data_1)
        # print(data)
        cursor.close()
        conn.close()
        QMessageBox.information(None, "提示", "数据库加载成功", QMessageBox.Ok)
        from Edit import Edit
        self.user_window = Edit.MainWindow(data_1, data,
                                           "{}/user/{}/data/{}.db".format(self.data_path, self.user, name),
                                           is_function_enable=self.func)
        self.user_window.show()

    def get_database_list(self):
        return os.listdir("{}/user/{}/data".format(self.data_path, self.user))
