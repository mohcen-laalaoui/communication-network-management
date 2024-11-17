import networkx as nx
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk
from tools.dijekstra import dijkstra
from tools.bellman_ford import bellman_ford
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

def visualize_network(G, title="Network Graph"):
    pos = nx.spring_layout(G)
    plt.figure(figsize=(10, 7))
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=15)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.title(title)
    plt.show()

def simulate_failure(G, edge):
    if G.has_edge(*edge):
        G.remove_edge(*edge)
        print(f"Simulated failure: Removed edge {edge}")
    else:
        print(f"Edge {edge} does not exist in the network.")
    visualize_network(G, title="Network After Edge Removal")

class NetworkSimulatorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Network Simulation")
        self.master.geometry("600x500")
        self.master.config(bg="#ADD8E6")
        self.G = create_network()
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.master, text="Network Communication Simulator", font=("Segoe UI", 18, "bold"), bg="#ADD8E6", fg="black")
        self.label.pack(pady=30)
        self.btn_visualize = ttk.Button(self.master, text="Visualize Network", style="Modern.TButton", command=self.visualize_network)
        self.btn_visualize.pack(pady=15, fill='x', padx=80)
        self.btn_dijkstra = ttk.Button(self.master, text="Run Dijkstra (1 to 5)", style="Modern.TButton", command=self.run_dijkstra)
        self.btn_dijkstra.pack(pady=15, fill='x', padx=80)
        self.btn_bellman_ford = ttk.Button(self.master, text="Run Bellman-Ford (1 to 5)", style="Modern.TButton", command=self.run_bellman_ford)
        self.btn_bellman_ford.pack(pady=15, fill='x', padx=80)
        self.btn_failure = ttk.Button(self.master, text="Simulate Failure (2 to 4)", style="Modern.TButton", command=self.simulate_failure)
        self.btn_failure.pack(pady=15, fill='x', padx=80)
        self.btn_variable_weights = ttk.Button(self.master, text="Simulate Variable Weights", style="Modern.TButton", command=self.simulate_variable_weights)
        self.btn_variable_weights.pack(pady=15, fill='x', padx=80)
        self.style = ttk.Style()
        self.style.configure("Modern.TButton", font=("Segoe UI", 14), padding=10, relief="flat", background="#007BFF", foreground="black")
        self.style.map("Modern.TButton", background=[('active', '#0056b3')])

    def visualize_network(self):
        visualize_network(self.G)

    def run_dijkstra(self):
        result = dijkstra(self.G, source=1, target=5)
        print(result)

    def run_bellman_ford(self):
        updates, self.G = bellman_ford(self.G, edges=[(1, 2), (3, 4), (4, 5)])
        for update in updates:
            print(update)

    def simulate_failure(self):
        simulate_failure(self.G, edge=(2, 4))

    def simulate_variable_weights(self):
        updates, self.G = bellman_ford(self.G, edges=[(1, 2), (3, 4), (4, 5)])
        for update in updates:
            print(update)

if __name__ == "__main__":
    root = tk.Tk()
    app = NetworkSimulatorApp(master=root)
    root.mainloop()
