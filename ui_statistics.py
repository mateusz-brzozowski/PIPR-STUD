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
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
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
        self.gridLayout_2 = QGridLayout(self.page_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.plot = QLabel(self.page_2)
        self.plot.setObjectName(u"plot")
        self.plot.setScaledContents(True)
        self.plot.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.plot, 5, 0, 1, 1)

        self.min_date_select = QDateEdit(self.page_2)
        self.min_date_select.setObjectName(u"min_date_select")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.min_date_select.sizePolicy().hasHeightForWidth())
        self.min_date_select.setSizePolicy(sizePolicy2)
        self.min_date_select.setAlignment(Qt.AlignCenter)
        self.min_date_select.setMaximumDateTime(QDateTime(QDate(2017, 12, 31), QTime(23, 59, 59)))
        self.min_date_select.setMinimumDateTime(QDateTime(QDate(2000, 1, 1), QTime(0, 0, 0)))
        self.min_date_select.setCurrentSection(QDateTimeEdit.YearSection)
        self.min_date_select.setCalendarPopup(False)

        self.gridLayout_2.addWidget(self.min_date_select, 3, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 301, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 6, 1, 1, 1)

        self.only_best = QRadioButton(self.page_2)
        self.only_best.setObjectName(u"only_best")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.only_best.sizePolicy().hasHeightForWidth())
        self.only_best.setSizePolicy(sizePolicy3)

        self.gridLayout_2.addWidget(self.only_best, 2, 0, 2, 1)

        self.min_data_text = QLabel(self.page_2)
        self.min_data_text.setObjectName(u"min_data_text")
        sizePolicy2.setHeightForWidth(self.min_data_text.sizePolicy().hasHeightForWidth())
        self.min_data_text.setSizePolicy(sizePolicy2)
        self.min_data_text.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.min_data_text, 2, 1, 1, 1)

        self.max_data_text = QLabel(self.page_2)
        self.max_data_text.setObjectName(u"max_data_text")
        sizePolicy2.setHeightForWidth(self.max_data_text.sizePolicy().hasHeightForWidth())
        self.max_data_text.setSizePolicy(sizePolicy2)
        self.max_data_text.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.max_data_text, 2, 2, 1, 1)

        self.values = QListWidget(self.page_2)
        self.values.setObjectName(u"values")
        sizePolicy.setHeightForWidth(self.values.sizePolicy().hasHeightForWidth())
        self.values.setSizePolicy(sizePolicy)
        self.values.setEditTriggers(QAbstractItemView.DoubleClicked|QAbstractItemView.EditKeyPressed)
        self.values.setSelectionMode(QAbstractItemView.MultiSelection)

        self.gridLayout_2.addWidget(self.values, 1, 0, 1, 3)

        self.generate_plot = QPushButton(self.page_2)
        self.generate_plot.setObjectName(u"generate_plot")

        self.gridLayout_2.addWidget(self.generate_plot, 4, 0, 1, 3)

        self.information_2 = QLabel(self.page_2)
        self.information_2.setObjectName(u"information_2")
        self.information_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.information_2, 0, 0, 1, 3)

        self.max_date_select = QDateEdit(self.page_2)
        self.max_date_select.setObjectName(u"max_date_select")
        sizePolicy2.setHeightForWidth(self.max_date_select.sizePolicy().hasHeightForWidth())
        self.max_date_select.setSizePolicy(sizePolicy2)
        self.max_date_select.setAlignment(Qt.AlignCenter)
        self.max_date_select.setDateTime(QDateTime(QDate(2000, 9, 14), QTime(0, 0, 0)))
        self.max_date_select.setMaximumDateTime(QDateTime(QDate(2017, 12, 31), QTime(23, 59, 59)))
        self.max_date_select.setMinimumDateTime(QDateTime(QDate(2000, 1, 1), QTime(0, 0, 0)))
        self.max_date_select.setCurrentSection(QDateTimeEdit.YearSection)
        self.max_date_select.setCalendarPopup(False)

        self.gridLayout_2.addWidget(self.max_date_select, 3, 2, 1, 1)

        self.stack.addWidget(self.page_2)
        self.splitter.addWidget(self.stack)

        self.gridLayout_3.addWidget(self.splitter, 0, 0, 1, 1)

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
        self.plot.setText("")
#if QT_CONFIG(tooltip)
        self.min_date_select.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.min_date_select.setDisplayFormat(QCoreApplication.translate("MainWindow", u"yyyy", None))
        self.only_best.setText(QCoreApplication.translate("MainWindow", u"The Best Values", None))
#if QT_CONFIG(tooltip)
        self.min_data_text.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.min_data_text.setText(QCoreApplication.translate("MainWindow", u"Minimum Date", None))
        self.max_data_text.setText(QCoreApplication.translate("MainWindow", u"Maximum Date", None))
        self.generate_plot.setText(QCoreApplication.translate("MainWindow", u"Generate a chart", None))
        self.information_2.setText(QCoreApplication.translate("MainWindow", u"Select the values you want to compare", None))
        self.max_date_select.setDisplayFormat(QCoreApplication.translate("MainWindow", u"yyyy", None))
    # retranslateUi

