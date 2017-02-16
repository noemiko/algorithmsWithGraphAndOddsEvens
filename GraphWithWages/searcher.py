from queue import PriorityQueue


class Searcher:

    def __init__(self, graph, start, goal):
        self.graph = graph
        self.start = start
        self.goal = goal

    def find_optimal_cost(self):
        costs = self.dijkstra_algorithm()
        optimal_cost = costs.get(self.goal)
        return optimal_cost

    def dijkstra_algorithm(self):
        queue = PriorityQueue()
        queue.put(self.start, 0)
        came_from = {}
        cost_so_far = {}
        came_from[self.start] = None
        cost_so_far[self.start] = self.graph.cost(self.start)

        while not queue.empty():
            current = queue.get()

            if current == self.goal:
                break

            for next_field in self.graph.allowed_moves(current):
                new_cost = cost_so_far[current] + self.graph.cost(next_field)
                if next_field not in cost_so_far or new_cost < cost_so_far[next_field]:
                    cost_so_far[next_field] = new_cost
                    priority = new_cost
                    queue.put(next_field, priority)
                    came_from[next_field] = current
        return cost_so_far
