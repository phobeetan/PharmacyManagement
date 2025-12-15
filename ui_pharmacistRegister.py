# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pharmacistRegister.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QGridLayout, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 6, 4, 1, 1)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.IDEdit = QLineEdit(self.centralwidget)
        self.IDEdit.setObjectName(u"IDEdit")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.SpanningRole, self.IDEdit)

        self.emailEdit = QLineEdit(self.centralwidget)
        self.emailEdit.setObjectName(u"emailEdit")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.SpanningRole, self.emailEdit)

        self.firstNameEdit = QLineEdit(self.centralwidget)
        self.firstNameEdit.setObjectName(u"firstNameEdit")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.SpanningRole, self.firstNameEdit)

        self.lastNameEdit = QLineEdit(self.centralwidget)
        self.lastNameEdit.setObjectName(u"lastNameEdit")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.SpanningRole, self.lastNameEdit)

        self.passwordEdit = QLineEdit(self.centralwidget)
        self.passwordEdit.setObjectName(u"passwordEdit")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.SpanningRole, self.passwordEdit)

        self.pharmacisRegistertSubmit = QPushButton(self.centralwidget)
        self.pharmacisRegistertSubmit.setObjectName(u"pharmacisRegistertSubmit")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.SpanningRole, self.pharmacisRegistertSubmit)


        self.gridLayout.addLayout(self.formLayout, 6, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 25))
        self.menuregistration = QMenu(self.menubar)
        self.menuregistration.setObjectName(u"menuregistration")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuregistration.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.IDEdit.setText(QCoreApplication.translate("MainWindow", u"pharmacistID", None))
        self.emailEdit.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.firstNameEdit.setText(QCoreApplication.translate("MainWindow", u"First Name", None))
        self.lastNameEdit.setText(QCoreApplication.translate("MainWindow", u"Last Name", None))
        self.passwordEdit.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.pharmacisRegistertSubmit.setText(QCoreApplication.translate("MainWindow", u"Register as Pharmacist", None))
        self.menuregistration.setTitle(QCoreApplication.translate("MainWindow", u"Registration", None))
    # retranslateUi

