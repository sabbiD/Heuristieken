import sys
import random
from helpers import neighbour_set

def dfs_recursive(graph, vertex, path=[]):

	for key in graph:
		neighb_station = neighbour_set(graph, vertex)

		if len(neighb_station) == 0:

			key.radio = 1

	radios = [1, 2, 3, 4, 5, 6, 7]

	path += [vertex] 

	neighb_station = neighbour_set(graph, vertex)

	options = [1, 2, 3, 4, 5, 6, 7]
	
	if vertex.radio is not 0:

		options.remove(vertex.radio)

	for i in range(len(radios)):

		if radios[i] in neighb_station:
			options.remove(radios[i])
	
		vertex.radio = min(options)

	for neighbour in graph[vertex]:	
		
		# # ga naar vorige in de lijst ipv naar buur  
		# # stop als radio niet kan! hou lijst bij met buur radios
		if neighbour not in path:
			neighb_station = []
			path = dfs_recursive(graph, neighbour, path)

	return path 