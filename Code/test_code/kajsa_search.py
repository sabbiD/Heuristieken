""" Kajsa Search
	
	kajsa.search.py creates a distribution of radio-stations, loosely based on an iterative depth-first search.
	Help from: http://www.koderdojo.com/blog/depth-first-search-in-python-recursive-and-non-recursive-programming

"""

def kajsa_search(graph, start):
	stack, path = [start], []
	
	# Pop the region on top of the stack
	while stack:
		vertex = stack.pop()
		
		# Check if region is visited, if not append to path
		if vertex in path:
			continue
		else:
			path.append(vertex)	

		# Loop through the neoghbouring regions, keep track of the regions that are already in the path
		for neighbour in graph[vertex]:
			
			if neighbour in path:
				used = neighbour.radio
			
				if used == vertex.radio:
					vertex.radio +=1

			# Constantly alter neighbour radios, so every neighbour gets changed instead of the vertex
			if vertex.radio == neighbour.radio:
				neighbour.radio += 1

			stack.append(neighbour)

	return path











