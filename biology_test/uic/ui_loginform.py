# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'biology_test/ui/LoginForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_loginForm(object):
    def setupUi(self, loginForm):
        loginForm.setObjectName("loginForm")
        loginForm.resize(500, 271)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(loginForm.sizePolicy().hasHeightForWidth())
        loginForm.setSizePolicy(sizePolicy)
        loginForm.setMaximumSize(QtCore.QSize(500, 271))
        font = QtGui.QFont()
        font.setPointSize(14)
        loginForm.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/static/images/main.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        loginForm.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(loginForm)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(loginForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(128, 128))
        self.frame.setMaximumSize(QtCore.QSize(128, 128))
        self.frame.setStyleSheet("border-image: url(:/images/static/images/avatar.png)  0 0 0 0 stretch stretch;\n"
"border: 3px solid black;\n"
"border-radius:  64")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setObjectName("frame")
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(loginForm)
        self.groupBox.setMinimumSize(QtCore.QSize(300, 0))
        self.groupBox.setObjectName("groupBox")
        self.formLayout_2 = QtWidgets.QFormLayout(self.groupBox)
        self.formLayout_2.setObjectName("formLayout_2")
        self.labelSurname = QtWidgets.QLabel(self.groupBox)
        self.labelSurname.setObjectName("labelSurname")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.labelSurname)
        self.lineEditSurname = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditSurname.setEnabled(True)
        self.lineEditSurname.setText("")
        self.lineEditSurname.setObjectName("lineEditSurname")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEditSurname)
        self.labelName = QtWidgets.QLabel(self.groupBox)
        self.labelName.setObjectName("labelName")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.labelName)
        self.lineEditName = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditName.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditName.sizePolicy().hasHeightForWidth())
        self.lineEditName.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEditName.setFont(font)
        self.lineEditName.setText("")
        self.lineEditName.setObjectName("lineEditName")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEditName)
        self.labelClass = QtWidgets.QLabel(self.groupBox)
        self.labelClass.setObjectName("labelClass")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.labelClass)
        self.comboBoxClass = QtWidgets.QComboBox(self.groupBox)
        self.comboBoxClass.setCurrentText("")
        self.comboBoxClass.setObjectName("comboBoxClass")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.comboBoxClass)
        self.labelPassword = QtWidgets.QLabel(self.groupBox)
        self.labelPassword.setObjectName("labelPassword")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.labelPassword)
        self.lineEditPassword = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditPassword.setEnabled(True)
        self.lineEditPassword.setText("")
        self.lineEditPassword.setObjectName("lineEditPassword")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEditPassword)
        self.gridLayout.addWidget(self.groupBox, 0, 1, 1, 1)
        self.loginButton = QtWidgets.QPushButton(loginForm)
        self.loginButton.setObjectName("loginButton")
        self.gridLayout.addWidget(self.loginButton, 1, 1, 1, 1)

        self.retranslateUi(loginForm)
        QtCore.QMetaObject.connectSlotsByName(loginForm)

    def retranslateUi(self, loginForm):
        _translate = QtCore.QCoreApplication.translate
        loginForm.setWindowTitle(_translate("loginForm", "Авторизация"))
        self.groupBox.setTitle(_translate("loginForm", "Данные ученика:"))
        self.labelSurname.setText(_translate("loginForm", "Фамилия:"))
        self.labelName.setText(_translate("loginForm", "Имя:"))
        self.labelClass.setText(_translate("loginForm", "Класс:"))
        self.labelPassword.setText(_translate("loginForm", "Пароль:"))
        self.loginButton.setText(_translate("loginForm", "Войти"))
import biology_test.main_rc
