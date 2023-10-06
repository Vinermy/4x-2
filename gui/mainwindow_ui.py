# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGroupBox, QHBoxLayout,
    QLabel, QMainWindow, QScrollArea, QSizePolicy,
    QTabWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1920, 1080)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.grbTopMenu = QGroupBox(self.centralwidget)
        self.grbTopMenu.setObjectName(u"grbTopMenu")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.grbTopMenu.sizePolicy().hasHeightForWidth())
        self.grbTopMenu.setSizePolicy(sizePolicy1)
        self.grbTopMenu.setMinimumSize(QSize(0, 60))
        self.grbTopMenu.setMaximumSize(QSize(16777215, 60))

        self.verticalLayout.addWidget(self.grbTopMenu)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.scrSideMenu = QScrollArea(self.centralwidget)
        self.scrSideMenu.setObjectName(u"scrSideMenu")
        self.scrSideMenu.setMinimumSize(QSize(300, 0))
        self.scrSideMenu.setMaximumSize(QSize(300, 16777215))
        self.scrSideMenu.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 298, 992))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.vloSideMenu = QVBoxLayout()
        self.vloSideMenu.setObjectName(u"vloSideMenu")

        self.verticalLayout_3.addLayout(self.vloSideMenu)

        self.scrSideMenu.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout.addWidget(self.scrSideMenu)

        self.lblDisplay = QLabel(self.centralwidget)
        self.lblDisplay.setObjectName(u"lblDisplay")
        self.lblDisplay.setFrameShape(QFrame.NoFrame)

        self.horizontalLayout.addWidget(self.lblDisplay)


        self.verticalLayout.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.grbTopMenu.setTitle(QCoreApplication.translate("MainWindow", u"Game controls and menus", None))
        self.lblDisplay.setText("")
    # retranslateUi

