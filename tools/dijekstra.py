import sys
import time

def dijkstra(graph, start_node):
    start_time = time.time()
    
    shortest_paths = {node: sys.maxsize for node in graph}
    shortest_paths[start_node] = 0
    
    unvisited_nodes = set(graph.keys())
    previous_nodes = {}

    while unvisited_nodes:

        current_node = min(unvisited_nodes, key=lambda node: shortest_paths[node])

        if shortest_paths[current_node] == sys.maxsize:
            break

        for neighbor, weight in graph[current_node].items():
            if neighbor in unvisited_nodes:
                new_path = shortest_paths[current_node] + weight
                if new_path < shortest_paths[neighbor]:
                    shortest_paths[neighbor] = new_path
                    previous_nodes[neighbor] = current_node

        unvisited_nodes.remove(current_node)

    end_time = time.time()
    response_time = end_time - start_time

    return shortest_paths, previous_nodes, response_time

if __name__ == "__main__":

    graph = {
        1: {2: 4, 3: 2},
        2: {3: 5, 4: 10},
        3: {4: 3, 5: 8},
        4: {5: 7},
        5: {}
    }

    start_node = 1
    shortest_paths, previous_nodes, response_time = dijkstra(graph, start_node)

    print("Shortest paths from node", start_node, "to all other nodes:")
    for node, distance in shortest_paths.items():
        print(f"Node {node}: {distance}")

    print(f"Response time: {response_time:.6f} seconds")
