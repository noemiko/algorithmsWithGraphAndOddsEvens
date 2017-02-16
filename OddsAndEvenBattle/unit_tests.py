import unittest
from war import War


class TestWar(unittest.TestCase):

    def test_binary_conversion(self):
        #given
        int_data = [-100, 5, 100, -8]
        war = War()
        #when
        result = war.convert_to_binary(int_data)
        #then
        expected = ['-1100100', '101', '1100100', '-1000']
        self.assertEqual(result, expected)

    def test_count_fight_points_for_odds(self):
        # given
        binary_data = ['-1100100', '101', '1100100', '-1000']
        war = War()
        # when
        result = war.count_battle_points(binary_data, '1')
        # then
        expected = {'positive': 4, 'negative': 5}
        self.assertEqual(result, expected)

    def test_count_battle_points_for_evens(self):
        # given
        binary_data = ['-1100100', '101', '1100100', '-1000']
        war = War()
        # when
        result = war.count_battle_points(binary_data, '0')
        # then
        expected = {'positive': 7, 'negative': 5}
        self.assertEqual(result, expected)

    def test_calculate_winner_when_odds_win(self):
        # given
        odds_points = {'positive': 10, 'negative': 5}
        evens_points = {'positive': 7, 'negative': 5}
        war = War()
        # when
        result = war.calculate_winner(odds_points, evens_points)
        # then
        self.assertEqual(result, 'odds win')

    def test_calculate_winner_when_evens_win(self):
        # given
        odds_points = {'positive': 7, 'negative': 25}
        evens_points = {'positive': 7, 'negative': 5}
        war = War()
        # when
        result = war.calculate_winner(odds_points, evens_points)
        # then
        self.assertEqual(result, 'evens win')

    def test_calculate_winner_when_evens_win(self):
        # given
        odds_points = {'positive': 15, 'negative': 5}
        evens_points = {'positive': 20, 'negative': 10}
        war = War()
        # when
        result = war.calculate_winner(odds_points, evens_points)
        # then
        self.assertEqual(result, 'tie')

if __name__ == '__main__':
    unittest.main()