import random

def bellman_ford(G, edges):
    updates = []

    for edge in edges:
        if G.has_edge(*edge):
            new_weight = random.randint(1, 15)  
            G[edge[0]][edge[1]]['weight'] = new_weight
            updates.append(f"Updated weight for edge {edge}: {new_weight}")

    return updates, G
