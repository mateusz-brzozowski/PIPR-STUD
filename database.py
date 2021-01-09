import pandas as pd

cols = [
    'tourney_id',
    'tourney_name',
    'surface',
    'draw_size',
    'tourney_level',
    'tourney_date',
    'match_num',
    'winner_id',
    'winner_seed',
    'winner_entry',
    'winner_name',
    'winner_hand',
    'winner_ht',
    'winner_ioc',
    'winner_age',
    'winner_rank',
    'winner_rank_points',
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
    'score',
    'best_of',
    'round',
    'minutes',
    'w_ace',
    'w_df',
    'w_svpt',
    'w_1stIn',
    'w_1stWon',
    'w_2ndWon',
    'w_SvGms',
    'w_bpSaved',
    'w_bpFaced',
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
    pd.read_csv('archive/atp_matches_2017.csv', usecols=cols)],
    ignore_index=True
)

df.tail()

values = {
    "Total number of Wins to Losses": ['winner_name', 'loser_name'],
    "Wins to Losses between players": ['winner_name', 'loser_name'],
    "Wins to Losses on Hard surface": ['winner_name', 'loser_name', 'surface'],
    "Wins to Losses on Clay surface": ['winner_name', 'loser_name', 'surface'],
    "Wins to Losses on Grass surface":
        ['winner_name', 'loser_name', 'surface'],
    # of winner (L=Left, R=Right, U=Unknown?)
    "Dominant hand": ['winner_hand', 'loser_hand'],
    "Height in cm": ['winner_ht', 'loser_ht'],
    "Country of winner": ['winner_ioc', 'loser_ioc'],
    "Number of aces": ['w_ace', 'l_ace'],
    "Number of double faults": ['w_df', 'l_df'],
    "Number of service points": ['w_svpt', 'l_svpt'],
    "Number of first serves in": ['w_1stIn', 'l_1stIn'],
    "Number of first serve points won": ['w_1stWon', 'l_1stWon'],
    "Number of second serve points won": ['w_2ndWon', 'l_2ndWon'],
    "Number of service games played": ['w_SvGms', 'l_SvGms'],
    "Number of break points saved": ['w_bpSaved', 'l_bpSaved'],
    "Number of break points faced": ['w_bpFaced', 'l_bpFaced'],
}


def getTournaments(player1, player2):
    player1_df = df.loc[
        (df['winner_name'] == player1) | (df['loser_name'] == player1)].copy()
    player2_df = player1_df.loc[
        (player1_df['winner_name'] == player2) |
        (player1_df['loser_name'] == player2)].copy()
    players = player2_df[['tourney_name']].astype(str).values.ravel()
    unique_players = pd.unique(players)
    player_list = [player for player in unique_players if player != "nan"]
    return sorted(player_list)


def getSecondPlayers(player1):
    player1_df = df.loc[
        (df['winner_name'] == player1) | (df['loser_name'] == player1)].copy()
    players = player1_df[
        ['winner_name', 'loser_name']].astype(str).values.ravel()
    unique_players = pd.unique(players)
    player_list = [player for player in unique_players if player != "nan"]
    player_list.remove(player1)
    return sorted(player_list)


def getAllElements(labels):
    elements = df[labels].astype(str).values.ravel()
    unique_elements = pd.unique(elements)
    elements_list = [
        element for element in unique_elements if element != "nan"]
    return sorted(elements_list)


def getIndexes():
    return values


def getDataFrame(player1, player2, tourney_name):
    player1_df = df.loc[
        (df['winner_name'] == player1) | (df['loser_name'] == player1)].copy()
    player2_df = player1_df.loc[
        (player1_df['winner_name'] == player2) |
        (player1_df['loser_name'] == player2)].copy()
    data_frame = player2_df.loc[(df['tourney_name'] == tourney_name)].copy()
    return data_frame


def get_sum_btw_players_in_columns(player1, player2, tourney_name, columns):
    data_frame = getDataFrame(player1, player2, tourney_name)
    w1 = data_frame.loc[df['winner_name'] == player1].sum()
    l1 = data_frame.loc[df['loser_name'] == player1].sum()
    w2 = data_frame.loc[df['winner_name'] == player2].sum()
    l2 = data_frame.loc[df['loser_name'] == player2].sum()
    pass
    # df.loc[df[['w_ace', 'l_ace']].count()[0]



def get_total_w_l(player):
    winnings = df.loc[df['winner_name'] == player].count()[0]
    losers = df.loc[df['loser_name'] == player].count()[0]
    return winnings, losers


def get_better(player1, player2):
    players = df.loc[
        (df['winner_name'] == player1) | (df['loser_name'] == player1)].copy()
    player1_wins = players.loc[
        (players['winner_name'] == player1) &
        (players['loser_name'] == player2)].count()[0]
    player2_wins = players.loc[
        (players['winner_name'] == player2) &
        (players['loser_name'] == player1)].count()[0]
    return player1_wins, player2_wins


def get_surface(tourney_name):
    return df.loc[df['tourney_name'] == tourney_name, "surface"].iloc[0]


def get_w_l_on_surface(player, tourney_name):
    surface = get_surface(tourney_name)
    winnings = df.loc[
        (df['winner_name'] == player) & (df['surface'] == surface)].count()[0]
    losers = df.loc[
        (df['loser_name'] == player) & (df['surface'] == surface)].count()[0]
    return winnings, losers


if __name__ == "__main__":
    get_sum_btw_players_in_columns("Novak Djokovic", "Juan Martin Del Potro", "US Open", [])
    df = getDataFrame("Novak Djokovic", "Juan Martin Del Potro", "US Open")
    print(df)
    pass
