""" Sebile search 2.0
	
	A recursive depth-first search algorithm that uses a limit dependent on neighboursize of region to determine optimal costs.

"""
import sys
import random
from helpers import neighbour_set
from country import country 
from data_structure import data_structure
from helpers import reset

costs_2 = {1: 19, 2: 20, 3: 21, 4: 23, 5: 36, 6: 37, 7: 38} 

def dfs_recursive(graph, vertex, path):

	radios = [1, 2, 3, 4, 5, 6, 7]
	
	# If region has no neighbours, set to 1 because depth-first will never reach this key
	for key in graph:
		neighb_station = neighbour_set(graph, key)

		if len(neighb_station) == 0:

			key.radio = 1

	path += [vertex] 

	neighb_station = neighbour_set(graph, vertex)

	options = [1, 2, 3, 4, 5, 6, 7]
	
	if vertex.radio is not 0:

		options.remove(vertex.radio)

	for i in range(len(radios)):
		
		if radios[i] in neighb_station:
			
			options.remove(radios[i])
	
	limit = 0
	
	for i in range(len(graph[vertex])):

		if i > 6:

			break
		else:

			limit += costs_2[i + 1]

	limit = limit / len(graph[vertex])

	if costs_2[min(options)] > limit:
		
		other_neighbour = random.choice(graph[vertex])
		
		if other_neighbour not in path:
			neighb_station = []
			
			path = dfs_recursive(graph, other_neighbour, path)

	vertex.radio = min(options)

	for neighbour in graph[vertex]:	
		
		# ga naar vorige in de lijst ipv naar buur  
		if neighbour not in path:
			neighb_station = []
			path = dfs_recursive(graph, neighbour, path)
			
	return path 

def depth_limit(regions):

	reset(regions)

	new_regions = regions.copy()

	for region in new_regions:

		if len(new_regions[region]) < 5:

			del new_regions[region]


	dfs_recursive(regions, list(new_regions.keys())[0] , path=[])
	dfs_recursive(regions, list(regions.keys())[0], path=[])
	
	return regions

