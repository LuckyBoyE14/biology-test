from typing import Any, Generator
from PyQt5.QtCore import QByteArray, QSignalMapper, QSize, pyqtSignal, pyqtSlot
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QMainWindow, QPushButton, QMessageBox, QRadioButton, QWidget

from biology_test.uic.ui_askform import Ui_Form
from biology_test.main_rc import *


class AskWidget(QWidget):
    """
    Виджет для вопросов
    """
    closed = pyqtSignal(int)

    def __init__(self, questions: list[dict[Any, Any]], parent=None):
        super().__init__(parent)
        self.__score = 0
        self.__count_qusetions = len(questions)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.__gen = self.get_next_question(questions)
        self.update_data()

        self.ui.pushButton.clicked.connect(self.click_continue)

    def closeEvent(self, event):
        self.closed.emit(0)

    def get_next_question(self, questions) -> Generator[dict[Any, Any], None, None]:
        """
        Генератор для обновления вопросов
        """
        for question in questions:
            yield question

    def clear_answers(self):
        layout = self.ui.widgetAnswers.layout()
        if layout is None or layout.count() == 0:
            return
        while layout.count() > 0:
            item = layout.takeAt(0)
            if item is not None:
                layout.removeWidget(item.widget())

    def update_data(self):
        """
        Функция обновляет вопросы на форме
        """
        try:
            self.clear_answers()
            question = next(self.__gen)
            print(question)
            self.ui.textEditAsk.setText(question["text"])
            for answer in question["answers"]:
                radio = QRadioButton(self.ui.widgetAnswers)
                radio.setText(answer["text"])
                radio.setObjectName("correct" if answer["is_true"] else "nocorrect")
                self.ui.widgetAnswers.layout().addWidget(radio) # type: ignore
        except StopIteration:
            QMessageBox.information(self, "Тест завершен",
                                    f"Вы набрали: {self.__score} из {self.__count_qusetions}")
            self.closed.emit(self.__score)
            self.close()

    @pyqtSlot()
    def click_continue(self):
        """
        Слот обрабатывает нажатие кнопки продолжить
        """
        layout = self.ui.widgetAnswers.layout()
        if layout is None or layout.count() == 0:
            return
        is_correct = False
        for idx in range(layout.count()):
            item = layout.itemAt(idx)
            if item is not None:
                radio = item.widget()
                is_correct = is_correct or (
                    radio.isChecked() and radio.objectName() == "correct"
                )
        if is_correct:
            self.__score += 1
            print("Выбран правильный вариант ответа")
        else:
            self.__score -= 1
            print("Выбран не правильный вариант ответа")
            QMessageBox.warning(self, "Ошибка", "Это не праильный ответ!")
        self.update_data()
