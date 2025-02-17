# Communication Network Management

## Overview
This project simulates network communication using **Dijkstra's** and **Bellman-Ford** algorithms to find the shortest path between nodes in a directed weighted graph. The application is built using **Python**, **NetworkX**, and **Tkinter**, providing a graphical interface to visualize network graphs and analyze their properties.

## Features
- **Graph Visualization**: Displays the network structure with nodes and edges.
- **Dijkstra's Algorithm**: Computes the shortest path for graphs without negative weights.
- **Bellman-Ford Algorithm**: Handles graphs with negative weights, detecting negative weight cycles.
- **QoS Metrics Calculation**: Evaluates total nodes, total edges, and average edge weight.
- **Edge Weight Randomization**: Updates edge weights randomly for dynamic simulations.

## Technologies Used
- **Python 3.x**
- **NetworkX** (for graph representation and algorithms)
- **Matplotlib** (for visualization)
- **Tkinter** (for GUI)
- **Random** (for weight generation)

## Installation
Ensure you have Python installed, then install dependencies:
```sh
pip install networkx matplotlib
```

## Usage
1. Clone the repository:
   ```sh
   git clone https://github.com/mohcen-laalaoui/communication-network-management.git
   cd communication-network-management
   ```
2. Run the application:
   ```sh
   python main.py
   ```

## GUI Features
- **Visualize Network**: Displays the initial graph.
- **Run Dijkstra**: Computes and highlights the shortest path (for graphs without negative weights).
- **Run Bellman-Ford**: Computes shortest paths (handles negative weights and detects negative cycles).
- **Calculate QoS Metrics**: Displays total nodes, edges, and average edge weight.
- **Randomize Edge Weights**: Assigns random weights to edges for different scenarios.

## Code Structure
- `create_network()`: Initializes the graph with predefined edges and weights.
- `dijkstra_algorithm(G, source, target)`: Implements Dijkstra's shortest path algorithm.
- `bellman_ford_algorithm(G, source, target)`: Implements Bellman-Ford algorithm.
- `visualize_network(G, title)`: Draws the network graph.
- `visualize_shortest_path(G, path, title)`: Highlights the computed shortest path.
- `calculate_qos_metrics(G)`: Computes network statistics.
- `randomize_weights(G)`: Assigns random weights to edges.
- **`NetworkSimulatorApp` Class**: Implements the Tkinter-based GUI.

## Example Output
- **Initial Network Graph**
  ![Graph](example_graph.png)
- **Shortest Path Visualization**
  ![Shortest Path](shortest_path.png)

## Contribution
Feel free to fork the repository, submit issues, and create pull requests!

---
Developed by **Mohcen Laalaoui**

