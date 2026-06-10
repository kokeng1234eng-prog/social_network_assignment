import pandas as pd
import networkx as nx
import plotly.graph_objects as go

# Load data
edges = pd.read_csv('edges.csv')
nodes = pd.read_csv('nodes.csv')

# Clean
edges = edges.drop_duplicates(subset=['source', 'target'])
edges = edges[edges['source'] != edges['target']]
edges['weight'] = edges['weight'].fillna(1)

# Build graph
G = nx.from_pandas_edgelist(edges, 'source', 'target', edge_attr=['weight','type'])
for _, row in nodes.iterrows():
    G.nodes[row['node']]['group'] = row['group']

# Compute layout positions (spring layout)
pos = nx.spring_layout(G, seed=42, k=1.5)

# Create edge traces
edge_traces = []
for edge in G.edges(data=True):
    x0, y0 = pos[edge[0]]
    x1, y1 = pos[edge[1]]
    weight = edge[2].get('weight', 1)
    edge_traces.append(go.Scatter(
        x=[x0, x1, None], y=[y0, y1, None],
        line=dict(width=weight/5, color='#888'),
        hoverinfo='none',
        mode='lines'
    ))

# Create node trace
node_x = []
node_y = []
node_colors = []
node_sizes = []
node_text = []

color_map = {'Leader': 'red', 'Contributor': 'teal', 'Lurker': 'gold'}

for node in G.nodes():
    x, y = pos[node]
    node_x.append(x)
    node_y.append(y)
    deg = G.degree(node)
    node_sizes.append(deg * 8)
    group = G.nodes[node].get('group', 'Other')
    node_colors.append(color_map.get(group, 'grey'))
    node_text.append(f"{node}<br>Degree: {deg}<br>Group: {group}")

node_trace = go.Scatter(
    x=node_x, y=node_y,
    mode='markers+text',
    text=[n for n in G.nodes()],
    textposition="top center",
    hoverinfo='text',
    hovertext=node_text,
    marker=dict(size=node_sizes, color=node_colors, line=dict(width=1, color='darkgrey')),
    name=''
)

# Create figure
fig = go.Figure(data=edge_traces + [node_trace],
                layout=go.Layout(
                    title='Study Group Messaging Network<br><sub>Node size = degree, colour = role, edge thickness = message count</sub>',
                    showlegend=False,
                    hovermode='closest',
                    xaxis=dict(showgrid=False, zeroline=False, visible=False),
                    yaxis=dict(showgrid=False, zeroline=False, visible=False),
                    plot_bgcolor='white',
                    height=700
                ))

# Save as HTML
fig.write_html("network_plotly.html")
print("Saved as network_plotly.html – open in browser")