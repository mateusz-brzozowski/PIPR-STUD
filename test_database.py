from database import Database
import pandas as pd

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


def test_impot():
    db = Database()
    db.from_csv(FILES)
    assert db.get_surface('Wimbledon') == "Grass"
