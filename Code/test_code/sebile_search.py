from kgbUA import final_regions
import sys


adjacency_matrix = final_regions


# copy of dict with all regions
new_final = dict(final_regions)

# stack for regions leftover
stack = []
for key in list(new_final):

	if len(new_final[key]) < 5:
		stack += [key]
		del new_final[key]

#now only contains regions >5 neighbours
#print(new_final)

def sebile(graph, vertex, path=[]):
	path += [vertex] 

	for neighbour in graph[vertex]:

		if neighbour.radio == vertex.radio:
			vertex.radio += 1

		if vertex.radio == 5:
			vertex.radio = 2
			path = sebile(graph, neighbour, path)

		if neighbour not in path:
			path = sebile(graph, neighbour, path)

	return path 

sebile(adjacency_matrix, list(new_final.keys())[0])
#print(final)
sebile(adjacency_matrix, list(final_regions.keys())[0])


#print(final)