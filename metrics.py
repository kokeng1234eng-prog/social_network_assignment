import pandas as pd
import networkx as nx

# Load again (or you can reuse the graph from Task 2)
edges = pd.read_csv('edges.csv')
nodes = pd.read_csv('nodes.csv')
edges = edges.drop_duplicates(subset=['source', 'target'])
edges = edges[edges['source'] != edges['target']]
edges['weight'] = edges['weight'].fillna(1)
G = nx.from_pandas_edgelist(edges, 'source', 'target', edge_attr=['weight','type'])
for _, row in nodes.iterrows():
    G.nodes[row['node']]['group'] = row['group']

# Compute metrics
degree = dict(G.degree())
deg_cent = nx.degree_centrality(G)
between_cent = nx.betweenness_centrality(G)
density = nx.density(G)

# Top 3 by degree centrality
top_nodes = sorted(deg_cent, key=deg_cent.get, reverse=True)[:3]

print("=== NETWORK METRICS ===")
print(f"Density: {density:.3f}\n")
print("Node | Degree | Degree Centrality | Betweenness Centrality")
print("-" * 60)
for node in top_nodes:
    print(f"{node:5} | {degree[node]:6} | {deg_cent[node]:.3f}              | {between_cent[node]:.3f}")