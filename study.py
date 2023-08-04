import json

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import *
from do import Ui_MainWindow
import os
from PyQt5.QtWidgets import QMessageBox
from qframelesswindow import AcrylicWindow, StandardTitleBar, FramelessWindow
from qfluentwidgets import setTheme, Theme
from PyQt5.QtWidgets import QMessageBox


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, data, username, path, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.is_rest = False
        self.test_index = 0
        self.test_result = []
        self.user = username
        self.path = path
        self.data = data  # 接收计划数据
        self.setup_ui()
        setTheme(Theme.LIGHT)
        # if self.is_rest:
        #     self.close() # 关闭窗口

    def setup_ui(self):
        self.current = self.data["total days"] - self.data["days"]
        if self.data["plan data"][self.current] == []:
            QMessageBox.information(None, "提示", "今天休息没有学习或复习单词😊,自动为你开启下一天")
            with open("{}/user/{}/plan.json".format(self.path, self.user), "w", encoding="utf-8") as f:
                current = self.data["days"]
                self.data["days"] = current - 1
                if current - 1 == 0:
                    self.data["info"] = 0
                    QMessageBox.information(None, "🎉", "恭喜你已经完成了本计划任务！")
                json.dump(self.data, f)
            self.is_rest = True
        else:
            self.pushButton.clicked.connect(self.start_test)
            self.a = self.get_data()
            self.row_count = len(self.a)
            self.tableWidget.setRowCount(self.row_count)  # 设置表格行数
            self.tableWidget.setColumnCount(2)  # 设置表格列数
            self.tableWidget.setHorizontalHeaderLabels(["参照语言", "考察语言"])
            # data = QTableWidgetItem("test text")
            self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)  # 禁止用户编辑
            # self.tableWidget.setItem(0, 0, data)

            index = 0
            for i in self.a:
                data = QTableWidgetItem(i[0])
                self.tableWidget.setItem(index, 0, data)
                data = QTableWidgetItem(i[1])
                self.tableWidget.setItem(index, 1, data)
                index += 1

    def start_test(self):
        if self.test_index >= 1:
            answer = self.textEdit.toPlainText()
            if self.a[self.test_index - 1][1] == answer:
                self.test_result.append(True)  # 记录答案正确
            else:
                self.test_result.append(False)  # 记录答案错误
        if self.row_count == self.test_index:  # self.row_count - 1 == ...
            self.label_2.setText("题目：已结束检验")
            self.pushButton.setEnabled(False)
            self.textEdit.setEnabled(False)
            error_times = 0
            for index, i in enumerate(self.test_result):
                if not i:
                    error_times += 1
                    QMessageBox.warning(None, "错题{}".format(error_times),
                                        "题目：{}\n答案:{}".format(self.a[index][0], self.a[index][1]))

            QMessageBox.information(None, "提示", "检验结束，一共{}道错题".format(error_times))
            with open("{}/user/{}/plan.json".format(self.path, self.user), "w", encoding="utf-8") as f:
                current = self.data["days"]
                self.data["days"] = current - 1
                if current - 1 == 0:
                    self.data["info"] = 0
                    QMessageBox.information(None, "🎉", "恭喜你已经完成了本计划任务！")
                json.dump(self.data, f)

        else:
            self.label_2.setText("题目：" + self.a[self.test_index][0])
            self.test_index += 1

    def get_data(self):
        result = []
        groups = self.data["plan data"][self.current]
        for i in groups:
            data = self.data["groups data"][i]
            for x in data:
                result.append(x)
        return result
