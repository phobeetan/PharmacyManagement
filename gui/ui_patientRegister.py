# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'patientRegister.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QDateEdit, QFormLayout, QLabel,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.formLayoutWidget = QWidget(self.centralwidget)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(20, 10, 751, 251))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.birthdateLabel = QLabel(self.formLayoutWidget)
        self.birthdateLabel.setObjectName(u"birthdateLabel")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.birthdateLabel)

        self.birthDateEdit = QDateEdit(self.formLayoutWidget)
        self.birthDateEdit.setObjectName(u"birthDateEdit")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.birthDateEdit)

        self.firstNameEdit = QLineEdit(self.formLayoutWidget)
        self.firstNameEdit.setObjectName(u"firstNameEdit")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.SpanningRole, self.firstNameEdit)

        self.emailEdit = QLineEdit(self.formLayoutWidget)
        self.emailEdit.setObjectName(u"emailEdit")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.SpanningRole, self.emailEdit)

        self.lastNameEdit = QLineEdit(self.formLayoutWidget)
        self.lastNameEdit.setObjectName(u"lastNameEdit")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.SpanningRole, self.lastNameEdit)

        self.passwordEdit = QLineEdit(self.formLayoutWidget)
        self.passwordEdit.setObjectName(u"passwordEdit")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.SpanningRole, self.passwordEdit)

        self.pharmacisRegistertSubmit = QPushButton(self.formLayoutWidget)
        self.pharmacisRegistertSubmit.setObjectName(u"pharmacisRegistertSubmit")

        self.formLayout.setWidget(7, QFormLayout.ItemRole.SpanningRole, self.pharmacisRegistertSubmit)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.formLayout.setItem(1, QFormLayout.ItemRole.FieldRole, self.verticalSpacer)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 25))
        self.menuRegister = QMenu(self.menubar)
        self.menuRegister.setObjectName(u"menuRegister")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuRegister.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.birthdateLabel.setText(QCoreApplication.translate("MainWindow", u"Date of Birth", None))
        self.firstNameEdit.setText(QCoreApplication.translate("MainWindow", u"First Name", None))
        self.emailEdit.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.lastNameEdit.setText(QCoreApplication.translate("MainWindow", u"Last Name", None))
        self.passwordEdit.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.pharmacisRegistertSubmit.setText(QCoreApplication.translate("MainWindow", u"Register as Pharmacist", None))
        self.menuRegister.setTitle(QCoreApplication.translate("MainWindow", u"Register", None))
    # retranslateUi

