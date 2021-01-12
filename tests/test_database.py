from database import (
    Database, InvalidIndexName, InvalidFilePath,
    MissingNameError, NegativeRange
)
import pandas as pd
import numpy as np
import pytest

FILES = [
    'archive/atp_matches_2000.csv',
    'archive/atp_matches_2001.csv',
    'archive/atp_matches_2002.csv',
    'archive/atp_matches_2003.csv',
    'archive/atp_matches_2004.csv',
    'archive/atp_matches_2005.csv',
    'archive/atp_matches_2006.csv',
    'archive/atp_matches_2007.csv',
    'archive/atp_matches_2008.csv',
    'archive/atp_matches_2009.csv',
    'archive/atp_matches_2010.csv',
    'archive/atp_matches_2011.csv',
    'archive/atp_matches_2012.csv',
    'archive/atp_matches_2013.csv',
    'archive/atp_matches_2014.csv',
    'archive/atp_matches_2015.csv',
    'archive/atp_matches_2016.csv',
    'archive/atp_matches_2017.csv',
]


def test_get_surface_typical():
    db = Database()
    db.df = pd.DataFrame(
        {"tourney_name": ['Wimbledon', 'Us Open', 'Kitzbuhel'],
            "surface": ['INNA', 'Hard', 'Clay']})
    assert db.get_surface('Wimbledon') == "INNA"


def test_get_surface_invalid_tournay():
    db = Database()
    db.df = pd.DataFrame(
        {"tourney_name": ['Wimbledon', 'Us Open', 'Kitzbuhel'],
            "surface": ['INNA', 'Hard', 'Clay']})
    with pytest.raises(InvalidIndexName):
        db.get_surface('INVALID') == "INNA"


def test_check_nan_change():
    db = Database()
    assert db.check_nan(np.nan) == 0


def test_check_nan_pass():
    db = Database()
    assert db.check_nan(14) == 14


def test_impot():
    db = Database()
    db.from_csv(FILES)
    assert db.get_surface('Wimbledon') == "Grass"


def test_impot_invalid_path():
    db = Database()
    with pytest.raises(InvalidFilePath):
        db.from_csv(["FILES.csv", "Invalid.sdfa"])


def test_get_all_elements_typical():
    db = Database()
    db.df = pd.DataFrame(
        {"tourney_name": ['Wimbledon', 'Us Open', 'Kitzbuhel'],
            "surface": ['INNA', 'Hard', 'Clay']})
    data = ['Kitzbuhel', 'Us Open', 'Wimbledon']
    assert db.get_all_elements('tourney_name') == data


def test_get_all_elements_no_data():
    db = Database()
    db.df = pd.DataFrame(
        {"tourney_name": ['Wimbledon', 'Us Open', 'Kitzbuhel'],
            "surface": ['INNA', 'Hard', 'Clay']})
    data = ['Kitzbuhel', 'Us Open', 'Wimbledon']
    with pytest.raises(InvalidIndexName):
        db.get_all_elements('INVALID') == data


def test_get_second_players_typical():
    db = Database()
    db.df = pd.DataFrame(
        {"winner_name": ['Tomas', 'John', 'Tomas'],
            "loser_name": ['Adam', 'Bob', 'Chris'],
            "tourney_name": ['Wimbledon', 'Us Open', 'Kitzbuhel'],
            "surface": ['INNA', 'Hard', 'Clay']})
    data = ['Adam', 'Chris']
    assert db.get_second_players('Tomas') == data


def test_get_second_players_no_data():
    db = Database()
    db.df = pd.DataFrame(
        {"winner_name": ['Tomas', 'John', 'Tomas'],
            "loser_name": ['Adam', 'Bob', 'Chris'],
            "tourney_name": ['Wimbledon', 'Us Open', 'Kitzbuhel'],
            "surface": ['INNA', 'Hard', 'Clay']})
    data = ['Adam', 'Chris']
    with pytest.raises(MissingNameError):
        db.get_second_players('INVALID NAME') == data


def test_get_tournaments_typical():
    db = Database()
    db.df = pd.DataFrame(
        {"winner_name": ['Tomas', 'John', 'Tomas'],
            "loser_name": ['Adam', 'Bob', 'Chris'],
            "tourney_name": ['Wimbledon', 'Us Open', 'Kitzbuhel'],
            "surface": ['INNA', 'Hard', 'Clay']})
    assert db.get_tournaments('Tomas', "Adam") == ['Wimbledon']


