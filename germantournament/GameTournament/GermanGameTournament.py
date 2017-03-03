"""This module contains the GermanGameTournament class."""


class GermanGameTournament(object):
    """Contain the GermanGameTournament class."""

    def __init__(self):
        """Contain the GermanGameTournament class."""
        self._players = []
        self._game_per_player = 2

    def set_players(self, players):
        """Contain the GermanGameTournament class."""
        self._players = players

    def _fix_players(self, player_count_in_one_game):
        """Contain the GermanGameTournament class."""
        player_count = self.player_count(player_count_in_one_game)

        while player_count > len(self._players):
            self._players.append(max(self._players) + 1)

        while len(self._players) > player_count and (len(self._players) % player_count) != 0:
            self._players.append(max(self._players) + 1)

    def schedule(self, player_count_in_one_game=4):
        """
        Return scheduled plays.

        :param player_count_in_one_game: Player count in the each sperate game
        :type player_count_in_one_game: int
        :rtype: list
        """
        events = []
        self._fix_players(player_count_in_one_game)
        players = self.players
        iteration = self._game_per_player - 1

        for index in range(1, int(len(self._players) / self.player_count(player_count_in_one_game)) + 1):

            while 0 <= iteration:
                _events = {}
                for player in players:
                    player_ = player / index
                    modulo = pow(player_count_in_one_game, iteration)
                    prefix = int(player_ / pow(player_count_in_one_game, iteration + 1))

                    hashing = str(prefix) + str(int(player_ % modulo))
                    if hashing in _events:
                        _events[hashing].append(player)
                    else:
                        _events[hashing] = [player, ]

                for event in _events.values():
                    events.append(event)

                iteration -= 1
        return events

    def player_count(self, player_count_in_one_game):
        """Contain the GermanGameTournament class."""
        return pow(player_count_in_one_game, self._game_per_player)

    @property
    def players(self):
        """Contain the GermanGameTournament class."""
        return self._players
