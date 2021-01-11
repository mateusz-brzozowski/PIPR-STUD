import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
# %matplotlib inline
plt.style.use('fivethirtyeight')

# import os
# for dirname, _, filenames in os.walk('archive'):
#         for filename in filenames:
#             print(os.path.join(dirname, filename))

cols = [
    'tourney_id', # Id of Tournament
    'tourney_name', # Name of the Tournament
    'surface', # Surface of the Court (Hard, Clay, Grass)
    'draw_size', # Number of people in the tournament
    'tourney_level', # Level of the tournament (A=ATP Tour, D=Davis Cup, G=Grand Slam, M=Masters)
    'tourney_date', # Start date of tournament
    'match_num', # Match number
    'winner_id', # Id of winner
    'winner_seed', # Seed of winner
    'winner_entry', # How the winner entered the tournament
    'winner_name', # Name of winner
    'winner_hand', # Dominant hand of winner (L=Left, R=Right, U=Unknown?)
    'winner_ht', # Height in cm of winner
    'winner_ioc', # Country of winner
    'winner_age', # Age of winner
    'winner_rank', # Rank of winner
    'winner_rank_points', # Rank points of winner
    'loser_id',
    'loser_seed',
    'loser_entry',
    'loser_name',
    'loser_hand',
    'loser_ht',
    'loser_ioc',
    'loser_age',
    'loser_rank',
    'loser_rank_points',
    'score', # Score
    'best_of', # Best of X number of sets
    'round', # Round
    'minutes', # Match length in minutes
    'w_ace', # Number of aces for winner
    'w_df', # Number of double faults for winner
    'w_svpt', # Number of service points played by winner
    'w_1stIn', # Number of first serves in for winner
    'w_1stWon', # Number of first serve points won for winner
    'w_2ndWon', # Number of second serve points won for winner
    'w_SvGms', # Number of service games played by winner
    'w_bpSaved', # Number of break points saved by winner
    'w_bpFaced', # Number of break points faced by winner
    'l_ace',
    'l_df',
    'l_svpt',
    'l_1stIn',
    'l_1stWon',
    'l_2ndWon',
    'l_SvGms',
    'l_bpSaved',
    'l_bpFaced'
]

df = pd.concat([
    pd.read_csv('archive/atp_matches_2000.csv', usecols=cols),
    pd.read_csv('archive/atp_matches_2001.csv', usecols=cols),
    pd.read_csv('archive/atp_matches_2002.csv', usecols=cols),
    pd.read_csv('archive/atp_matches_2003.csv', usecols=cols),
    pd.read_csv('archive/atp_matches_2004.csv', usecols=cols),
    pd.read_csv('archive/atp_matches_2005.csv', usecols=cols),
    pd.read_csv('archive/atp_matches_2006.csv', usecols=cols),
    pd.read_csv('archive/atp_matches_2007.csv', usecols=cols),
    pd.read_csv('archive/atp_matches_2008.csv', usecols=cols),
    pd.read_csv('archive/atp_matches_2009.csv', usecols=cols),
    pd.read_csv('archive/atp_matches_2010.csv', usecols=cols),
    pd.read_csv('archive/atp_matches_2011.csv', usecols=cols),
    pd.read_csv('archive/atp_matches_2012.csv', usecols=cols),
    pd.read_csv('archive/atp_matches_2013.csv', usecols=cols),
    pd.read_csv('archive/atp_matches_2014.csv', usecols=cols),
    pd.read_csv('archive/atp_matches_2015.csv', usecols=cols),
    pd.read_csv('archive/atp_matches_2016.csv', usecols=cols),
    pd.read_csv('archive/atp_matches_2017.csv', usecols=cols),
],ignore_index=True) #have to make sure that the index will not be duplicated

df.tail()

min_date = "2005318"
max_date = "2012318"

date_df = df.loc[
    (df['tourney_date'].astype(str) >= min_date) &
    (df['tourney_date'].astype(str) <= max_date)].copy()