from gui import guiMain
from database import Database
from plotter import Plotter
import sys


db = Database()

fiels = [
    'data/atp_matches_2000.csv',
    'data/atp_matches_2001.csv',
    'data/atp_matches_2002.csv',
    'data/atp_matches_2003.csv',
    'data/atp_matches_2004.csv',
    'data/atp_matches_2005.csv',
    'data/atp_matches_2006.csv',
    'data/atp_matches_2007.csv',
    'data/atp_matches_2008.csv',
    'data/atp_matches_2009.csv',
    'data/atp_matches_2010.csv',
    'data/atp_matches_2011.csv',
    'data/atp_matches_2012.csv',
    'data/atp_matches_2013.csv',
    'data/atp_matches_2014.csv',
    'data/atp_matches_2015.csv',
    'data/atp_matches_2016.csv',
    'data/atp_matches_2017.csv',
]
db.from_csv(fiels)

plt = Plotter(db)

guiMain(sys.argv, database=db, plotter=plt)
