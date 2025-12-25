import heapq

def dijkstra(graph, start):

    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0

    heap = [(0, start)]

    while heap:
        current_distance, current_vertex = heapq.heappop(heap)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))

    return distances


graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'C': 1, 'D': 5},
    'C': {'A': 2, 'B': 1, 'D': 8, 'E': 10},
    'D': {'B': 5, 'C': 8, 'E': 2},
    'E': {'C': 10, 'D': 2}
}

start_vertex = 'A'
shortest_paths = dijkstra(graph, start_vertex)

print(f"Найкоротші шляхи від вершини {start_vertex}:")
for vertex, distance in shortest_paths.items():
    print(f"{vertex}: {distance}")
