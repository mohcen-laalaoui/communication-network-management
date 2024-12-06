import networkx as nx
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk
import random

def create_network():
    G = nx.DiGraph()
    G.add_weighted_edges_from([
        (1, 2, 4),
        (1, 3, 2),
        (2, 3, 5),
        (2, 4, 10),
        (3, 4, 3),
        (4, 5, 7),
        (3, 5, 8)
    ])
    return G

def randomize_weights(G):
    for u, v in G.edges():
        G[u][v]['weight'] = random.randint(-10, 20)
    return G

def calculate_qos_metrics(G):
    total_edges = G.number_of_edges()
    total_nodes = G.number_of_nodes()
    avg_weight = sum(nx.get_edge_attributes(G, 'weight').values()) / total_edges
    metrics = {
        "Total Nodes": total_nodes,
        "Total Edges": total_edges,
        "Average Edge Weight": round(avg_weight, 2),
    }
    return metrics

def visualize_network(G, title="Network Graph"):
    pos = nx.spring_layout(G)
    plt.figure(figsize=(10, 7))
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=15)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.title(title)
    plt.show()

def visualize_shortest_path(G, path, title="Shortest Path Highlighted"):
    pos = nx.spring_layout(G)
    plt.figure(figsize=(10, 7))
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=15)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    path_edges = list(zip(path[:-1], path[1:]))
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2.5)

    plt.title(title)
    plt.show()

def dijkstra_algorithm(G, source, target):
    if any(data['weight'] < 0 for _, _, data in G.edges(data=True)):
        raise ValueError("Graph contains negative weight edges. Use Bellman-Ford instead.")
    
    nodes = list(G.nodes())
    distances = {node: float('inf') for node in nodes}
    distances[source] = 0
    previous_nodes = {node: None for node in nodes}
    unvisited = set(nodes)

    while unvisited:
        current_node = min(unvisited, key=lambda node: distances[node])
        unvisited.remove(current_node)

        if distances[current_node] == float('inf'):
            break

        for neighbor in G.neighbors(current_node):
            weight = G[current_node][neighbor]['weight']
            alt = distances[current_node] + weight
            if alt < distances[neighbor]:
                distances[neighbor] = alt
                previous_nodes[neighbor] = current_node

        if current_node == target:
            break

    path = []
    current = target
    while current:
        path.insert(0, current)
        current = previous_nodes[current]

    return path, distances[target]

def bellman_ford_algorithm(G, source, target):
    nodes = list(G.nodes())
    distances = {node: float('inf') for node in nodes}
    distances[source] = 0
    previous_nodes = {node: None for node in nodes}

    for _ in range(len(nodes) - 1):
        for u, v, data in G.edges(data=True):
            weight = data['weight']
            if distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight
                previous_nodes[v] = u

    for u, v, data in G.edges(data=True):
        weight = data['weight']
        if distances[u] + weight < distances[v]:
            raise ValueError("Graph contains a negative weight cycle")

    path = []
    current = target
    while current:
        path.insert(0, current)
        current = previous_nodes[current]

    return path, distances[target]

class NetworkSimulatorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Network Simulation")
        self.master.geometry("600x800")
        self.master.config(bg="#ADD8E6")

        self.G = create_network()
        self.result_label = None

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.master, text="Network Communication Simulator", font=("Segoe UI", 18, "bold"),
                              bg="#ADD8E6", fg="black")
        self.label.pack(pady=30)

        self.source_var = tk.IntVar(value=1)
        self.target_var = tk.IntVar(value=5)

        source_label = tk.Label(self.master, text="Source Node:", font=("Segoe UI", 14), bg="#ADD8E6")
        source_label.pack(pady=5)
        self.source_entry = ttk.Entry(self.master, textvariable=self.source_var, font=("Segoe UI", 14))
        self.source_entry.pack(pady=5)

        target_label = tk.Label(self.master, text="Target Node:", font=("Segoe UI", 14), bg="#ADD8E6")
        target_label.pack(pady=5)
        self.target_entry = ttk.Entry(self.master, textvariable=self.target_var, font=("Segoe UI", 14))
        self.target_entry.pack(pady=5)

        style = ttk.Style()
        style.configure("Highlighted.TButton", background="yellow", foreground="black")

        self.btn_visualize = ttk.Button(self.master, text="Visualize Network", command=self.visualize_network)
        self.btn_visualize.pack(pady=15, fill='x', padx=80)

        self.btn_dijkstra = ttk.Button(self.master, text="Run Dijkstra", command=self.run_dijkstra)
        self.btn_dijkstra.pack(pady=15, fill='x', padx=80)

        self.btn_bellman_ford = ttk.Button(self.master, text="Run Bellman-Ford", command=self.run_bellman_ford)
        self.btn_bellman_ford.pack(pady=15, fill='x', padx=80)

        self.qos_button = ttk.Button(self.master, text="Calculate QoS Metrics", command=self.view_qos_metrics)
        self.qos_button.pack(pady=15, fill='x', padx=80)

        self.randomize_button = ttk.Button(self.master, text="Randomize Edge Weights", command=self.randomize_edge_weights)
        self.randomize_button.pack(pady=15, fill='x', padx=80)

        self.result_label = tk.Label(self.master, text="", font=("Segoe UI", 12), bg="#ADD8E6", fg="black", justify="left")
        self.result_label.pack(pady=10)

    def visualize_network(self):
        visualize_network(self.G)

    def run_dijkstra(self):
        source = self.source_var.get()
        target = self.target_var.get()
        try:
            path, cost = dijkstra_algorithm(self.G, source, target)
            self.result_label.config(text=f"Path: {path}\nCost: {cost}")
            visualize_shortest_path(self.G, path)
        except ValueError as e:
            self.result_label.config(text=f"Warning: {str(e)}")
            self.btn_bellman_ford.config(style="Highlighted.TButton")

    def run_bellman_ford(self):
        source = self.source_var.get()
        target = self.target_var.get()
        try:
            path, cost = bellman_ford_algorithm(self.G, source, target)
            self.result_label.config(text=f"Path: {path}\nCost: {cost}")
            visualize_shortest_path(self.G, path, title="Bellman-Ford Shortest Path")
        except Exception as e:
            self.result_label.config(text=f"Error: {str(e)}")

    def view_qos_metrics(self):
        metrics = calculate_qos_metrics(self.G)
        result_text = "\n".join([f"{k}: {v}" for k, v in metrics.items()])
        self.result_label.config(text=result_text)

    def randomize_edge_weights(self):
        self.G = randomize_weights(self.G)
        self.result_label.config(text="Edge weights randomized.")
        visualize_network(self.G, title="Network with Randomized Weights")

if __name__ == "__main__":
    root = tk.Tk()
    app = NetworkSimulatorApp(master=root)
    root.mainloop()