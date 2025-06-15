import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

# Membuat graph berarah dan berbobot
G = nx.DiGraph()

# Menambahkan node (representasi peta kota)
nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
G.add_nodes_from(nodes)

# Menambahkan edge dan bobot (jarak antar simpul)
edges = [
    ('A', 'B', 4), ('A', 'C', 2), 
    ('B', 'D', 5), ('C', 'B', 1), ('C', 'D', 8), 
    ('D', 'E', 6), ('E', 'F', 3), 
    ('F', 'G', 2), ('G', 'H', 1), 
    ('H', 'E', 4)
]
G.add_weighted_edges_from(edges)

# Visualisasi graf
pos = nx.spring_layout(G, seed=42)
plt.figure(figsize=(10, 6))
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=1200, font_size=14)
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.title("Graf Peta Kota dengan 8 Node")
plt.show()

# BFS
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    result = []

    while queue:
        node = queue.popleft()
        if node not in visited:
            result.append(node)
            visited.add(node)
            queue.extend(set(graph.neighbors(node)) - visited)
    return result

# DFS
def dfs(graph, start, visited=None, result=None):
    if visited is None:
        visited = set()
        result = []
    visited.add(start)
    result.append(start)
    for neighbor in graph.neighbors(start):
        if neighbor not in visited:
            dfs(graph, neighbor, visited, result)
    return result

# Menjalankan BFS dan DFS dari node 'A'
print("BFS dari A:", bfs(G, 'A'))
print("DFS dari A:", dfs(G, 'A'))

# Dijkstra
dijkstra_path = nx.dijkstra_path(G, 'A', 'H', weight='weight')
dijkstra_distance = nx.dijkstra_path_length(G, 'A', 'H', weight='weight')
print("\nDijkstra: Jalur A ke H =", dijkstra_path, "dengan jarak =", dijkstra_distance)

# Bellman-Ford
bellman_path = nx.bellman_ford_path(G, 'A', 'H', weight='weight')
bellman_distance = nx.bellman_ford_path_length(G, 'A', 'H', weight='weight')
print("Bellman-Ford: Jalur A ke H =", bellman_path, "dengan jarak =", bellman_distance)
