""" Sebile search

	Attempt at depth-first search that is not a depth-first but does return valid results for graph coloring.

"""


adjacency_matrix = final_regions


# Copy of dict with all regions
new_final = dict(final_regions)

# Stack for regions leftover
stack = []

# Create new dict containing regions with more than 5 neighbours
for key in list(new_final):

	if len(new_final[key]) < 5:
		stack += [key]
		del new_final[key]



def sebile(graph, vertex, path=[]):

	# Mark current region as visited
	path += [vertex] 

	# Check neighbour stations of current region
	for neighbour in graph[vertex]:

		# If neighbour station equal to station of current region change current station
		if neighbour.radio == vertex.radio:
			vertex.radio += 1

		# Change current radio to 2 if 5 and call function 
		# to try and force to use 4 stations
		if vertex.radio == 5:
			vertex.radio = 2
			path = sebile(graph, neighbour, path)

	# Check neighbours of current region
	for neighbour in graph[vertex]:

		# If neighbour has not been marked
		# call function on that region
		if neighbour not in path:
			path = sebile(graph, neighbour, path)

	return path 

# First call function on dict with regions with more than 5 regions 
sebile(adjacency_matrix, list(new_final.keys())[0])

# Call function on original dict with regions to color remaining regions
sebile(adjacency_matrix, list(final_regions.keys())[0])


