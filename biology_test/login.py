from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget

from biology_test.uic.ui_loginform import Ui_loginForm
from biology_test.main_rc import *


class Login(QWidget):
    """
    Диалог входа в систему
    """
    login = pyqtSignal(str, str, str, str)

    def __init__(self, classes: list[str], parent=None):
        super().__init__(parent)
        self.ui = Ui_loginForm()
        self.ui.setupUi(self)
        self.ui.loginButton.clicked.connect(self.continue_click)
        self.ui.comboBoxClass.addItems(classes)
        self.show()

    def continue_click(self):
        """
        Обработка события при нажатии на кнопку продолжить
        """
        name = self.ui.lineEditName.text()
        surname = self.ui.lineEditSurname.text()
        password = self.ui.lineEditPassword.text()
        classroom = self.ui.comboBoxClass.currentText()
        if all([name, surname, password]):
            self.login.emit(name, surname, password, classroom)
            self.close()
