from gui import guiMain
from database import Database
from plotter import Plotter
import sys


db = Database()

fiels = [
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
db.from_csv(fiels)

plt = Plotter(db)

guiMain(sys.argv, database=db, plotter=plt)
