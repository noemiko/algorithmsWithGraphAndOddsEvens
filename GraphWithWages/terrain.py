class SquareTerrain:

    def __init__(self, terrain):
        self.terrain = terrain

    def in_bounds_of_terrain(self, id):
        (x, y) = id
        return 0 <= x < len(self.terrain) and 0 <= y < len(self.terrain)

    # possible moves are only to the right or down
    def allowed_moves(self, id):
        (x, y) = id
        results = [(x + 1, y), (x, y + 1)]
        return filter(self.in_bounds_of_terrain, results)

    # cost for move to this field
    def cost(self, field):
        (x, y) = field
        return self.terrain[x][y]
