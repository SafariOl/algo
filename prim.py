import heapq
from collections import defaultdict

class Graph:
    def __init__(self):
        self.edges = defaultdict(list)

    def add_edge(self, u, v, weight):
        self.edges[u].append((weight, v))
        self.edges[v].append((weight, u))

    def prim(self, start):
        mst = []
        visited = set()
        min_heap = [(0, start)]
        step = 0
        
        while min_heap:
            weight, u = heapq.heappop(min_heap)
            if u in visited:
                continue

            visited.add(u)
            if step > 0:
                mst.append((weight, u))
                if step == 5:
                    return weight
            step += 1

            for next_weight, v in self.edges[u]:
                if v not in visited:
                    heapq.heappush(min_heap, (next_weight, v))

        return None

# Побудова графа з малюнка
graph = Graph()
graph.add_edge('A', 'B', 4)
graph.add_edge('A', 'C', 1)
graph.add_edge('A', 'F', 3)
graph.add_edge('B', 'E', 2)
graph.add_edge('B', 'D', 11)
graph.add_edge('C', 'D', 7)
graph.add_edge('D', 'G', 10)
graph.add_edge('E', 'F', 4)
graph.add_edge('F', 'N', 9)
graph.add_edge('G', 'E', 10)
graph.add_edge('C', 'N', 10)
graph.add_edge('G', 'N', 8)

# Виконання алгоритму Пріма, починаючи з вершини A
fifth_step_weight = graph.prim('A')
print(fifth_step_weight)