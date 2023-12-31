# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'biology_test/ui/main.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(985, 600)
        font = QtGui.QFont()
        font.setPointSize(14)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/static/images/main.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QtCore.QSize(256, 256))
        self.frame_2.setMaximumSize(QtCore.QSize(256, 256))
        self.frame_2.setStyleSheet("border-image: url(:/images/static/images/avatar.png)  0 0 0 0 stretch stretch;\n"
"border: 3px solid black;\n"
"border-radius: 128")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2.addWidget(self.frame_2)
        self.groupBox_2 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_2.setObjectName("groupBox_2")
        self.formLayout = QtWidgets.QFormLayout(self.groupBox_2)
        self.formLayout.setObjectName("formLayout")
        self.labelSurname = QtWidgets.QLabel(self.groupBox_2)
        self.labelSurname.setObjectName("labelSurname")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.labelSurname)
        self.lineEditSurname = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEditSurname.setEnabled(False)
        self.lineEditSurname.setObjectName("lineEditSurname")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEditSurname)
        self.lineEditName = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEditName.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditName.sizePolicy().hasHeightForWidth())
        self.lineEditName.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEditName.setFont(font)
        self.lineEditName.setObjectName("lineEditName")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEditName)
        self.labelName = QtWidgets.QLabel(self.groupBox_2)
        self.labelName.setObjectName("labelName")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.labelName)
        self.lineEditClass = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEditClass.setEnabled(False)
        self.lineEditClass.setObjectName("lineEditClass")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEditClass)
        self.labelClass = QtWidgets.QLabel(self.groupBox_2)
        self.labelClass.setObjectName("labelClass")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.labelClass)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(3, QtWidgets.QFormLayout.FieldRole, spacerItem)
        self.progressBar = QtWidgets.QProgressBar(self.groupBox_2)
        self.progressBar.setStyleSheet("QProgressBar {\n"
"    border: 2px solid grey;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk {\n"
"    background-color: #05B8CC;\n"
"    width: 10px;\n"
"    margin: 0.5px;\n"
"}")
        self.progressBar.setMinimum(-1000)
        self.progressBar.setMaximum(1000)
        self.progressBar.setProperty("value", 30)
        self.progressBar.setObjectName("progressBar")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.progressBar)
        self.labelClass_2 = QtWidgets.QLabel(self.groupBox_2)
        self.labelClass_2.setObjectName("labelClass_2")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.labelClass_2)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.horizontalLayout.addWidget(self.frame)
        self.groupBoxCategories = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBoxCategories.sizePolicy().hasHeightForWidth())
        self.groupBoxCategories.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupBoxCategories.setFont(font)
        self.groupBoxCategories.setObjectName("groupBoxCategories")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBoxCategories)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout.addWidget(self.groupBoxCategories)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 985, 32))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionLogout = QtWidgets.QAction(MainWindow)
        self.actionLogout.setObjectName("actionLogout")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menu.addAction(self.actionLogout)
        self.menu.addSeparator()
        self.menu.addAction(self.actionExit)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Тест по биологии"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Данные ученика:"))
        self.labelSurname.setText(_translate("MainWindow", "Фамилия:"))
        self.lineEditSurname.setText(_translate("MainWindow", "Петров"))
        self.lineEditName.setText(_translate("MainWindow", "Петр"))
        self.labelName.setText(_translate("MainWindow", "Имя:"))
        self.lineEditClass.setText(_translate("MainWindow", "5 \"A\""))
        self.labelClass.setText(_translate("MainWindow", "Класс:"))
        self.progressBar.setFormat(_translate("MainWindow", "%v"))
        self.labelClass_2.setText(_translate("MainWindow", "Рейтинг:"))
        self.groupBoxCategories.setTitle(_translate("MainWindow", "Выберите тему:"))
        self.menu.setTitle(_translate("MainWindow", "&Файл"))
        self.actionLogout.setText(_translate("MainWindow", "Сменить пользователя"))
        self.actionExit.setText(_translate("MainWindow", "&Выход"))
import biology_test.main_rc
