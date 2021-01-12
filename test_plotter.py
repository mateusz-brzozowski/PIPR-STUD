from plotter import Plotter, MissingDataError
from database import Database
import numpy as np
import pytest


def test_get_description_divine_by_zero():
    db = Database
    plt = Plotter(db)
    string = "Lack of data"
    plt.get_description(0, 0) == string


def test_get_description_nan():
    db = Database
    plt = Plotter(db)
    with pytest.raises(MissingDataError):
        plt.get_description(np.nan, 0)


def test_get_description_typical():
    db = Database
    plt = Plotter(db)
    string = "1/0 (100%)"
    plt.get_description(1, 0) == string
