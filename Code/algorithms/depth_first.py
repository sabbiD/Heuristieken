""" Depth-first
	
	A recursive depth-first search algorithm used for map coloring. 
	The depth_first function below it is used to run iterations of algorithms.
	
"""

import sys
import random
from helpers import neighbour_set
from helpers import reset

def dfs_recursive(graph, vertex, path):

	# List with all stations
	radios = [1, 2, 3, 4, 5, 6, 7]

	# If region has no neighbours, set to 1 because depth-first will never reach this key
	for region in graph:

		neighb_station = neighbour_set(graph, region)

		if len(neighb_station) == 0:

			region.radio = 1

	# Mark current region as visited
	path += [vertex] 

	# Get neighbours of current region
	neighb_station = neighbour_set(graph, vertex)

	# List that contains available stations for current region
	options = [1, 2, 3, 4, 5, 6, 7]
	
	# Remove current value of region station
	if vertex.radio is not 0:

		options.remove(vertex.radio)

	# Look through stations and remove from options 
	# if that is the station of a neighbour
	for i in range(len(radios)):

		if radios[i] in neighb_station:

			options.remove(radios[i])
	
	# Set station of current region to lowest available option
	vertex.radio = min(options)

	# Check for neighbours of current region, if they are not marked 
	# start function again with that region
	for neighbour in graph[vertex]:	
		
		if neighbour not in path:

			# Empty neighbour set for new region
			neighb_station = []
			path = dfs_recursive(graph, neighbour, path)
			
	# Return visited regions
	return path 



# Function used to reset data when multiple iterations of depth-first is run
def depth_first(regions, order):

	# Reset data for iterations
	reset(regions)

	# Call depth-first function
	dfs_recursive(regions, order, path=[])

	return regions