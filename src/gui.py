from PySide2.QtWidgets import (
    QApplication, QMainWindow, QListWidgetItem
)
from PySide2.QtGui import QPixmap
from ui_statistics import Ui_MainWindow


class NegativeRange(Exception):
    pass


class PlayersWindow(QMainWindow):
    """
    PlayersWindow class is responsible
    for presenting the user a graphical interface,
    retrieving the necessary values and parameters from him
    to display the graph to the user.
    """
    def __init__(self, database, plotter, parent=None):
        """Initializes a PlayersWindow"""
        super().__init__(parent)
        self.database = database
        self.plotter = plotter
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.stack.setCurrentIndex(0)
        self.tourney_clicked = False
        self.only_best = False
        self._setupLists()

    def _setupLists(self):
        """
        the function sets the lists and checks
        if the user has selected any item
        """
        players = self.database.get_all_elements(['winner_name', 'loser_name'])
        self.player_1 = self._setupList(players, self.ui.player_1_list)
        self.ui.player_1_list.itemClicked.connect(self._selectPlayer1)
        self.ui.player_2_list.itemClicked.connect(self._selectPlayer2)
        self.ui.tournamnet_list.itemClicked.connect(self._selectTourney)
        self.ui.only_best.toggled.connect(self.onClicked)
        self.ui.generate_plot.clicked.connect(self._generatePlot)

    def onClicked(self):
        """The function checks the logical value of the toggle"""
        radio_button = self.sender()
        if radio_button.isChecked():
            self.only_best = True
        else:
            self.only_best = False

    def checkDate(self):
        """Returns a date range, if valid"""
        min_date = self.ui.min_date_select
        max_date = self.ui.max_date_select
        if min_date.date() > max_date.date():
            raise NegativeRange()
        min_date = min_date.date().toString("yyyyMMdd")
        max_date = max_date.date().toString("yyyyMMdd")
        return min_date, max_date

    def _generatePlot(self, item):
        """The function checks the conditions and displays the graph"""
        try:
            min_date, max_date = self.checkDate()
            selected_values = {}
            indexes = self.database.get_indexes()
            value_item = self.ui.values.selectedItems()
            for value in value_item:
                if value.name in indexes:
                    selected_values[value.name] = indexes[value.name]

            image_data = self.plotter.get_plot(
                self.player_1.name, self.player_2.name,
                self.tourney.name, selected_values, self.only_best,
                min_date, max_date)
            pixmap = QPixmap()
            if pixmap.loadFromData(image_data):
                self.ui.plot.setPixmap(pixmap)
        except NegativeRange:
            self.ui.plot.setText("The date range selected cannot be negative")

    def _selectPlayer1(self, item):
        """
        The function takes the first selected item
        and generates a second list of items
        """
        self.tourney_clicked = False
        self.player_1 = item
        self.ui.tournamnet_list.clear()
        self.ui.player_2_list.clear()
        self.ui.information.setText("Select Second Player")
        player_2_list = self.database.get_second_players(self.player_1.name)
        self.player_2 = self._setupList(player_2_list, self.ui.player_2_list)
        self._checkClicked()

    def _selectPlayer2(self, item):
        """
        The function takes the second selected item
        and generates a third list of items
        """
        self.tourney_clicked = False
        self.player_2 = item
        self.ui.tournamnet_list.clear()
        self.ui.information.setText("Select Tournament")
        tourney = self.database.get_tournaments(
            self.player_1.name, self.player_2.name)
        self.tourney = self._setupList(tourney, self.ui.tournamnet_list)
        self._checkClicked()

    def _selectTourney(self, item):
        """The function takes the third element"""
        self.tourney_clicked = True
        self.tourney = item
        self._checkClicked()

    def _checkClicked(self):
        """The function checks if three elements have been selected"""
        if self.tourney_clicked:
            self.ui.stack.setCurrentIndex(1)
            values = self.database.get_indexes()
            self.ui.values.clear()
            for value in values:
                value_item = QListWidgetItem(value)
                value_item.name = value
                self.ui.values.addItem(value_item)
        else:
            self.ui.stack.setCurrentIndex(0)
            self.ui.plot.clear()

    def _setupList(self, elements, widget_list):
        """function adds items to the list"""
        for element in elements:
            item = QListWidgetItem(element)
            item.name = element
            widget_list.addItem(item)
        return item


def guiMain(args, database, plotter):
    """Main function that makes up the Player Window class"""
    app = QApplication(args)
    window = PlayersWindow(database, plotter)
    window.show()
    return app.exec_()
