class HamiltonianCycle:
    def __init__(self, graph):
        self.graph = graph
        self.num_vertices = len(graph)
        self.path = [-1] * self.num_vertices

    def is_safe(self, v, pos):
        if self.graph[self.path[pos - 1]][v] == 0:
            return False

        for vertex in self.path:
            if vertex == v:
                return False

        return True

    def solve_util(self, pos):
        if pos == self.num_vertices:
            return self.graph[self.path[pos - 1]][self.path[0]] == 1

        for v in range(1, self.num_vertices):
            if self.is_safe(v, pos):
                self.path[pos] = v
                if self.solve_util(pos + 1):
                    return True
                self.path[pos] = -1

        return False

    def find_cycle(self):
        self.path[0] = 0
        if not self.solve_util(1):
            return None
        return self.path + [self.path[0]]

graph_matrix = [
    [0, 1, 0, 1, 0],
    [1, 0, 1, 1, 1],
    [0, 1, 0, 0, 1],
    [1, 1, 0, 0, 1],
    [0, 1, 1, 1, 0]
]

hc = HamiltonianCycle(graph_matrix)
result = hc.find_cycle()
print(result)
