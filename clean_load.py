import pandas as pd
import networkx as nx

# Load the CSV files
edges = pd.read_csv('edges.csv')
nodes = pd.read_csv('nodes.csv')

# ---- Cleaning edges ----
print("Before cleaning:", len(edges), "edges")

# Remove duplicate rows (same source and target)
edges = edges.drop_duplicates(subset=['source', 'target'])

# Remove self-loops (source equals target)
edges = edges[edges['source'] != edges['target']]

# If any weight is missing, fill with 1
edges['weight'] = edges['weight'].fillna(1)

print("After cleaning:", len(edges), "edges")

# Create graph
G = nx.from_pandas_edgelist(edges, 'source', 'target', 
                            edge_attr=['weight', 'type'])

# Add node attributes (group)
for _, row in nodes.iterrows():
    G.nodes[row['node']]['group'] = row['group']

print(f"Final graph has {G.number_of_nodes()} nodes and {G.number_of_edges()} edges")