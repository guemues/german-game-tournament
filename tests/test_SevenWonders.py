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

    def test_schedule_for_2(self):
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
        self.assertCountEqual(
            self.tournament.schedule(player_count_in_one_game=2),
            [[0, 1], [2, 3],
             [0, 2], [1, 3],
             [4, 5], [6, 7],
             [4, 6], [5, 7]])

    def test_schedule_for_4(self):
        self.assertEqual(self.tournament.players, [])
        self.tournament.set_players(list(range(0, 16)))
        self.assertCountEqual(
            self.tournament.schedule(player_count_in_one_game=4),
            [[0, 1, 2, 3],  [4, 5, 6, 7],  [8, 9, 10, 11], [12, 13, 14, 15],
             [0, 4, 8, 12], [1, 5, 9, 13], [2, 6, 10, 14], [3, 7, 11, 15]])

    def test_schedule_for_4x2(self):
        self.assertEqual(self.tournament.players, [])
        self.tournament.set_players(list(range(0, 32)))
        self.assertCountEqual(
            self.tournament.schedule(player_count_in_one_game=4),
            [[0, 1, 2, 3],  [4, 5, 6, 7],  [8, 9, 10, 11], [12, 13, 14, 15],
             [0, 4, 8, 12], [1, 5, 9, 13], [2, 6, 10, 14], [3, 7, 11, 15],
             [16, 17, 18, 19], [20, 21, 22, 23], [24, 25, 26, 27], [28, 29, 30, 31],
             [16, 20, 24, 28], [17, 21, 25, 29], [18, 22, 26, 30], [19, 23, 27, 31]
             ])
