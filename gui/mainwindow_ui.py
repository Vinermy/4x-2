# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.3
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
    QLabel, QMainWindow, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QTabWidget, QVBoxLayout,
    QWidget)

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
        self.grbTopMenu.setMinimumSize(QSize(0, 80))
        self.grbTopMenu.setMaximumSize(QSize(16777215, 70))
        self.horizontalLayout_2 = QHBoxLayout(self.grbTopMenu)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, 9, 9)
        self.horizontalSpacer = QSpacerItem(1807, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.groupBox = QGroupBox(self.grbTopMenu)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.btnSave = QPushButton(self.groupBox)
        self.btnSave.setObjectName(u"btnSave")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btnSave.sizePolicy().hasHeightForWidth())
        self.btnSave.setSizePolicy(sizePolicy2)
        self.btnSave.setMinimumSize(QSize(30, 30))
        icon = QIcon()
        icon.addFile(u"./gui/icons/floppy-disk-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btnSave.setIcon(icon)
        self.btnSave.setIconSize(QSize(20, 20))

        self.horizontalLayout_3.addWidget(self.btnSave)

        self.btnLoad = QPushButton(self.groupBox)
        self.btnLoad.setObjectName(u"btnLoad")
        sizePolicy2.setHeightForWidth(self.btnLoad.sizePolicy().hasHeightForWidth())
        self.btnLoad.setSizePolicy(sizePolicy2)
        self.btnLoad.setMinimumSize(QSize(30, 30))
        icon1 = QIcon()
        icon1.addFile(u"./gui/icons/upload-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btnLoad.setIcon(icon1)
        self.btnLoad.setIconSize(QSize(20, 20))

        self.horizontalLayout_3.addWidget(self.btnLoad)

        self.btnNewGame = QPushButton(self.groupBox)
        self.btnNewGame.setObjectName(u"btnNewGame")
        self.btnNewGame.setMinimumSize(QSize(30, 30))
        icon2 = QIcon()
        icon2.addFile(u"./gui/icons/square-plus-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btnNewGame.setIcon(icon2)
        self.btnNewGame.setIconSize(QSize(20, 20))

        self.horizontalLayout_3.addWidget(self.btnNewGame)


        self.horizontalLayout_2.addWidget(self.groupBox)


        self.verticalLayout.addWidget(self.grbTopMenu)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.scrSideMenu = QScrollArea(self.centralwidget)
        self.scrSideMenu.setObjectName(u"scrSideMenu")
        self.scrSideMenu.setMinimumSize(QSize(300, 0))
        self.scrSideMenu.setMaximumSize(QSize(300, 16777215))
        self.scrSideMenu.setFrameShape(QFrame.Panel)
        self.scrSideMenu.setWidgetResizable(True)
        self.scrSideMenu.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 298, 972))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.vloSideMenu = QVBoxLayout()
        self.vloSideMenu.setSpacing(6)
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
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Save / Load", None))
        self.btnSave.setText("")
        self.btnLoad.setText("")
        self.btnNewGame.setText("")
        self.lblDisplay.setText("")
    # retranslateUi

