import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

# Membuat graf berarah berbobot
G = nx.DiGraph()

# Tambahkan simpul
nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
G.add_nodes_from(nodes)

# Tambahkan sisi dan bobotnya
edges = [
    ('A', 'B', 4), ('A', 'C', 2), 
    ('C', 'B', 1), ('B', 'D', 5), ('C', 'D', 8),
    ('D', 'E', 6), ('E', 'F', 3), 
    ('F', 'G', 2), ('G', 'H', 1), 
    ('H', 'E', 4)
]
G.add_weighted_edges_from(edges)

# Hitung jalur terpendek dari A ke H menggunakan Dijkstra
shortest_path = nx.dijkstra_path(G, 'A', 'H', weight='weight')

# Buat list edge dalam jalur terpendek
path_edges = list(zip(shortest_path, shortest_path[1:]))

# Layout node
pos = nx.spring_layout(G, seed=42)

# Gambar semua edge dengan warna default (abu-abu)
nx.draw_networkx_edges(G, pos, edgelist=G.edges(), edge_color='gray', width=2)

# Gambar edge pada jalur terpendek dengan warna merah
nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=3)

# Gambar node dan label
nx.draw_networkx_nodes(G, pos, node_color='skyblue', node_size=1200)
nx.draw_networkx_labels(G, pos, font_size=14)

# Tambahkan label bobot edge
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

# Judul
plt.title("Graf Peta Kota dengan Jalur Terpendek A ke H (Dijkstra)", fontsize=14)
plt.axis('off')
plt.show()
