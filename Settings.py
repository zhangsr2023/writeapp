import json
import os

from PyQt5 import QtWidgets, QtCore
from SettingsUI import Ui_MainWindow
from PyQt5.QtWidgets import QMessageBox
from qframelesswindow import AcrylicWindow, StandardTitleBar, FramelessWindow
from qfluentwidgets import setTheme, Theme


# import json


class MainWindow(QtWidgets.QMainWindow, FramelessWindow, Ui_MainWindow):
    def __init__(self, user, data, data_path, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.setTitleBar(StandardTitleBar(self))
        self.titleBar.raise_()

        setTheme(Theme.LIGHT)
        self.user = user
        self.data = data
        self.data_path = data_path
        QMessageBox.warning(None, "提醒", "设置路径时请小心\nBe careful when setting the path")
        if self.user == None:
            self.setWindowTitle("设置-未登录")
        else:
            self.setWindowTitle("设置-" + self.user)
        self.setup_ui()

    def setup_ui(self):
        with open("data/info.json", "r", encoding="utf-8") as f:
            d = json.load(f)
            data_path = d["path"]
        self.lineEdit.setText(data_path)
        self.pushButton.clicked.connect(self.choose_path)
        self.pushButton_2.clicked.connect(self.set_data_path)

    def choose_path(self):
        pass

    def set_data_path(self):
        p = self.lineEdit.text()
        if p[-1] == "\\" or p == "/":
            path = p + "StarGroup_data"
        else:
            path = p + "\\StarGroup_data"
        if "StarGroup_data" not in os.listdir(p):
            os.mkdir(path)
        else:
            if QMessageBox.warning(None, "",
                                "当前路径下已经有了StarGroup_data文件夹，这是由软件创建的，但如果是你自己创建的文件夹，请点击点击否以免文件被覆盖的风险\n是否更改路径？",
                                QMessageBox.Yes | QMessageBox.No) == QMessageBox.No:
                return False

        with open("data/info.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        data["path"] = p
        with open("data/info.json", "w", encoding="utf-8") as f:
            json.dump(data, f)
        QMessageBox.information(None, "提示", "路径修改成功，手动重启后生效！")
