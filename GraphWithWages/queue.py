import heapq


class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    # add to queue new coordinates with cost
    def put(self, field_coordinates, priority):
        heapq.heappush(self.elements, (priority, field_coordinates))

    # get cheapest coordinates
    def get(self):
        return heapq.heappop(self.elements)[1]
