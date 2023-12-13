import time

from PyQt5 import QtWidgets, QtCore
import importlib

from PyQt5.Qt import Qt

import AppDataUI
from MainUI import Ui_MainWindow
from PyQt5.QtWidgets import QMessageBox
import json
import os
import logging
from qframelesswindow import AcrylicWindow, StandardTitleBar, FramelessWindow
from qfluentwidgets import setTheme, Theme, FluentIcon, SplitFluentWindow

logging.basicConfig(level=logging.DEBUG, format="%(funcName)s %(asctime)s %(name)s %(levelname)s: %(message)s",
                    filename="logs/root.log")
user_log = logging.getLogger("user")

# import easygui
# 加载数据存储路径

with open("data/info.json", "r", encoding="utf-8") as f:
    data_path = json.load(f)["path"]
    if data_path[-1] == "\\" or data_path == "/":
        path = data_path + "StarGroup_data"
    else:
        path = data_path + "\\StarGroup_data"
    data_path = path

# 加载软件设置
try:
    with open("{}/product_settings.json".format(data_path), "r", encoding="utf-8") as f:
        settings = json.load(f)
except FileNotFoundError:
    with open("{}/product_settings.json".format(data_path), "w", encoding="utf-8") as f:
        settings = {
            "experiment": {
                "Alpha function enable": False
            },
            "info": {
                "version": "2.0"
            }
        }
        json.dump(settings, f)
    os.mkdir(data_path + "/user")  # 构建数据存储架构
logging.info("加载软件设置")


def load(name):
    mod = importlib.import_module(name, package="plugins")
    cls = getattr(mod, "Main")
    return cls


def load_data():  # 加载所有数据
    with open("data/info.json", "r", encoding="utf-8") as f:
        data_info = json.load(f)
        d = data_info["path"]
        if d[-1] == "\\" or d == "/":
            path = d + "StarGroup_data"
        else:
            path = d + "\\StarGroup_data"
        data_info["path"] = path
        version = data_info["version"]
        return (version, data_info)


def get_user_list():
    return os.listdir(data_path + "/user")


data = load_data()  # 加载数据


