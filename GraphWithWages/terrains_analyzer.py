import io
import sys
from searcher import Searcher
from terrain import SquareTerrain


class TerrainsAnalyzer:

    def __init__(self, path_to_file):
        self.terrains = self.extract_data_from_file(path_to_file)

    def extract_data_from_file(self, path):
        with io.open(path, 'r') as f:
            data = [x.rstrip() for x in f]
        return self.extract_terrains(data)

    #return the smallest cost for travel each terrains
    def get_terrains_costs(self):
        costs = []
        for terrain in self.terrains:
            costs.append(self.minimum_effort_to_travel(terrain))
        return "\n".join(map(str, costs))

    # return the smallest cost for travel one terrain
    def minimum_effort_to_travel(self, terrain):
        last_index = len(terrain) - 1
        start_point = (0, 0)
        end_point = (last_index, last_index)

        g = SquareTerrain(terrain)
        optimal = Searcher(g, start_point, end_point)
        return optimal.find_optimal_cost()

    #return array with arrays that represent each terrains
    def extract_terrains(self, data):
        sizes = []
        terrains = []
        for i in data:
            if self.is_int(i):
                sizes.append(int(i))
            else:
                i = self.split_rows(i)
                terrains.append(i)
        return self.divide_terrains(sizes, terrains)

    def divide_terrains(self, sizes, terrains):
        all_terrains = []
        for size in sizes:
            all_terrains.append(terrains[:size])
            del terrains[:size]
        return all_terrains

    def split_rows(self, row):
        try:
            row = [int(x) for x in row.split(',')]
            return row
        except ValueError:
            print('wrong data in terrain: {}'.format(row))
            sys.exit(0)

    def is_int(self, s):
        try:
            int(s)
            return True
        except ValueError:
            return False

if __name__ == "__main__":

    terrains = TerrainsAnalyzer('./input.txt')
    print(terrains.get_terrains_costs())
