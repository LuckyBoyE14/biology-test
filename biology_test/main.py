"""
Главный модуль приложения
"""
import sys
from PyQt5.QtWidgets import QApplication

from biology_test.db.config import engine
from biology_test.db.crud import Interface
from biology_test.main_window import MainWindow
from biology_test.login import Login
from biology_test.main_rc import *


def main():
    """
    Точка входа в приложение
    """
    app = QApplication(sys.argv)
    interface = Interface(engine)
    # Создание окна для авторизации
    login = Login(classes=interface.get_classes())
    mainwindow = MainWindow(interface=interface)
    login.login.connect(mainwindow.show_window)
    mainwindow.logout_signal.connect(login.show)
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
