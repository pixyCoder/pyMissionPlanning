
import matplotlib.pyplot as plt
import networkx as nx


def plot_weighted_graph(N, adjacency_list, outputFilename, save):			
	G = nx.Graph()

	for ii in range(0, N):
		G.add_edge(adjacency_list[ii][1], adjacency_list[ii][2], 
			weight=adjacency_list[ii][0])

	elarge = [(u, v) for (u, v, d) in G.edges(data=True) if d["weight"] > 0.5]
	esmall = [(u, v) for (u, v, d) in G.edges(data=True) if d["weight"] <= 0.5]

	pos = nx.spring_layout(G, seed=7)  # positions for all nodes - seed for reproducibility

	# nodes
	nx.draw_networkx_nodes(G, pos, node_size=700)

	# edges
	nx.draw_networkx_edges(G, pos, edgelist=elarge, width=6)
	nx.draw_networkx_edges(
    		G, pos, edgelist=esmall, width=6, alpha=0.5, edge_color="b", style="dashed"
)

	# node labels
	nx.draw_networkx_labels(G, pos, font_size=20, font_family="sans-serif")
	# edge weight labels
	edge_labels = nx.get_edge_attributes(G, "weight")
	nx.draw_networkx_edge_labels(G, pos, edge_labels)

	ax = plt.gca()
	ax.margins(0.08)
	plt.axis("off")
	plt.tight_layout()
	if (save == 1):
		plt.savefig(outputFilename)
	else:
		plt.show()


if __name__ == '__main__':
	outputFilename = "builtInTestGraph.png"
	N = 6
	adjacency_list_str = [[60, "a", "b"],
				[20, "a", "c"],
				[10, "c", "d"],
				[70, "c", "e"],
				[90, "c", "f"],
				[30, "a", "d"]]
	adjacency_list_int = [[60, 0, 1],
				[20, 0, 2],
				[10, 2, 3],
				[70, 2, 4],
				[90, 2, 5],
				[30, 0, 3]]

	save = 1
	
	adjacency_list = adjacency_list_str
	node_datatype = isinstance(adjacency_list[0][1], str)
	if (node_datatype == False):
		for ii in range(0, N):
			adjacency_list[ii][1] = str(adjacency_list[ii][1])
			adjacency_list[ii][2] = str(adjacency_list[ii][2])	

	plot_weighted_graph(N, adjacency_list, outputFilename, save)
