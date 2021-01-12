import pandas as pd
import math


class InvalidIndexName(Exception):
    pass


class MissingNameError(Exception):
    pass


class InvalidFilePath(Exception):
    pass


class NegativeRange(Exception):
    pass


class Database:
    """
    Database class contains all functions responsible for data storage,
    data manipulation and return
    """
    def __init__(self):
        """Initializes a Database"""
        self.cols = [
            'tourney_id', 'tourney_name', 'surface', 'draw_size',
            'tourney_level', 'tourney_date', 'match_num', 'winner_id',
            'winner_seed', 'winner_entry', 'winner_name', 'winner_hand',
            'winner_ht', 'winner_ioc', 'winner_age', 'winner_rank',
            'winner_rank_points', 'loser_id', 'loser_seed', 'loser_entry',
            'loser_name', 'loser_hand', 'loser_ht', 'loser_ioc',
            'loser_age', 'loser_rank', 'loser_rank_points', 'score',
            'best_of', 'round', 'minutes', 'w_ace', 'w_df', 'w_svpt',
            'w_1stIn', 'w_1stWon', 'w_2ndWon', 'w_SvGms', 'w_bpSaved',
            'w_bpFaced', 'l_ace', 'l_df', 'l_svpt', 'l_1stIn',
            'l_1stWon', 'l_2ndWon', 'l_SvGms', 'l_bpSaved', 'l_bpFaced'
        ]
        self.df = pd.DataFrame()
        self.values = {
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
            "W/L on ATP Tour":
                ['winner_name', 'loser_name', 'general', 'tourney_level', 'A'],
            "W/L on Davis Cup":
                ['winner_name', 'loser_name', 'general', 'tourney_level', 'D'],
            "W/L on Grand Slam":
                ['winner_name', 'loser_name', 'general', 'tourney_level', 'G'],
            "W/L on Masters":
                ['winner_name', 'loser_name', 'general', 'tourney_level', 'M'],
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
            "Total no. 1. serve points won":
                ['w_1stWon', 'l_1stWon', 'general'],
            "Total no. 2. serve points won":
                ['w_2ndWon', 'l_2ndWon', 'general'],
            "Total no. service games played":
                ['w_SvGms', 'l_SvGms', 'general'],
            "Total no. break points saved":
                ['w_bpSaved', 'l_bpSaved', 'general'],
            "Total no. break points faced":
                ['w_bpFaced', 'l_bpFaced', 'general'],
        }

    def from_csv(self, paths):
        """Reads data from files"""
        files = []
        for path in paths:
            try:
                files.append(pd.read_csv(path, usecols=self.cols))
            except FileNotFoundError:
                raise InvalidFilePath
        self.df = pd.concat(files, ignore_index=True)
        self.df.tail()

    def get_tournaments(self, player1, player2):
        """Returns a sorted list of tournament names"""
        self.check_player(player1)
        self.check_player(player2)
        player1_df = self.df.loc[
            (self.df['winner_name'] == player1) |
            (self.df['loser_name'] == player1)].copy()
        player2_df = player1_df.loc[
            (player1_df['winner_name'] == player2) |
            (player1_df['loser_name'] == player2)].copy()
        players = player2_df[['tourney_name']].astype(str).values.ravel()
        unique_players = pd.unique(players)
        player_list = [player for player in unique_players if player != "nan"]
        return sorted(player_list)

    def check_player(self, player):
        """Checks if the player is in the database"""
        player_df = self.df.loc[
            (self.df['winner_name'] == player) |
            (self.df['loser_name'] == player)].count()[0]
        if player_df == 0:
            raise MissingNameError()

    def get_second_players(self, player1):
        """
        Returns a sorted list of the players
        who have played with given player
        """
        self.check_player(player1)
        player1_df = self.df.loc[
            (self.df['winner_name'] == player1) |
            (self.df['loser_name'] == player1)].copy()

        players = player1_df[
            ['winner_name', 'loser_name']].astype(str).values.ravel()
        unique_players = pd.unique(players)

        player_list = [
            player for player in unique_players if player != "nan"]
        player_list.remove(player1)
        return sorted(player_list)

    def get_all_elements(self, labels):
        """Returns a sorted list of the players"""
        try:
            elements = self.df[labels].astype(str).values.ravel()
        except KeyError:
            raise InvalidIndexName()
        unique_elements = pd.unique(elements)
        elements_list = [
            element for element in unique_elements if element != "nan"]
        return sorted(elements_list)

    def get_indexes(self):
        """Returns all user-usable variables"""
        return self.values

    def get_data_frame_with_date(self, min_date, max_date):
        """Returns a data frame in the given date range"""
        if int(min_date) > int(max_date):
            raise NegativeRange()
        date_df = self.df.loc[
            (self.df['tourney_date'].astype(str) >= min_date) &
            (self.df['tourney_date'].astype(str) <= max_date)].copy()
        return date_df

    def get_data_frame(
        self, player1, player2, tourney_name, min_date, max_date
    ):
        """
        Returns a data frame where both players competed
        for the given date range
        """
        if int(min_date) > int(max_date):
            raise NegativeRange()
        date_df = self.get_data_frame_with_date(min_date, max_date)
        player1_df = date_df.loc[
            (date_df['winner_name'] == player1) |
            (date_df['loser_name'] == player1)].copy()
        player2_df = player1_df.loc[
            (player1_df['winner_name'] == player2) |
            (player1_df['loser_name'] == player2)].copy()
        data_frame = player2_df.loc[
            (self.df['tourney_name'] == tourney_name)].copy()
        return data_frame

    def get_winratio_columns(
        self, player1, player2, tourney_name, columns, min_date, max_date
    ):
        """
        The function based on the given parameters
        counts the number of occurrences of the variable
        """
        if columns[2] == "local":
            data_frame = self.get_data_frame(
                player1, player2, tourney_name, min_date, max_date)
        else:
            data_frame = self.get_data_frame_with_date(min_date, max_date)
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

    def get_sum_in_columns(
        self, player1, player2, tourney_name, columns, min_date, max_date
    ):
        """
        The function search based on the given parameters
        values in the columns and sums them up
        """
        if columns[2] == "local":
            data_frame = self.get_data_frame(
                player1, player2, tourney_name, min_date, max_date)
        else:
            data_frame = self.get_data_frame_with_date(min_date, max_date)
        player1_data = data_frame.loc[
            data_frame['winner_name'] == player1].sum()[columns[0]]
        player1_data += data_frame.loc[
            data_frame['loser_name'] == player1].sum()[columns[1]]
        player2_data = data_frame.loc[
            data_frame['winner_name'] == player2].sum()[columns[0]]
        player2_data += data_frame.loc[
            data_frame['loser_name'] == player2].sum()[columns[1]]
        return player1_data, player2_data

    def check_nan(self, value):
        """Returns a valid variable value"""
        if math.isnan(value):
            value = 0
        return value

    def get_best_in_columns(
        self, player1, player2, tourney_name, columns, min_date, max_date
    ):
        """
        The function search based on the given parameters
        the maximum values in the columns
        """
        if columns[2] == "local":
            data_frame = self.get_data_frame(
                player1, player2, tourney_name, min_date, max_date)
        else:
            data_frame = self.get_data_frame_with_date(min_date, max_date)
        player1_winner = data_frame.loc[
            data_frame['winner_name'] == player1][columns[0]].max()
        player1_winner = self.check_nan(player1_winner)

        player1_losser = data_frame.loc[
            data_frame['loser_name'] == player1][columns[1]].max()
        player1_losser = self.check_nan(player1_losser)

        player2_winner = data_frame.loc[
            data_frame['winner_name'] == player2][columns[0]].max()
        player2_winner = self.check_nan(player2_winner)

        player2_losser = data_frame.loc[
            data_frame['loser_name'] == player2][columns[1]].max()
        player2_losser = self.check_nan(player2_losser)

        player1_data = max(player1_winner, player1_losser)
        player2_data = max(player2_winner, player2_losser)
        return player1_data, player2_data

    def get_surface(self, tourney_name):
        """
        Returns the name of the surface on which
        the given tournament takes place
        """
        try:
            return self.df.loc[
                self.df['tourney_name'] == tourney_name, "surface"].iloc[0]
        except IndexError:
            raise InvalidIndexName()