def test_get_tournaments_no_data():
    db = Database()
    db.df = pd.DataFrame(
        {"winner_name": ['Tomas', 'John', 'Tomas'],
            "loser_name": ['Adam', 'Bob', 'Chris'],
            "tourney_name": ['Wimbledon', 'Us Open', 'Kitzbuhel'],
            "surface": ['INNA', 'Hard', 'Clay']})
    with pytest.raises(MissingNameError):
        db.get_tournaments('INVALID NAME', "Adam") == 'Wimbledon'


def test_get_indexes_typical():
    db = Database()
    db.df = pd.DataFrame(
        {"winner_name": ['Tomas', 'John', 'Tomas'],
            "loser_name": ['Adam', 'Bob', 'Chris'],
            "tourney_name": ['Wimbledon', 'Us Open', 'Kitzbuhel'],
            "surface": ['INNA', 'Hard', 'Clay']})
    db.values = {
        "Wins": ["One", "Two"],
        "Losses": ["Three", "Four"]
    }
    assert db.get_indexes() == db.values


def test_get_data_frame_with_date_negative_range():
    db = Database()
    db.df = pd.DataFrame(
        {"winner_name": ['Tomas', 'John', 'Tomas'],
            "loser_name": ['Adam', 'Bob', 'Chris'],
            "tourney_name": ['Wimbledon', 'Us Open', 'Kitzbuhel'],
            "tourney_date": [20000000, 30000000, 40000000],
            "surface": ['INNA', 'Hard', 'Clay']})
    with pytest.raises(NegativeRange):
        db.get_data_frame_with_date("20200000", "19990101")


def test_get_winratio_columns_local():
    db = Database()
    db.df = pd.DataFrame(
        {"winner_name": ['Tomas', 'John', 'Tomas'],
            "loser_name": ['Adam', 'Bob', 'Chris'],
            "tourney_name": ['Wimbledon', 'Us Open', 'Kitzbuhel'],
            "tourney_date": [20000000, 30000000, 40000000],
            "surface": ['INNA', 'Hard', 'Clay']})
    db.values = {
        "Wins": ["winner_name", "loser_name", "local"],
        "Losses": ["winner_name", "loser_name", "local"]
    }
    date = (1, 0, 0, 1)
    assert db.get_winratio_columns(
            "Tomas", "Adam", "Wimbledon",
            ["winner_name", "loser_name", "local"],
            "19990101", "20000101"
        ) == date


def test_get_winratio_columns_global():
    db = Database()
    db.df = pd.DataFrame(
        {"winner_name": ['Tomas', 'John', 'Tomas'],
            "loser_name": ['Adam', 'Bob', 'Chris'],
            "tourney_name": ['Wimbledon', 'Us Open', 'Kitzbuhel'],
            "tourney_date": [20000000, 30000000, 40000000],
            "surface": ['INNA', 'Hard', 'Clay']})
    db.values = {
        "Wins": ["winner_name", "loser_name", "local"],
        "Losses": ["winner_name", "loser_name", "local"]
    }
    date = (2, 0, 0, 1)
    assert db.get_winratio_columns(
            "Tomas", "Adam", "Wimbledon",
            ["winner_name", "loser_name", "global"],
            "19990101", "50000101"
        ) == date


def test_get_winratio_columns_more_params():
    db = Database()
    db.df = pd.DataFrame(
        {"winner_name": ['Tomas', 'John', 'Tomas'],
            "loser_name": ['Adam', 'Bob', 'Chris'],
            "tourney_name": ['Wimbledon', 'Us Open', 'Kitzbuhel'],
            "tourney_level": ['G', 'G', 'M'],
            "tourney_date": [20000000, 30000000, 40000000],
            "surface": ['INNA', 'Hard', 'Clay']})
    db.values = {
        "Wins": ["winner_name", "loser_name", "local"],
        "Losses": ["winner_name", "loser_name", "local"],
        "LVL": ['winner_name', 'loser_name', 'general', 'tourney_level', 'G']
    }
    date = (1, 0, 0, 1)
    assert db.get_winratio_columns(
            "Tomas", "Adam", "Wimbledon",
            ['winner_name', 'loser_name', 'general', 'tourney_level', 'G'],
            "19990101", "50000101"
        ) == date


