import sys

def dfs_recursive(graph, vertex, path=[]):
	path += [vertex] 

	for neighbour in graph[vertex]:

		if neighbour.radio == vertex.radio:
			vertex.radio += 1

		# if vertex.radio == 5:
		# 	vertex.radio = 2
		# 	path = dfs_recursive(graph, neighbour, path)

		if neighbour not in path:
			path = dfs_recursive(graph, neighbour, path)

	return path 

