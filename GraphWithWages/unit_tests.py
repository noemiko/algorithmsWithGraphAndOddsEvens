import unittest
from mock import mock
from terrains_analyzer import TerrainsAnalyzer
from terrain import SquareTerrain


class TestTerrainsAnalyzer(unittest.TestCase):

    def test_minimum_effort_to_travel_2x2(self):
        #given
        terrain = [[4, 6], [2, 8]]
        TerrainsAnalyzer.extract_data_from_file = mock.Mock(return_value=terrain)
        analyzer = TerrainsAnalyzer('')

        #when
        result = analyzer.minimum_effort_to_travel(terrain)
        #then
        self.assertEqual(result, 14)

    def test_minimum_effort_to_travel_3x3(self):
        # given
        terrain = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        TerrainsAnalyzer.extract_data_from_file = mock.Mock(return_value=terrain)
        analyzer = TerrainsAnalyzer('')
         # when
        result = analyzer.minimum_effort_to_travel(terrain)
        # then
        self.assertEqual(result, 21)

    def test_minimum_effort_to_travel_3x3(self):
        # given
        terrain = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        TerrainsAnalyzer.extract_data_from_file = mock.Mock(return_value=terrain)
        analyzer = TerrainsAnalyzer('')
         # when
        result = analyzer.minimum_effort_to_travel(terrain)
        # then
        self.assertEqual(result, 21)

    def test_minimum_effort_to_travel_5x5(self):
        # given
        terrain = [[1, 2, 3, 4, 6], [1, 8, 9, 10, 3], [1, 12, 13, 14, 6], [1, 5, 6, 5, 4], [1, 1, 1, 1, 1]]
        TerrainsAnalyzer.extract_data_from_file = mock.Mock(return_value=terrain)
        analyzer = TerrainsAnalyzer('')
        # when
        result = analyzer.minimum_effort_to_travel(terrain)
        # then
        self.assertEqual(result, 9)

    def test_extract_2_terrains(self):
        # given
        terrain = ['2', '4, 6', '2, 8', '3', '1, 2, 3', '4, 5, 6', '7, 8, 9']
        TerrainsAnalyzer.extract_data_from_file = mock.Mock(return_value='')
        analyzer = TerrainsAnalyzer('')
        # when
        result = analyzer.extract_terrains(terrain)
        # then
        expected = [[[4, 6], [2, 8]], [[1, 2, 3], [4, 5, 6], [7, 8, 9]]]
        self.assertEqual(result, expected)

    def test_extract_terrains_if_data_not_correct(self):
        # given
        terrain = ['2', 'j,5', '2, 8', '3', '1, 2, 3', '4, 5, 6', '7, 8, 9']
        TerrainsAnalyzer.extract_data_from_file = mock.Mock(return_value='')
        analyzer = TerrainsAnalyzer('')
        self.assertRaises(SystemExit, analyzer.extract_terrains, terrain)

class TestTerrains(unittest.TestCase):

    def test_is_not_in_bounds(self):
        # given
        terrain = SquareTerrain([[2, 2], [2, 2]])
        # when
        result = terrain.in_bounds_of_terrain((2, 2))
        # then
        self.assertFalse(result)

    def test_is_in_bounds(self):
        # given
        terrain = SquareTerrain([[2, 2],[2, 2]])
        # when
        result = terrain.in_bounds_of_terrain((1,1))
        # then
        self.assertTrue(result)

    def test_get_possible_moves_when_allowed_only_to_down(self):
        # given
        terrain = SquareTerrain([[2, 2], [2, 2]])
        # when
        result = terrain.allowed_moves((0, 1))
        # then
        self.assertEqual(result, [(1, 1)])

    def test_get_possible_moves_(self):
        # given
        terrain = SquareTerrain([[2, 2, 2], [2, 2, 2], [2, 2, 2]])
        # when
        result = terrain.allowed_moves((1,1))
        # then
        self.assertEqual(result, [(2, 1), (1, 2)])


if __name__ == '__main__':
    unittest.main()

#pip install -U mock