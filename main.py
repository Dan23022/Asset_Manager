from PyQt5 import QtWidgets, uic
import sys
from PyQt5.QtWidgets import *


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.login_button.clicked.connect(self.page1)
        self.actionsign_out.triggered.connect(self.page2)
        self.submit_button.clicked.connect(self.add_to_list)

    def page1(self):
        email = self.email_edit.text()
        password = self.password_edit.text()
        print(email)
        if email == "test" and password == "test":
            self.stackedWidget.setCurrentIndex(1)
        else:
            pass

    def page2(self):
        self.stackedWidget.setCurrentIndex(0)

    def add_to_list(self):
        asset_number =  self.asset_number_edit.text()
        asset_type = self.asset_type_edit.text()
        assignee = self.assignee_edit.text()

        list_item_name = f"{asset_number}: {asset_type} - Assigned to: {assignee}"

        self.asset_list.addItem(list_item_name)

        
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MyWindow()
    mainWindow.show()
    sys.exit(app.exec_())