def test_get_data_frame_negative_range():
    db = Database()
    db.df = pd.DataFrame(
        {"winner_name": ['Tomas', 'John', 'Tomas'],
            "loser_name": ['Adam', 'Bob', 'Chris'],
            "tourney_name": ['Wimbledon', 'Us Open', 'Kitzbuhel'],
            "surface": ['INNA', 'Hard', 'Clay']})
    with pytest.raises(NegativeRange):
        db.get_data_frame(
            "Adam", "Bob", "Us Open", "20200000", "19990101")


def test_get_sum_in_columns_local():
    db = Database()
    db.df = pd.DataFrame(
        {"winner_name": ['Tomas', 'John', 'Tomas'],
            "loser_name": ['Adam', 'Bob', 'Chris'],
            "tourney_name": ['Wimbledon', 'Us Open', 'Kitzbuhel'],
            "w_ace": [5, 1, 6],
            "l_ace": [3, 2, 1],
            "tourney_date": [20000000, 30000000, 40000000],
            "surface": ['INNA', 'Hard', 'Clay']})
    db.values = {
        "Wins": ["winner_name", "loser_name", "local"],
        "Losses": ["winner_name", "loser_name", "local"],
        "Aces": ['w_ace', 'l_ace', 'local']
    }
    date = (5.0, 3.0)
    assert db.get_sum_in_columns(
            "Tomas", "Adam", "Wimbledon",
            ['w_ace', 'l_ace', 'local'],
            "19990101", "20000101"
        ) == date


def test_get_sum_in_columns_global():
    db = Database()
    db.df = pd.DataFrame(
        {"winner_name": ['Tomas', 'John', 'Tomas'],
            "loser_name": ['Adam', 'Bob', 'Chris'],
            "tourney_name": ['Wimbledon', 'Us Open', 'Kitzbuhel'],
            "w_ace": [5, 1, 6],
            "l_ace": [3, 2, 1],
            "tourney_date": [20000000, 30000000, 40000000],
            "surface": ['INNA', 'Hard', 'Clay']})
    db.values = {
        "Wins": ["winner_name", "loser_name", "local"],
        "Losses": ["winner_name", "loser_name", "local"]
    }
    date = (11.0, 3.0)
    assert db.get_sum_in_columns(
            "Tomas", "Adam", "Wimbledon",
            ['w_ace', 'l_ace', 'global'],
            "19990101", "50000101"
        ) == date


def test_get_best_in_columns_local():
    db = Database()
    db.df = pd.DataFrame(
        {"winner_name": ['Tomas', 'John', 'Tomas'],
            "loser_name": ['Adam', 'Bob', 'Chris'],
            "tourney_name": ['Wimbledon', 'Us Open', 'Kitzbuhel'],
            "w_ace": [5, 1, 6],
            "l_ace": [3, 2, 1],
            "tourney_date": [20000000, 30000000, 40000000],
            "surface": ['INNA', 'Hard', 'Clay']})
    db.values = {
        "Wins": ["winner_name", "loser_name", "local"],
        "Losses": ["winner_name", "loser_name", "local"],
        "Aces": ['w_ace', 'l_ace', 'local']
    }
    date = (5.0, 3.0)
    assert db.get_best_in_columns(
            "Tomas", "Adam", "Wimbledon",
            ['w_ace', 'l_ace', 'local'],
            "19990101", "20000101"
        ) == date


def test_get_best_in_columns_global():
    db = Database()
    db.df = pd.DataFrame(
        {"winner_name": ['Tomas', 'John', 'Tomas'],
            "loser_name": ['Adam', 'Bob', 'Chris'],
            "tourney_name": ['Wimbledon', 'Us Open', 'Kitzbuhel'],
            "w_ace": [5, 1, 6],
            "l_ace": [3, 2, 1],
            "tourney_date": [20000000, 30000000, 40000000],
            "surface": ['INNA', 'Hard', 'Clay']})
    db.values = {
        "Wins": ["winner_name", "loser_name", "local"],
        "Losses": ["winner_name", "loser_name", "local"]
    }
    date = (6, 3)
    assert db.get_best_in_columns(
            "Tomas", "Adam", "Wimbledon",
            ['w_ace', 'l_ace', 'global'],
            "19990101", "50000101"
        ) == date
