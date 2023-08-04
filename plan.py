import json
import sqlite3

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import *
from planUI import Ui_MainWindow
import os
from PyQt5.QtWidgets import QMessageBox
from qframelesswindow import AcrylicWindow, StandardTitleBar, FramelessWindow
from qfluentwidgets import setTheme, Theme


# import json


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, data, path, user, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        # self.setTitleBar(StandardTitleBar(self))
        # self.titleBar.raise_()

        setTheme(Theme.LIGHT)
        self.data = data
        self.path = path
        self.user = user
        self.pushButton.clicked.connect(self.create_plan)
        self.setup_ui()  # 设置控件样式

    def setup_ui(self):
        self.commandLinkButton.clicked.connect(self.do_task)
        self.spinBox.setMinimum(1)  # 设置最小值
        self.radioButton.setChecked(True)
        self.radioButton_3.setChecked(True)
        if self.data is None:
            self.commandLinkButton.setEnabled(False)

        # 加载词库列表
        List = []
        for i in self.get_database_list():
            List.append(i.replace(".db", ""))
        self.comboBox.addItems(List)
        self.lcdNumber.setSegmentStyle(QLCDNumber.Flat)
        if self.data is None:
            self.lcdNumber.setProperty("value", "0")
        else:
            self.lcdNumber.setProperty("value", str(self.data["days"]))

    def get_database_list(self):
        return os.listdir("{}/user/{}/data".format(self.path, self.user))

    def do_task(self):
        print("do_task被调用")
        import study
        self.add_window = study.MainWindow(self.data, self.user, self.path)
        self.add_window.show()
        if self.add_window.is_rest:
            self.add_window.close()  # 关闭窗口

    def create_plan(self):
        name = self.comboBox.currentText()
        word_n = self.spinBox.value()  # 获取用户每日单词数量设置
        # 双重确认
        if QMessageBox.warning(None, "警告⚠️", "如果你已经有了计划，那么将会覆盖上一个计划，你确定吗？",
                               QMessageBox.Yes | QMessageBox.No) == QMessageBox.No:
            return False
        if QMessageBox.warning(None, "再次警告⚠️", "如果你已经有了计划，那么将会覆盖上一个计划。",
                               QMessageBox.Yes | QMessageBox.No) == QMessageBox.No:
            return False

        with open("{}/user/{}/plan.json".format(self.path, self.user), "w", encoding="utf-8") as f:
            conn = sqlite3.connect("{}/user/{}/data/{}.db".format(self.path, self.user, name))
            cursor = conn.cursor()
            cursor.execute("select * from info")  # 查询 info 表单的数据
            data_1 = cursor.fetchall()
            cursor.execute("select * from word")  # 查询 word 表单的数据
            data = cursor.fetchall()
            # print(data_1)
            # print(data)
            cursor.close()
            conn.close()
            status = self.radioButton_4.isChecked()
            plan_data = self.ebbinghaus(word_n, data, recite=self.radioButton_2.isChecked(),
                                        check=status)
            print(status)
            json.dump(plan_data, f)
            QMessageBox.information(None, "提示", "计划创建成功!!! 预计需要{}天".format(plan_data["days"]))

    @staticmethod
    def ebbinghaus(number: int, data: list, check: bool, recite: bool = False) -> dict:
        """

        :param number: 每日背的单词数量
        :param data: 词库数据
        :param recite: 背诵模式 严格为 True
        :param check: 校对模式 校对第二语言为 True
        :return: 计划数据（可以直接保存至.json文件中）
        """
        data_list = []
        for i in data:
            data_list.append([i[1], i[2], i[3]])
        # print(data_list)
        numbers = len(data_list)  # 单词总数量
        groups = numbers // number
        last_group_number = 0  # 最后一组需要背的单词量
        if numbers % number != 0:
            last_group_number = numbers % number
        groups_data = []
        temp = 0
        for i in range(groups):
            data_temp = []
            for x in range(number):
                data_temp.append(data_list[temp + x])
            # print(data_temp)
            groups_data.append(data_temp)
            temp += number
        data_temp = []
        for i in range(last_group_number):
            data_temp.append(data_list[temp + i])
        if last_group_number != 0:
            groups_data.append(data_temp)
        # if last_group_number != 0:
        #     print(data_temp)
        del data_temp
        del temp
        listcount = len(groups_data)  # 单词组的总数量
        # 制定生成规则
        if recite:
            days = [1, 2, 3, 5, 11, 19]
        else:
            days = [1, 2, 4, 7, 15]
        List = [[] for i in range(listcount + max(days))]
        for i in range(listcount):
            List[i].append(i)
            for j in days:
                List[i + j].append(i)
        day_number = len(List)
        for i in List:
            print(i)
        print(day_number)
        result = {
            "info": 1,
            "total days": day_number,
            "days": day_number,  # 剩余天数
            "groups data": groups_data,
            "plan data": List,
            "check": check
        }
        return result


if __name__ == '__main__':
    data = [
        (0, "你好", "hello", 3),
        (0, "苹果🍎", "apple", 3),
        (0, "香蕉🍌", "banana", 4),
        (0, "漂亮的", "beautiful", 5),
        (0, "调试程序", "debug", 3),
        (0, "名字", "name", 4),
        (0, "微软", "Microsoft", 3),
        (0, "信息", "information", 2)
    ]
    print(MainWindow.ebbinghaus(data, recite=True))