class MainWindow(QtWidgets.QMainWindow, StandardTitleBar, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.user = None
        # 界面设置
        self.setupUi(self)
        self.actionAbout.triggered.connect(self.about)
        self.actionD.triggered.connect(lambda: self.open(0))
        self.commandLinkButton_3.clicked.connect(lambda: self.open(1))
        self.pushButton_3.clicked.connect(self.create_user)
        self.pushButton.clicked.connect(self.help)
        self.actionsettings_2.triggered.connect(lambda: self.open(2))
        self.pushButton_2.clicked.connect(self.login)
        logging.info("进行界面设置")
        self.actionopen_2.triggered.connect(lambda: self.open(3))
        self.pushButton_4.clicked.connect(lambda: self.open(4))
        # self.lineEdit_2.setPlaceholderText("这里要跟问题一样哦")
        # self.setTitleBar(StandardTitleBar(self))
        # self.titleBar.raise_()
        self.PrimaryToolButton.setIcon(FluentIcon.LINK)

        setTheme(Theme.LIGHT)
        # self.commandLinkButton_2.clicked.connect(self.setup_forget)
        self.set_geo()  # 设置样式
        QMessageBox.warning(None, "警告",
                            "该项目主要目的为练习编程技术，目前版本可能会出现严重BUG。（特别提醒配置路径时需要小心）\n"
                            "The main purpose of this project is to practice programming techniques, and there may"
                            " be serious bugs in the current version. (Special reminder to be careful when configuring paths)")
        if data_path == "data\\StarGroup_data" or data_path == "data/StarGroup_data":
            QMessageBox.information(None, "警告",
                                    "你目前还没有设置数据存储路径，或者更新了软件，我们已经设置成了默认路径 软件目录/data 请在 设置-通用-软件数据存储路径 修改设置，否则下次升级后数据将会被覆盖！")

    def help(self):
        pass

    def set_geo(self):
        self.actionD.setText("添加词库")
        self.actionD.setEnabled(False)
        self.actionD_2.setText("删除词库(正在开发)")
        self.actionD_2.setEnabled(False)
        self.actionopen_2.setText("打开词库")
        self.actionopen_2.setEnabled(False)
        self.pushButton_4.setEnabled(False)
        if not settings["experiment"]["Alpha function enable"]:
            self.label_11.setText("功能未启用")
        self.commandLinkButton.setEnabled(False)

    def open(self, name):
        if name == 0:
            import AppData
            self.add_window = AppData.MainWindow(data_path, self.user)
            self.add_window.show()
        elif name == 1:
            import UserManage
            self.user_window = UserManage.MainWindow(get_user_list, data_path)
            self.user_window.show()
        elif name == 2:
            import Settings
            self.settings_window = Settings.MainWindow(self.user, settings, data_path)
            self.settings_window.show()
        elif name == 3:
            import Open
            self.open_window = Open.MainWindow(user=self.user, data_path=data_path,
                                               func_enable=settings["experiment"]["Alpha function enable"])
            self.open_window.show()
        elif name == 4:
            import plan
            with open("{}/user/{}/plan.json".format(data_path, self.user), "r", encoding="utf-8") as f:
                data = json.load(f)
                if data["info"] == 0:
                    data = None
            self.plan_window = plan.MainWindow(data, data_path, self.user, self.user_info,
                                               is_func_enable=settings["experiment"]["Alpha function enable"])
            self.plan_window.show()

        else:
            QMessageBox.critical(None, "错误", "[0x3E9] 窗口加载失败")

    def about(self):
        text = """
        版本：{}
        开发者：zhangsr
        """.format(data[0])
        QMessageBox.about(None, "关于软件", text)

    def login(self):
        user_name = self.lineEdit.text()
        password = self.lineEdit_2.text()
        try:
            with open("{}/user/{}/info.json".format(data_path, user_name), "r") as f:
                data = json.load(f)
                have_sh = True  # 是否是新版本数据 是否拥有 study history
                if password == data["password"]:
                    self.user = user_name  # 更新登录状态
                    # 登录后允许用户使用以下功能
                    self.actionD.setEnabled(True)
                    self.actionD_2.setEnabled(True)
                    self.actionopen_2.setEnabled(True)
                    self.pushButton_4.setEnabled(True)
                    self.commandLinkButton.setEnabled(True)
                    logging.info("登录操作")
                    if "study history" in data:
                        pass
                    else:
                        have_sh = False
                    if not have_sh:
                        data["study history"] = {}  # 为低版本升级上来的用户提供兼容支持
                        with open("{}/user/{}/info.json".format(data_path, user_name), "w") as f1:
                            json.dump(data, f1)
                    if settings["experiment"]["Alpha function enable"]:
                        if time.strftime("%Y-%m-%d") in data["study history"]:
                            self.label_11.setText(
                                "今日已背单词：" + str(data["study history"][time.strftime("%Y-%m-%d")][0]))
                        else:
                            self.label_11.setText("今日还没有背诵单词，快点击我的计划开始背诵吧")
                    self.user_info = data

                    QMessageBox.information(None, "提示", "登录成功", QMessageBox.Ok)
                else:
                    QMessageBox.information(None, "警告", "密码错误", QMessageBox.Ok)
                    user_log.warning("密码输入错误")
        except FileNotFoundError:
            QMessageBox.critical(None, "错误", "[0x3EA]用户名不存在或文件数据出现问题!", QMessageBox.Ok)

    def create_user(self):
        # 获取用户的所有输入
        user_name = self.lineEdit_3.text()
        if user_name == "" or "." in user_name or "/" in user_name or "\\" in user_name:
            QMessageBox.critical(None, "警告", "不允许用户名为空，同时不允许含有英文句号、斜杠或反斜杠！", QMessageBox.Ok)
            return False
        password = self.lineEdit_4.text()
        password_again = self.lineEdit_5.text()
        question = self.lineEdit_6.text()
        answer = self.lineEdit_7.text()
        for i in get_user_list():
            if i == user_name:
                QMessageBox.critical(None, "警告", "此用户已存在！！！", QMessageBox.Ok)
                return False
        if password != password_again:
            QMessageBox.warning(None, "提示", "你输入的两次密码不一致！", QMessageBox.Ok)
            return False
        os.mkdir("{}/user/{}".format(data_path, user_name))  # 创建用户文件夹
        with open("{}/user/{}/info.json".format(data_path, user_name), "w") as f:
            # os.mkdir("{}/user/{}".format(data_path, user_name))
            data = {"password": password, "question": question, "answer": answer}
            json.dump(data, f)
            os.mkdir("{}/user/{}/data".format(data_path, user_name))
        with open("{}/user/{}/plan.json".format(data_path, user_name), "w", encoding="utf-8") as f:
            result = {
                "info": 0,
            }
            json.dump(result, f)
            QMessageBox.information(None, "提示", "用户创建成功！", QMessageBox.Ok)

    def setup_forget(self):
        self.pushButton_2.setText("找回密码")
        self.pushButton_2.clicked.connect(lambda: self.forget_password(name))
        self.label_2.setText("问题")
        name = self.lineEdit.text()
        all_user = get_user_list()
        if name not in all_user:
            QMessageBox.critical(None, "警告", "你输入的用户名不存在", QMessageBox.Ok)
            return False
        with open("{}/user/{}/info.json".format(data_path, name), "r", encoding="utf-8") as f:
            self.user_load_data = json.load(f)
            self.label_3.setText("问题：{}".format(self.user_load_data["question"]))
            self.label_2.setText("问题回答：")
            # 校对用户的回答是否正确
            # self.label_2.setText("问题�答：")
            # self.label_3.setText("问题：{}".format(self.user_load_data["question"]))

        # QMessageBox.critical(None, "错误", "问题回答错误！", QMessageBox.Ok)

    def forget_password(self, name):
        if self.lineEdit_2 == self.user_load_data["answer"]:
            with open("{}/user/{}/info.json".format(data_path, name), "w", encoding="utf-8") as f:
                self.user_load_data["password"] = "123456"
                json.dump(self.user_load_data, f)
                QMessageBox.information(None, "警告⚠️",
                                        "已经将您的密码修改为123456，为了你的安全🔐，请您尽快到 用户管理-更改密码 处更改密码！",
                                        QMessageBox.Ok)
            self.pushButton_2.setText("登录")
            self.pushButton_2.clicked.connect(self.login)
            self.label_2.setText("密码：")
            self.label_3.setText("有疑问可前往帮助")

            return True


if __name__ == '__main__':
    import sys

    QtCore.QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)  # 适应windows缩放
    app = QtWidgets.QApplication(sys.argv)
    # apply_stylesheet(app, theme='light_purple.xml')
    # 重新设置标题
    mainwindow = MainWindow()
    mainwindow.setFixedSize(731, 450)  # 设置禁止改变窗口大小
    mainwindow.setWindowTitle("主界面-{}".format(data[0]))
    # mainwindow.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
    mainwindow.show()
    # p = PluginsManager(load(".test"))
    sys.exit(app.exec_())
