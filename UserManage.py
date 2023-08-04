from PyQt5 import QtWidgets, QtCore
from UserManageUI import Ui_MainWindow
from PyQt5.QtWidgets import QMessageBox
import json
import os
import shutil


# import json


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, f, path, parent=None):
        super(MainWindow, self).__init__(parent)
        self.f = f
        self.path = path
        self.setupUi(self)
        self.setup_ui()

    def setup_ui(self):
        self.pushButton_2.clicked.connect(self.del_user)
        self.pushButton.clicked.connect(self.change_password)

    def del_user(self):
        name = self.lineEdit_4.text()
        password = self.lineEdit_5.text()
        if name not in self.f():
            QMessageBox.warning(None, "输入错误", "输入的用户名不存在", QMessageBox.Ok)
            return False
        with open("{}/user/{}/info.json".format(self.path, name), "r", encoding="utf-8") as f:
            data = json.load(f)
        if data["password"] != password:
            QMessageBox.critical(None, "输入错误", "密码错误", QMessageBox.Ok)
            return False
        a = QMessageBox.warning(None, "警告⚠️", "你确定要删除用户{}吗？".format(name),
                                QMessageBox.Discard | QMessageBox.No)
        if a == QMessageBox.No:
            return False
        b = QMessageBox.warning(None, "警告⚠️", "删除用户意味着你的所有词库将不可挽回的删除！！！确认删除吗？".format(name),
                                QMessageBox.Discard | QMessageBox.No)
        if b == QMessageBox.No:
            return False
        shutil.rmtree("{}/user/{}/data".format(self.path, name))  # 删除用户所有数据库
        os.remove("{}/user/{}/info.json".format(self.path, name))  # 删除用户信息
        try:
            os.rmdir("{}/user/{}".format(self.path, name))  # 尝试删除用户文件夹
        except OSError:
            QMessageBox.information(None, "警告", "检测到你在部分地方有其他文件，我们暂时没有删除你的用户文件夹",
                                    QMessageBox.Ok)
        QMessageBox.information(None, "提示", "用户删除成功", QMessageBox.Ok)

    def change_password(self):  # 修改用户密码
        name = self.lineEdit.text()
        password = self.lineEdit_2.text()
        new = self.lineEdit_3.text()
        if "." in name:
            QMessageBox.warning(None, "", "输入的不是用户名")
            return False
        try:
            with open("{}/user/{}/info.json".format(self.path, name), "r", encoding="utf-8") as f:
                data = json.load(f)
        except FileNotFoundError as u:
            QMessageBox.critical(None, "警告", "用户名不正确 - {}".format(u))
            return False
        except Exception as e:
            QMessageBox.critical(None, "ERROR", e)
            exit(-2)
        if password != data["password"]:
            QMessageBox.critical(None, "错误", "原密码不正确", QMessageBox.Ok)
            return False
        data["password"] = new
        with open("{}/user/{}/info.json".format(self.path, name), "w", encoding="utf-8") as f:
            json.dump(data, f)
        QMessageBox.information(None, "", "密码更改成功")
