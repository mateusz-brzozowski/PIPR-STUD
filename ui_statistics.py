# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'statistics.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1005, 713)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.layoutWidget = QWidget(self.splitter)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.player_1_name = QLabel(self.layoutWidget)
        self.player_1_name.setObjectName(u"player_1_name")
        self.player_1_name.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.player_1_name)

        self.player_1_list = QListWidget(self.layoutWidget)
        self.player_1_list.setObjectName(u"player_1_list")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.player_1_list.sizePolicy().hasHeightForWidth())
        self.player_1_list.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.player_1_list)

        self.player_2_name = QLabel(self.layoutWidget)
        self.player_2_name.setObjectName(u"player_2_name")
        self.player_2_name.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.player_2_name)

        self.player_2_list = QListWidget(self.layoutWidget)
        self.player_2_list.setObjectName(u"player_2_list")
        sizePolicy.setHeightForWidth(self.player_2_list.sizePolicy().hasHeightForWidth())
        self.player_2_list.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.player_2_list)

        self.tournament_name = QLabel(self.layoutWidget)
        self.tournament_name.setObjectName(u"tournament_name")
        self.tournament_name.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.tournament_name)

        self.tournamnet_list = QListWidget(self.layoutWidget)
        self.tournamnet_list.setObjectName(u"tournamnet_list")
        sizePolicy.setHeightForWidth(self.tournamnet_list.sizePolicy().hasHeightForWidth())
        self.tournamnet_list.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.tournamnet_list)

        self.splitter.addWidget(self.layoutWidget)
        self.stack = QStackedWidget(self.splitter)
        self.stack.setObjectName(u"stack")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.stack.sizePolicy().hasHeightForWidth())
        self.stack.setSizePolicy(sizePolicy1)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout = QGridLayout(self.page)
        self.gridLayout.setObjectName(u"gridLayout")
        self.information = QLabel(self.page)
        self.information.setObjectName(u"information")
        self.information.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.information, 0, 0, 1, 1)

        self.stack.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_2 = QVBoxLayout(self.page_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.information_2 = QLabel(self.page_2)
        self.information_2.setObjectName(u"information_2")
        self.information_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.information_2)

        self.values = QListWidget(self.page_2)
        self.values.setObjectName(u"values")
        sizePolicy.setHeightForWidth(self.values.sizePolicy().hasHeightForWidth())
        self.values.setSizePolicy(sizePolicy)
        self.values.setEditTriggers(QAbstractItemView.DoubleClicked|QAbstractItemView.EditKeyPressed)
        self.values.setSelectionMode(QAbstractItemView.MultiSelection)

        self.verticalLayout_2.addWidget(self.values)

        self.generate_plot = QPushButton(self.page_2)
        self.generate_plot.setObjectName(u"generate_plot")

        self.verticalLayout_2.addWidget(self.generate_plot)

        self.plot = QLabel(self.page_2)
        self.plot.setObjectName(u"plot")
        self.plot.setScaledContents(True)
        self.plot.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.plot)

        self.verticalSpacer = QSpacerItem(20, 301, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.stack.addWidget(self.page_2)
        self.splitter.addWidget(self.stack)

        self.horizontalLayout.addWidget(self.splitter)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1005, 20))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stack.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.player_1_name.setText(QCoreApplication.translate("MainWindow", u"First Player", None))
        self.player_2_name.setText(QCoreApplication.translate("MainWindow", u"Second Player", None))
        self.tournament_name.setText(QCoreApplication.translate("MainWindow", u"Tournament", None))
        self.information.setText(QCoreApplication.translate("MainWindow", u"Choose First Player", None))
        self.information_2.setText(QCoreApplication.translate("MainWindow", u"Select the values you want to compare", None))
        self.generate_plot.setText(QCoreApplication.translate("MainWindow", u"Generate a chart", None))
        self.plot.setText("")
    # retranslateUi

