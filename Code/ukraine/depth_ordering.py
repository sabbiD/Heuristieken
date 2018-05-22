from ukraine import country
from data_structure import data_structure
import sys
import random
from costs import distribution
from score import score
from ldo import ldo

regions = country()
final = data_structure(regions)

for key in final:
	key.radio = 0

order = ldo(final)

adjacency_matrix = final

radios = [1, 2, 3, 4, 5, 6, 7]



# copy of dict with all regions
#new_final = dict(final)

# stack for regions leftover
# for key in list(new_final):

# 	if len(new_final[key]) < 5:
# 		del new_final[key]

#now only contains regions >5 neighbours
#print(new_final)


def dfs_recursive(graph, vertex, path=[]):
	path += [vertex] 
	neigh_station = set()

	
	for region in graph.get(vertex):
		
		neigh_station.add(region.radio)
	
	options = [1, 2, 3, 4]#, 5]#, 6, 7]
	
	if vertex.radio is not 0:

		options.remove(vertex.radio)

	for i in range(len(radios)):

		if radios[i] in neigh_station:
			options.remove(radios[i])
	

		vertex.radio = min(options)

	for neighbour in graph[vertex]:	
		
		# # ga naar vorige in de lijst ipv naar buur  
		# # stop als radio niet kan! hou lijst bij met buur radios
		if neighbour not in path:
			neigh_station = []
			path = dfs_recursive(graph, neighbour, path)

	return path 

#dfs_recursive(adjacency_matrix, list(new_final.keys())[0])
dfs_recursive(adjacency_matrix, order[0])

print(final)

score = score(final)
distribution = distribution(score)

print(distribution)