import time
import heapq

def dijkstra(G, source, target):
    """Find the shortest path using Dijkstra's algorithm manually."""
    start_time = time.time()
    
    distances = {node: float('inf') for node in G.nodes}
    previous_nodes = {node: None for node in G.nodes}
    distances[source] = 0

    priority_queue = [(0, source)]
    visited = set()

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_node in visited:
            continue

        visited.add(current_node)

        if current_node == target:
            path = []
            while previous_nodes[current_node] is not None:
                path.append(current_node)
                current_node = previous_nodes[current_node]
            path.append(source)
            path.reverse()
            end_time = time.time()
            return f"Shortest path using Dijkstra from {source} to {target}: {path}", \
                   f"Total path cost: {distances[target]}", \
                   f"Response time: {end_time - start_time:.6f} seconds"

        for neighbor, weight in G[current_node].items():
            if neighbor not in visited:
                new_distance = current_distance + weight['weight']
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    previous_nodes[neighbor] = current_node
                    heapq.heappush(priority_queue, (new_distance, neighbor))

    return f"No path found from {source} to {target}."
