from PyQt5 import QtWidgets, uic
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.uic.properties import QtGui
import sqlite3

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.text_formatting()

        self.login_button.clicked.connect(self.login)
        self.actionsign_out.triggered.connect(self.sign_out)
        self.submit_button.clicked.connect(self.add_to_list)
        self.delete_button.clicked.connect(self.delete_from_list)

        self.current_asset_number = 0

    def login(self):
        username = self.password_edit.text()
        password = self.password_edit.text()

        if username == "test" and password == "test":
            self.stackedWidget.setCurrentIndex(1)
            self.username_edit.setText("")
            self.password_edit.setText("")
            con = sqlite3.connect("assets.db")
            cur = con.cursor()

            result = cur.execute('SELECT * FROM Assets')
            rows = result.fetchall()
            for row in rows:
                self.current_asset_number += 1
                self.asset_number = cur.execute("SELECT asset_number FROM Assets")
                self.asset_name =cur.execute("SELECT asset_name FROM Assets")
                self.assignee = cur.execute("SELECT assignee FROM Assets")
                self.list_item_name = f"#{str(self.asset_number)}: {str(self.asset_name)} - Assigned to: {str(self.assignee)}"
                self.asset_list.addItem(self.list_item_name)
            con.close()


            if self.current_asset_number == 0:
                self.asset_number_edit.setText(f'00001')
            if self.current_asset_number in range(1, 9):
                self.current_asset_number += 1
                self.asset_number_edit.setText(f'0000{str(self.current_asset_number)}')
            if self.current_asset_number in range(10, 99):
                self.current_asset_number += 1
                self.asset_number_edit.setText(f'000{str(self.current_asset_number)}')
            if self.current_asset_number in range(100, 999):
                self.current_asset_number += 1
                self.asset_number_edit.setText(f'00{str(self.current_asset_number)}')
            if self.current_asset_number in range(1000, 9999):
                self.current_asset_number += 1
                self.asset_number_edit.setText(f'0{str(self.current_asset_number)}')
            if self.current_asset_number in range(10000, 99999):
                self.current_asset_number += 1
                self.asset_number_edit.setText(f'{str(self.current_asset_number)}')
        else:
            pass

    def sign_out(self):
        self.stackedWidget.setCurrentIndex(0)
        self.asset_list.clear()

    def add_to_list(self):
        self.asset_number = self.asset_number_edit.text()
        self.asset_name = self.asset_name_edit.text()
        self.assignee = self.assignee_edit.text()

        con = sqlite3.connect("assets.db")
        cur = con.cursor()
        cur.execute(f"""
                    INSERT INTO Assets VALUES
                    ('{self.asset_number}', '{self.asset_name}', '{self.assignee}')
        """)
        con.commit()

        self.list_item_name = f"#{self.asset_number}: {self.asset_name} - Assigned to: {self.assignee}"
        self.asset_list.addItem(self.list_item_name)


        self.current_asset_number += 1
        self.asset_number_edit.setText(self.current_asset_number)
        self.asset_name_edit.setText("")
        self.assignee_edit.setText("")

    def delete_from_list(self):
        pass

    def text_formatting(self):
        self.username_edit.setAlignment(Qt.AlignCenter)
        self.password_edit.setAlignment(Qt.AlignCenter)
        self.password_edit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.asset_number_edit.setAlignment(Qt.AlignCenter)
        self.asset_name_edit.setAlignment(Qt.AlignCenter)
        self.assignee_edit.setAlignment(Qt.AlignCenter)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MyWindow()
    mainWindow.show()
    sys.exit(app.exec_())