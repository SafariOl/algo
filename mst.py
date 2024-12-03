import heapq

def dijkstra(graph, start, end):
    heap = [(0, start)]  # (cost, node)
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    shortest_path = {}

    while heap:
        current_distance, current_node = heapq.heappop(heap)

        if current_node == end:
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = shortest_path.get(current_node, None)
            return current_distance, path[::-1]

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                shortest_path[neighbor] = current_node
                heapq.heappush(heap, (distance, neighbor))

    return float('infinity'), []

# Визначення графа
graph = {
    1: {2: 4, 3: 5, 4: 4, 5: 2},
    2: {6: 3, 7: 4},
    3: {6: 1, 7: 1, 8: 3},
    4: {6: 4, 7: 5, 8: 5},
    5: {7: 2, 8: 5},
    6: {9: 3, 10: 4, 12: 6},
    7: {9: 6, 10: 7, 11: 7},
    8: {10: 4, 11: 4, 12: 4},
    9: {13: 7, 15: 6},
    10: {13: 4, 14: 7},
    11: {14: 8, 15: 7},
    12: {13: 9, 15: 10},
    13: {16: 2},
    14: {16: 3},
    15: {16: 2},
    16: {}
}

# Пошук найменшого шляху з пункту 1 до пункту 16
distance, path = dijkstra(graph, 1, 16)
print(f"Найменша відстань: {distance}")
print(f"Шлях: {' -> '.join(map(str, path))}")
