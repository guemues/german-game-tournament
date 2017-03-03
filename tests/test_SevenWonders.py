from germantournament.GameTournament.GermanGameTournament import GermanGameTournament
from unittest import TestCase


class TestSevenWonders(TestCase):
    @classmethod
    def setup_class(cls):
        """This method is run once for each class before any tests are run"""

    @classmethod
    def teardown_class(cls):
        """This method is run once for each class _after_ all tests are run"""

    def setUp(self):
        """This method is run once before _each_ test method is executed"""
        self.tournament = GermanGameTournament()

    def teardown(self):
        """This method is run once after _each_ test method is executed"""

    def test_init(self):
        self.assertEqual(self.tournament.players, [])

    def test_fix_player_count(self):
        self.tournament.set_players(list(range(0, 4)))
        self.tournament._fix_players(player_count_in_one_game=2)
        self.assertEqual(len(self.tournament.players) % 4, 0)

        self.tournament.set_players(list(range(0, 8)))
        self.tournament._fix_players(player_count_in_one_game=2)
        self.assertEqual(len(self.tournament.players) % 4, 0)

        self.tournament.set_players(list(range(0, 2)))
        self.tournament._fix_players(player_count_in_one_game=2)
        self.assertEqual(len(self.tournament.players) % 4, 0)

        self.tournament.set_players(list(range(0, 3)))
        self.tournament._fix_players(player_count_in_one_game=2)
        self.assertEqual(len(self.tournament.players) % 4, 0)

        self.tournament.set_players(list(range(0, 10)))
        self.tournament._fix_players(player_count_in_one_game=2)
        self.assertEqual(len(self.tournament.players) % 4, 0)

    def test_schedule(self):
        self.assertEqual(self.tournament.players, [])
        self.tournament.set_players(list(range(0, 4)))
        self.assertCountEqual(
            self.tournament.schedule(player_count_in_one_game=2),
            [[0, 1], [2, 3],
             [0, 2], [1, 3]])

        self.tournament.set_players(list(range(0, 3)))
        self.assertCountEqual(
            self.tournament.schedule(player_count_in_one_game=2),
            [[0, 1], [2, 3],
             [0, 2], [1, 3]])

        self.tournament.set_players(list(range(0, 5)))
        print(self.tournament.schedule(player_count_in_one_game=2))
        self.assertCountEqual(
            self.tournament.schedule(player_count_in_one_game=2),
            [[0, 1], [2, 3],
             [0, 2], [1, 3],
             [4, 5], [6, 7],
             [4, 6], [5, 7]])
