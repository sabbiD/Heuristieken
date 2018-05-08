from ukraine import country
from kgbUA import final_regions

# http://www.koderdojo.com/blog/depth-first-search-in-python-recursive-and-non-recursive-programming
data = final_regions

def dfs(graph, start):
	stack, path = [start], []
	
	
	while stack:
		vertex = stack.pop()
		
		if vertex in path:
			continue
		else:
			path.append(vertex)	

		for neighbour in graph[vertex]:
			print(graph[vertex])
			
			if vertex.radio == neighbour.radio:
				#print(vertex.radio)
				vertex.radio += 1

			#print(neighbour)
			stack.append(neighbour)
	#print(path)
	return path

start = list(final_regions.keys())[0]


d = dfs(data, start)
print(d)






