import networkx as nx
import matplotlib.pyplot as plt

# Create an empty graph
G = nx.Graph()

# Add nodes for characters
G.add_nodes_from([
    "Harry Potter", "Ron Weasley", "Hermione Granger", "Hagrid",
    "Uncle Vernon", "Aunt Petunia", "Dudley", "Professor Snape",
    "Professor McGonagall", "Percy Weasley", "Hedwig"
])

# Add edges based on closeness in the text
G.add_edges_from([
    ("Harry Potter", "Ron Weasley"),
    ("Harry Potter", "Hermione Granger"),
    ("Harry Potter", "Hagrid"),
    ("Harry Potter", "Uncle Vernon"),
    ("Harry Potter", "Aunt Petunia"),
    ("Harry Potter", "Dudley"),
    ("Harry Potter", "Professor Snape"),
    ("Harry Potter", "Professor McGonagall"),
    ("Harry Potter", "Percy Weasley"),
    ("Harry Potter", "Hedwig"),
])

# Define edge weights based on closeness (adjust as needed)
edge_weights = {
    ("Harry Potter", "Ron Weasley"): 5,
    ("Harry Potter", "Hermione Granger"): 5,
    ("Harry Potter", "Hagrid"): 4,
    ("Harry Potter", "Uncle Vernon"): 1,
    ("Harry Potter", "Aunt Petunia"): 1,
    ("Harry Potter", "Dudley"): 1,
    ("Harry Potter", "Professor Snape"): 1,
    ("Harry Potter", "Professor McGonagall"): 1,
    ("Harry Potter", "Percy Weasley"): 1,
    ("Harry Potter", "Hedwig"): 4,
}

# Set edge weights
for u, v in edge_weights:
    G[u][v]['weight'] = edge_weights[(u, v)]

# Draw the network
pos = nx.spring_layout(G)  # Use spring layout for visualization
nx.draw(G, pos, with_labels=True, node_size=700, node_color="lightblue", font_size=8)
nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, 'weight'))

plt.title("Character Network in Harry Potter Excerpt")
plt.show()