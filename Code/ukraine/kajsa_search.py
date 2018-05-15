from ukraine import country
from kgbUA import final_regions
import time
# http://www.koderdojo.com/blog/depth-first-search-in-python-recursive-and-non-recursive-programming
data = final_regions

for key in data:
	key.radio = 1

def kajsa_search(graph, start):
	start_time = time.time()
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

	
	print("--- %s seconds ---" % (time.time() - start_time))
	return path

start = list(final_regions.keys())[0]

kajsa_search(data, start)










