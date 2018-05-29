""" Sebile search 2.0
	
	A recursive depth-first search algorithm that uses a limit dependent on neighboursize of region to determine optimal costs.

"""

import sys
import random
from helpers import neighbour_set
from country import country 
from data_structure import data_structure
from helpers import reset


# Cost scheme 2 is used because preliminary results showed that this scheme 
# returns lowest costs
costs_2 = {1: 19, 2: 20, 3: 21, 4: 23, 5: 36, 6: 37, 7: 38} 


def dfs_recursive(graph, vertex, path):

	# All stations
	radios = [1, 2, 3, 4, 5, 6, 7]
	
	# If region has no neighbours, set to 1 because depth-first will never reach this key
	for key in graph:
		neighb_station = neighbour_set(graph, key)

		if len(neighb_station) == 0:

			key.radio = 1

	# Mark current region as visited
	path += [vertex] 

	# Get neighbour stations of current region
	neighb_station = neighbour_set(graph, vertex)


	options = [1, 2, 3, 4, 5, 6, 7]
	
	# Remove current value of region station
	if vertex.radio is not 0:

		options.remove(vertex.radio)

	
	# Look through stations and remove from options 
	# if that is the station of a neighbour
	for i in range(len(radios)):
		
		if radios[i] in neighb_station:
			
			if radios[i] in options:
				
				options.remove(radios[i])
	
	# Initialize limit 
	limit = 0
	
	# Set limit according to amount of neighbours of current region
	for i in range(len(graph[vertex])):

		# If region has more neighbours than types of stations (7) 
		if i > 6:

			break

		# Add cost of station to limit
		else:

			limit += costs_2[i + 1]

	if len(graph[vertex]) > 0:
		
		# Determine limit by dividing it by amount of neighbours
		limit = limit / len(graph[vertex])


		# Check if current option for station is higher than limit
		# if so try again for neighbour of region
		if costs_2[min(options)] > limit:
			
			other_neighbour = random.choice(graph[vertex])
			
			if other_neighbour not in path:

				# Empty neighbour list for next region
				neighb_station = []

				path = dfs_recursive(graph, other_neighbour, path)

	else:
		vertex.radio = 1

	# Assign cheapest station available to current region
	vertex.radio = min(options)

	# Check for neighbours of current region if they are visited 
	# if not visited try that region
	for neighbour in graph[vertex]:	
		  
		if neighbour not in path:

			# Empty neighbour list for next region
			neighb_station = []

			path = dfs_recursive(graph, neighbour, path)
			
	return path 


# Function used to reset data when multiple iterations of depth-first is run
def depth_limit(regions, order):

	# Reset data for iterations
	reset(regions)

	dfs_recursive(regions, order[0] , path=[])
	
	return regions

