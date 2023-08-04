from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMessageBox
from AppDataUI import Ui_MainWindow_Add
import sqlite3


# import json


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow_Add):
    def __init__(self, file_data, user, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.data_file = file_data
        self.user = user
        self.pushButton.clicked.connect(self.add)
        self.label.setText("词库名")

    def add(self):
        name = self.lineEdit.text()
        try:
            conn = sqlite3.connect("{}/user/{}/data/{}.db".format(self.data_file, self.user, name))  # 创建数据库
            cursor = conn.cursor()
            """
            l_name: 
            1：中文
            2：英文
            """
            cursor.execute("create table info(name1 integer,name2 integer,is_spell bit)")
            cursor.execute(
                "create  table  word (id int primary key , l1 varchar(30), l2 varchar(30), important int)")
            # 写入词库设置信息
            cursor.execute("insert into info (name1,name2,is_spell) values (1,2,1)")
            cursor.close()
            conn.commit()
            conn.close()
            QMessageBox.information(None, "提示", "数据库创建成功")
        except Exception as e:
            QMessageBox.critical(None, "错误", "0x3EB数据创建失败 {}".format(e), QMessageBox.Ok)


def main():
    import sys

    app = QtWidgets.QApplication(sys.argv)
    # 重新设置标题
    mainwindow = MainWindow()
    # mainwindow.setWindowTitle("主界面-{}".format(data[0]))
    # mainwindow.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
    mainwindow.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
