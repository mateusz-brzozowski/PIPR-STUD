from PySide2.QtWidgets import (
    QApplication, QMainWindow, QListWidgetItem
)
from PySide2.QtGui import QPixmap
import sys
from ui_statistics import Ui_MainWindow
from database import (
    getAllElements, getIndexes, getSecondPlayers, getTournaments
)
from plotter import get_plot


class PlayersWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.stack.setCurrentIndex(0)
        self.tourney_clicked = False
        self._setupLists()

    def _setupLists(self):
        players = getAllElements(['winner_name', 'loser_name'])
        self.player_1 = self._setupList(players, self.ui.player_1_list)
        self.ui.player_1_list.itemClicked.connect(self._selectPlayer1)
        self.ui.player_2_list.itemClicked.connect(self._selectPlayer2)
        self.ui.tournamnet_list.itemClicked.connect(self._selectTourney)
        self.ui.generate_plot.clicked.connect(self._generatePlot)

    def _generatePlot(self, item):
        selected_values = {}
        indexes = getIndexes()
        value_item = self.ui.values.selectedItems()
        for value in value_item:
            if value.name in indexes:
                selected_values[value.name] = indexes[value.name]

        image_data = get_plot(
            self.player_1.name, self.player_2.name,
            self.tourney.name, selected_values)
        pixmap = QPixmap()
        if pixmap.loadFromData(image_data):
            self.ui.plot.setPixmap(pixmap)

    def _selectPlayer1(self, item):
        self.tourney_clicked = False
        self.player_1 = item
        self.ui.tournamnet_list.clear()
        self.ui.player_2_list.clear()
        self.ui.information.setText("Select Second Player")
        player_2_list = getSecondPlayers(self.player_1.name)
        self.player_2 = self._setupList(player_2_list, self.ui.player_2_list)
        self._checkClicked()

    def _selectPlayer2(self, item):
        self.tourney_clicked = False
        self.player_2 = item
        self.ui.tournamnet_list.clear()
        self.ui.information.setText("Select Tournament")
        tourney = getTournaments(self.player_1.name, self.player_2.name)
        self.tourney = self._setupList(tourney, self.ui.tournamnet_list)
        self._checkClicked()

    def _selectTourney(self, item):
        self.tourney_clicked = True
        self.tourney = item
        self._checkClicked()

    def _checkClicked(self):
        if self.tourney_clicked:
            self.ui.stack.setCurrentIndex(1)
            values = getIndexes()
            self.ui.values.clear()
            for value in values:
                value_item = QListWidgetItem(value)
                value_item.name = value
                self.ui.values.addItem(value_item)
        else:
            self.ui.stack.setCurrentIndex(0)
            self.ui.plot.clear()

    def _setupList(self, elements, widget_list):
        for element in elements:
            item = QListWidgetItem(element)
            item.name = element
            widget_list.addItem(item)
        return item


def guiMain(args):
    app = QApplication(args)
    window = PlayersWindow()
    window.show()
    return app.exec_()


if __name__ == "__main__":
    guiMain(sys.argv)
