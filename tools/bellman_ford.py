import sys
import time

def bellman_ford(graph, start_node):

    start_time = time.time()
    
    nodes = set(node for edge in graph for node in edge[:2])  # Get all unique nodes
    distances = {node: sys.maxsize for node in nodes}
    distances[start_node] = 0
    
    predecessors = {}

    for _ in range(len(nodes) - 1):
        for source, destination, weight in graph:
            if distances[source] != sys.maxsize and distances[source] + weight < distances[destination]:
                distances[destination] = distances[source] + weight
                predecessors[destination] = source

    has_negative_cycle = False
    for source, destination, weight in graph:
        if distances[source] != sys.maxsize and distances[source] + weight < distances[destination]:
            has_negative_cycle = True
            break

    end_time = time.time()
    response_time = end_time - start_time

    return distances, predecessors, response_time, has_negative_cycle

if __name__ == "__main__":

    graph = [
        (1, 2, 4),
        (1, 3, 2),
        (2, 3, 5),
        (2, 4, 10),
        (3, 4, 3),
        (4, 5, 7),
        (3, 5, 8),
        (5, 1, -15)  
    ]

    start_node = 1
    distances, predecessors, response_time, has_negative_cycle = bellman_ford(graph, start_node)

    if has_negative_cycle:
        print("The graph contains a negative weight cycle.")
    else:
        print("Shortest paths from node", start_node, "to all other nodes:")
        for node, distance in distances.items():
            print(f"Node {node}: {distance if distance != sys.maxsize else 'Unreachable'}")

        print(f"Response time: {response_time:.6f} seconds")
