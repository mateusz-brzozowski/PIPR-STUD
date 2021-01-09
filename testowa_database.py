import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
# %matplotlib inline
plt.style.use('fivethirtyeight')

import os
for dirname, _, filenames in os.walk('archive'):
        for filename in filenames:
            print(os.path.join(dirname, filename))

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

roger = df.loc[(df['winner_name'] == 'Antony Dupuis') | (df['loser_name'] == 'Antony Dupuis')].copy()
#we want to analyze his performance over time but date is not float 64, so let's change it to datettime datatype.
roger.tourney_date.apply(lambda x: '%.0f' % round(x,0))

roger.loc[:,'tourney_date'] = pd.to_datetime(roger['tourney_date'], format='%Y%m%d')
# Let's look at his serve performance over the time. However, we have to look at the number of serve whether it is winner or loser based on loser or winner
# how important is the serve
# let's define variable that we will use a lot
rogerwin = roger.loc[roger['winner_name'] == 'Antony Dupuis'].copy()
rogerloss = roger.loc[roger['loser_name'] == 'Antony Dupuis'].copy()
# print(f'Number of wins: {rogerwin.count()[0]}')
# print(f'Number of losses: {rogerloss.count()[0]}')

    #let's plot the number of wins and losses from 2000 to
fig = plt.figure(figsize=(5,5))
import matplotlib as mpl

plt.title("No. of Roger's Wins and Losses throughout his careers")
plt.pie([rogerwin.count()[0],rogerloss.count()[0]],labels = [f'{rogerwin.count()[0]} matches won',f'{rogerloss.count()[0]} matches lost'],textprops={'fontsize': 20})
plt.show()


tour = rogerwin.loc[rogerwin.tourney_level == 'G'].groupby(rogerwin.tourney_id).count()
championship = tour.loc[tour.tourney_id == 7]
plt.title('No. of Grandslam Championships')
plt.yticks([1,2,3])
grandslams = championship.groupby(championship.index.map(lambda x: x[0:4])).count()
plt.bar(grandslams.index,grandslams.tourney_id)

plt.show()
#  -----------------------------------------------------------------------------------
loss = roger.loc[roger.winner_name != 'Roger Federer', ['winner_name']]
# loss.rename(r={'winner_name': 'name'})
loss.columns = ['name']
loss['status'] = 'loss'
win = roger.loc[roger.winner_name == 'Roger Federer', ['loser_name']]
win.columns = ['name']
win['status'] = 'win'
opponents = pd.concat([win,loss])
# opponents
opponents.groupby('name').count().sort_values('status', ascending = False)

opponents_grouped = pd.DataFrame()
opponents_grouped['No. of matches'] = numberofmatches.status
opponents_grouped['No. of winning'] = opponents.loc[opponents.status=='win'].groupby('name').count().status
opponents_grouped['percentage'] = opponents_grouped['No. of winning']/opponents_grouped['No. of matches']
opponents_grouped.loc[opponents_grouped['No. of matches'] > 10].sort_values('percentage',ascending = True).head()

opponents.loc[opponents.status=='win'].groupby('name').count()
plt.xlabel('opponent name')
plt.ylabel("Percentage of Roger's winning")
plt.xticks(rotation='vertical')
# plt.bar(opponents_grouped.sort_values('percentage',ascending = True).index[0:10], opponents_grouped.sort_values('percentage',ascending = True).percentage[0:10])

plt.bar(opponents_grouped.loc[opponents_grouped['No. of matches'] > 10].sort_values('percentage',ascending = True).index[0:10], opponents_grouped.sort_values('percentage',ascending = True).percentage[0:10])
plt.title("Roger's Strongest Opponents")

plt.show()
