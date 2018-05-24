# Team KGB, Radio Russia
# kajsa.search.py creates a distribution of radio-stations, loosely based on depth-first search.
# Help from: http://www.koderdojo.com/blog/depth-first-search-in-python-recursive-and-non-recursive-programming


def kajsa_search(graph, start):
	stack, path = [start], []
	
	while stack:
		vertex = stack.pop()
		
		if vertex in path:
			continue
		else:
			path.append(vertex)	

		for neighbour in graph[vertex]:
			
			if neighbour in path:
				used = neighbour.radio
			
				if used == vertex.radio:
					vertex.radio +=1


			if vertex.radio == neighbour.radio:
				neighbour.radio += 1

			
			stack.append(neighbour)

	return path











