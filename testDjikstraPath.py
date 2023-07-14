
import sys
import numpy as np
from heapq import heapify, heappush, heappop
import graph

# Inputs with adjacency list
# format [weight, srcNode, destNode]
Nn = 3
adjacency_list = [[2, 0, 1],
                        [4, 1, 2]]
filename = "testDjikstraPath.png"
source = 0
destination = 2


Ne = len(adjacency_list)
print('Number of edges : ', Ne)
saveFile = 1
distPath = {}

def djikstraPath(graph, src, dest):

	inf = sys.maxsize
	node_data = {0 : {'cost' : inf, 'pred' : []},
			1 : {'cost' : inf, 'pred' : []},
			2 : {'cost' : inf, 'pred' : []}}
				

	node_data[src]['cost'] = 0
	visited = []
	temp = src
	
	for i in range(0, Nn-1):
		if temp not in visited:
			visited.append(temp)
			min_heap = [] 
			for j in graph[temp]:
				if j not in visited:
					cost = node_data[temp]['cost'] + graph[temp][j]
					if (cost < node_data[j]['cost']):
						node_data[j]['cost'] = cost
						if (isinstance(temp, str) == False):
							node_data[j]['pred'] = node_data[temp]['pred'] + list(str(temp))
						else:
							node_data[j]['pred'] = node_data[temp]['pred'] + list(temp)
					heappush(min_heap, (node_data[j]['cost'], j))
		heapify(min_heap)
		print("Min heap, min : ", min_heap, '\t', min_heap[0][1])
		temp = min_heap[0][1]

	shortest_distance = node_data[dest]['cost']
	if (isinstance(dest, str) == False):
		shortest_path = node_data[dest]['pred'] + list(str(dest))
	else:
		shortest_path = node_data[dest]['pred'] + list(dest)


	
	distPath[str(source) + '<-->' + str(dest) + '  distance'] = shortest_distance
	distPath[str(source) + '<-->' + str(dest) + '  path'] = shortest_path
	
	return distPath


if __name__== '__main__':

	graph.plot_weighted_graph(Ne, adjacency_list, filename, saveFile)

	graph_computed = {}
	graph_computed[0] = {}
	graph_computed[1] = {}
	graph_computed[2] = {}

	print('Initial graph : ', graph_computed)

	for i in range(0, Ne):
		graph_computed[adjacency_list[i][1]][adjacency_list[i][2]] = adjacency_list[i][0] 
		graph_computed[adjacency_list[i][2]][adjacency_list[i][1]] = adjacency_list[i][0]

	print()
	print()
	print("Computed node distances")
	print(graph_computed)
	print()
	print()

	#for iSrc in range(0, Nn):
	#	for iDest in range(0, Nn):
	#		if (iSrc != iDest):
	#			distPathDict = djikstraPath(graph_computed, iSrc, iDest)

	distPathDict = djikstraPath(graph_computed, 0, 1)
	distPathDict = djikstraPath(graph_computed, 0, 2)


	print()
	print()
	print('Djikstra computation')
	print(distPathDict)
	print()
	print()
