# Study Group Messaging Network Analysis

This project visualises a social network of 12 study group members.  
**Nodes** = people. **Edges** = messaging interactions. **Edge weight** = number of messages.

## How to run locally
1. Install Python 3.14.5
2. Install packages: `pip install pandas networkx pyvis`
3. Run `python visualize_plotly.py` to generate `network.html`
4. Open `index.html` in your browser

## What the visualisation shows
- **Node size** = number of connections (degree)
- **Node colour** = role: Leader (red), Contributor (teal), Lurker (yellow)
- **Edge thickness** = message count
- **Layout** = force-directed (nodes with strong ties cluster)

## Key insight
The Leader (red) has the highest degree and betweenness centrality – acting as both the central hub and the bridge that connects Contributors to Lurkers. Without the Leader, the network would split into isolated clusters.

## Live demo (bonus)
[View the interactive network]( https://kokeng1234eng-prog.github.io/social_network_assignment/)  
*(replace with your actual GitHub Pages link after deploying)*
