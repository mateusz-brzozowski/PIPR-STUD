import pandas as pd
import math

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
    "W/L between players": ['winner_name', 'loser_name', 'local'],
    "Height in cm": ['winner_ht', 'loser_ht', 'local'],
    "No. aces": ['w_ace', 'l_ace', 'local'],
    "No. double faults": ['w_df', 'l_df', 'local'],
    "No. service points": ['w_svpt', 'l_svpt', 'local'],
    "No. 1. serves in": ['w_1stIn', 'l_1stIn', 'local'],
    "No. 1. serve points won": ['w_1stWon', 'l_1stWon', 'local'],
    "No. 2. serve points won": ['w_2ndWon', 'l_2ndWon', 'local'],
    "No. service games played": ['w_SvGms', 'l_SvGms', 'local'],
    "No. break points saved": ['w_bpSaved', 'l_bpSaved', 'local'],
    "No. break points faced": ['w_bpFaced', 'l_bpFaced', 'local'],
    "Total no. W/L": ['winner_name', 'loser_name', 'general'],
    "W/L on Hard surface":
        ['winner_name', 'loser_name', 'general', 'surface', 'Hard'],
    "W/L on Clay surface":
        ['winner_name', 'loser_name', 'general', 'surface', 'Clay'],
    "W/L on Grass surface":
        ['winner_name', 'loser_name', 'general', 'surface', 'Grass'],
    "Total no. aces": ['w_ace', 'l_ace', 'general'],
    "Total no. double faults": ['w_df', 'l_df', 'general'],
    "Total no. service points": ['w_svpt', 'l_svpt', 'general'],
    "Total no. 1. serves in": ['w_1stIn', 'l_1stIn', 'general'],
    "Total no. 1. serve points won": ['w_1stWon', 'l_1stWon', 'general'],
    "Total no. 2. serve points won": ['w_2ndWon', 'l_2ndWon', 'general'],
    "Total no. service games played": ['w_SvGms', 'l_SvGms', 'general'],
    "Total no. break points saved": ['w_bpSaved', 'l_bpSaved', 'general'],
    "Total no. break points faced": ['w_bpFaced', 'l_bpFaced', 'general'],
}


def get_tournaments(player1, player2):
    player1_df = df.loc[
        (df['winner_name'] == player1) | (df['loser_name'] == player1)].copy()
    player2_df = player1_df.loc[
        (player1_df['winner_name'] == player2) |
        (player1_df['loser_name'] == player2)].copy()
    players = player2_df[['tourney_name']].astype(str).values.ravel()
    unique_players = pd.unique(players)
    player_list = [player for player in unique_players if player != "nan"]
    return sorted(player_list)


def get_second_players(player1):
    player1_df = df.loc[
        (df['winner_name'] == player1) | (df['loser_name'] == player1)].copy()
    players = player1_df[
        ['winner_name', 'loser_name']].astype(str).values.ravel()
    unique_players = pd.unique(players)
    player_list = [player for player in unique_players if player != "nan"]
    player_list.remove(player1)
    return sorted(player_list)


def get_all_elements(labels):
    elements = df[labels].astype(str).values.ravel()
    unique_elements = pd.unique(elements)
    elements_list = [
        element for element in unique_elements if element != "nan"]
    return sorted(elements_list)


def get_indexes():
    return values


def getDataFrame(player1, player2, tourney_name):
    player1_df = df.loc[
        (df['winner_name'] == player1) | (df['loser_name'] == player1)].copy()
    player2_df = player1_df.loc[
        (player1_df['winner_name'] == player2) |
        (player1_df['loser_name'] == player2)].copy()
    data_frame = player2_df.loc[(df['tourney_name'] == tourney_name)].copy()
    return data_frame


def get_winratio_columns(player1, player2, tourney_name, columns):
    if columns[2] == "local":
        data_frame = getDataFrame(player1, player2, tourney_name)
    else:
        data_frame = df.copy()
    if len(columns) > 4:
        data_frame = data_frame.loc[
            data_frame[columns[3]] == columns[4]].copy()
    player1_wins = data_frame.loc[
        data_frame['winner_name'] == player1].count()[0]
    player1_losses = data_frame.loc[
        data_frame['loser_name'] == player1].count()[0]
    player2_wins = data_frame.loc[
        data_frame['winner_name'] == player2].count()[0]
    player2_losses = data_frame.loc[
        data_frame['loser_name'] == player2].count()[0]
    return player1_wins, player1_losses, player2_wins, player2_losses


def get_sum_in_columns(player1, player2, tourney_name, columns):
    if columns[2] == "local":
        data_frame = getDataFrame(player1, player2, tourney_name)
    else:
        data_frame = df.copy()
    player1_data = data_frame.loc[
        data_frame['winner_name'] == player1].sum()[columns[0]]
    player1_data += data_frame.loc[
        data_frame['loser_name'] == player1].sum()[columns[1]]
    player2_data = data_frame.loc[
        data_frame['winner_name'] == player2].sum()[columns[0]]
    player2_data += data_frame.loc[
        data_frame['loser_name'] == player2].sum()[columns[1]]
    return player1_data, player2_data


def check_nan(value):
    if math.isnan(value):
        value = 0
    return value


def get_best_in_columns(player1, player2, tourney_name, columns):
    if columns[2] == "local":
        data_frame = getDataFrame(player1, player2, tourney_name)
    else:
        data_frame = df.copy()
    player1_winner = data_frame.loc[
        data_frame['winner_name'] == player1][columns[0]].max()
    player1_winner = check_nan(player1_winner)

    player1_losser = data_frame.loc[
        data_frame['loser_name'] == player1][columns[1]].max()
    player1_losser = check_nan(player1_losser)

    player2_winner = data_frame.loc[
        data_frame['winner_name'] == player2][columns[0]].max()
    player2_winner = check_nan(player2_winner)

    player2_losser = data_frame.loc[
        data_frame['loser_name'] == player2][columns[1]].max()
    player2_losser = check_nan(player2_losser)

    player1_data = max(player1_winner, player1_losser)
    player2_data = max(player2_winner, player2_losser)
    return player1_data, player2_data


def get_surface(tourney_name):
    return df.loc[df['tourney_name'] == tourney_name, "surface"].iloc[0]


if __name__ == "__main__":
    get_sum_in_columns("Nicolas Mahut", "John Isner", "Wimbledon", ['winner_ht', 'loser_ht', 'local'])
    df = getDataFrame("Novak Djokovic", "Juan Martin Del Potro", "US Open")
    print(df)
    pass
