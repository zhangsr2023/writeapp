import sqlite3

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import *
from . import EditUI


# import json


class MainWindow(QtWidgets.QMainWindow, EditUI.Ui_MainWindow):
    def __init__(self, data_1, data, data_path, is_function_enable, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.data = data
        print(self.data)
        self.data_1 = data_1
        self.data_path = data_path
        self.row_count = 0
        self.tableWidget.itemClicked.connect(self.setup_data)
        self.setup_GUI()  # 界面显示初始化
        self.pushButton.clicked.connect(self.add_data)
        self.pushButton_2.clicked.connect(self.delete_data)
        if not is_function_enable:
            self.pushButton_2.setEnabled(False)

    def get_last_data_id(self):
        if len(self.data) == 0:
            result = 0
        else:
            result = self.data[-1][0]
        return result

    def setup_GUI(self):
        self.actiondata_settings.setText("词库属性设置（正式版推出）")
        self.row_count = len(self.data)
        self.tableWidget.setRowCount(self.row_count)  # 设置表格行数
        self.tableWidget.setColumnCount(2)  # 设置表格列数
        self.tableWidget.setHorizontalHeaderLabels(["中文", "English"])
        for i in range(self.row_count):
            for x in range(1, 3):
                data = QTableWidgetItem(str(self.data[i][x]))

                self.tableWidget.setItem(i, x - 1, data)  # 将数据填入表格
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()
        self.tableWidget.setAlternatingRowColors(True)  # 让表格颜色交错显示
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)  # 禁止编辑表格
        self.tableWidget.horizontalHeader().setStretchLastSection(True)

    def add_data(self):
        l1 = self.lineEdit.text()
        l2 = self.lineEdit_2.text()
        if len(l1) > 30 or len(l2) > 30:
            QMessageBox.critical(None, "错误", "第一语言或者第二语言字符长度不能超过30！")
            return False
        data = (self.get_last_data_id() + 1, l1, l2)
        self.tableWidget.setRowCount(self.row_count)
        for i in range(1, 3):
            data_q = QTableWidgetItem(str(data[i]))
            self.tableWidget.setItem(self.row_count - 1, i - 1, data_q)
        # self.data.append(data)
        # 修改数据库里的数据
        conn = sqlite3.connect(self.data_path)
        cursor = conn.cursor()
        print(self.get_last_data_id())
        print(type(self.get_last_data_id()))
        print("标识", self.get_last_data_id() + 1, l1, l2, 3)
        print(self.data)
        cursor.execute("insert into word (id, l1, l2, important) values (?,?,?,?)",
                       (self.get_last_data_id() + 1, l1, l2, 3))
        self.data.append(data)
        self.row_count += 1
        self.tableWidget.setRowCount(self.row_count)
        for i in range(self.row_count):
            print(i)
            for x in range(1, 3):
                Qdata = QTableWidgetItem(str(self.data[i][x]))

                self.tableWidget.setItem(i, x - 1, Qdata)  # 将数据填入表格
        # self.data.append(data)
        # cursor.execute("update word set l2 = ?", (l2, self.row_count))
        cursor.close()
        conn.commit()
        conn.close()

    def delete_data(self):
        id = self.data[self.select_n][0]
        self.row_count -= 1
        l1 = self.lineEdit.text()
        l2 = self.lineEdit_2.text()
        # if len(l1) > 30 or len(l2) > 30:
        #     QMessageBox.critical(None, "错误", "第一语言或者第二语言字符长度不能超过30！")
        #     return False
        data = (self.row_count - 1, l1, l2)
        self.tableWidget.setRowCount(self.row_count)
        for i in range(1, 3):
            data_q = QTableWidgetItem(str(data[i]))
            self.tableWidget.setItem(self.row_count - 1, i - 1, data_q)
        del self.data[self.select_n]
        # 修改数据库里的数据
        conn = sqlite3.connect(self.data_path)
        cursor = conn.cursor()
        cursor.execute("delete from word where id = ?", (id,))
        # cursor.execute("update word set l2 = ?", (l2, self.row_count))
        cursor.close()
        conn.commit()
        conn.close()
        for i in range(self.row_count):
            for x in range(1, 3):
                Qdata = QTableWidgetItem(str(self.data[i][x]))

                self.tableWidget.setItem(i, x - 1, Qdata)  # 将数据填入表格
        QMessageBox.information(None, "提示", "单词删除成功")

    def setup_data(self, item):
        self.select_n = item.row()
        self.select_data = self.data[self.select_n]
        self.lineEdit.setText(self.select_data[1])
        self.lineEdit_2.setText(self.select_data[2])
