from PyQt5.QtCore import QByteArray, QSignalMapper, QSize, pyqtSignal, pyqtSlot
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QMainWindow, QPushButton, QMessageBox
from biology_test.ask import AskWidget

from biology_test.db.crud import Interface
from biology_test.uic.ui_mainwindow import Ui_MainWindow
from biology_test.main_rc import *


class MainWindow(QMainWindow):
    """
    Главное окно приложения
    """
    logout_signal = pyqtSignal()

    def __init__(self, interface: Interface, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.__interface = interface
        self.__mapper = QSignalMapper(self)
        self.__mapper.mapped[str].connect(self.select_category)
        self.__create_categories()

        self.ui.actionExit.triggered.connect(self.close_window)
        self.ui.actionLogout.triggered.connect(self.logout)

    @pyqtSlot()
    def close_window(self):
        self.close()

    @pyqtSlot()
    def logout(self):
        self.logout_signal.emit()
        self.close()

    def __create_categories(self):
        """
        Функция создает кнопки с темами для тестирования
        """
        categories = self.__interface.get_categories()
        for cat in categories:
            button = QPushButton(self)
            button.setText(cat["name"])
            if cat["image"] is not None:
                button.setIcon(QIcon(MainWindow.get_image(cat["image"])))
                button.setIconSize(QSize(32, 32))
            # закрепление сигнала со слотом
            button.clicked.connect(self.__mapper.map)
            self.__mapper.setMapping(button, cat["name"])
            # добавление кнопки в поле выбора
            self.ui.groupBoxCategories.layout().addWidget(button) # type: ignore
        self.ui.progressBar.setMaximum(len(categories) * 10)
        self.ui.progressBar.setMinimum(- (len(categories) * 10))

    @staticmethod
    def get_image(data: bytes) -> QPixmap:
        """
        Функция перекодирует байтовую строку в изображение, которое можно
        использовать в качестве иконки для кнопок
        """
        ba = QByteArray(data)
        img = QPixmap()
        img.loadFromData(ba)
        return img

    @pyqtSlot(str)
    def select_category(self, category: str):
        """
        Слот получает имя темы, и создает тест
        """
        asks = self.__interface.get_asks(category)
        self.setEnabled(False)
        asks = AskWidget(asks)
        asks.closed.connect(self.closed_test)
        asks.show()

    @pyqtSlot(int)
    def closed_test(self, score: int):
        """
        Слот вызывается, когда тест закончен
        """
        self.setEnabled(True)
        self.ui.progressBar.setValue(self.ui.progressBar.value() + score)
        self.__interface.update_rating(
            self.ui.progressBar.value(),
            self.ui.lineEditName.text(),
            self.ui.lineEditSurname.text(),
        )

    @pyqtSlot(str, str, str, str)
    def show_window(self, name: str, surname: str, password: str, classroom: str):
        """
        Слот принимает параметры пользователя, если его нет в системе, то
        создает нового пользователя.
        """
        try:
            user = self.__interface.get_user(name, surname, password, classroom)
            self.ui.lineEditName.setText(name)
            self.ui.lineEditSurname.setText(surname)
            self.ui.lineEditClass.setText(classroom)
            self.ui.progressBar.setValue(user["rating"])
            self.show()
        except KeyError as err:
            QMessageBox.critical(self, "Ошибка", str(err))
            self.logout_signal.emit()
            self.close()

