from kgbUA import final
import sys


adjacency_matrix = final


# copy of dict with all regions
new_final = dict(final)

# stack for regions leftover
stack = []
for key in list(new_final):

	if len(new_final[key]) < 5:
		stack += [key]
		del new_final[key]

#now only contains regions >5 neighbours
#print(new_final)

def dfs_recursive(graph, vertex, path=[]):
	path += [vertex] 

	for neighbour in graph[vertex]:

		if neighbour.radio == vertex.radio:
			vertex.radio += 1

		if vertex.radio == 5:
			vertex.radio = 2
			path = dfs_recursive(graph, neighbour, path)

		if neighbour not in path:
			path = dfs_recursive(graph, neighbour, path)

	return path 

dfs_recursive(adjacency_matrix, list(new_final.keys())[0])
#print(final)
dfs_recursive(adjacency_matrix, list(final.keys())[0])


#print(final)