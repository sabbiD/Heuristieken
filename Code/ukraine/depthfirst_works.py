import sys
import random
from helpers import neighbour_set
from country import country 
from data_structure import data_structure

final = country("ukr_admbnda_adm1_q2_sspe_20171221.shp", "ADM1_PCODE")
final = data_structure(final)

adjacency_matrix = final
for key in final:
	key.radio = 0
#print(final)

# # copy of dict with all regions
# new_final = dict(final)

# # stack for regions leftover
# for key in list(new_final):

# 	if len(new_final[key]) < 5:
# 		del new_final[key]

# #now only contains regions >5 neighbours
# #print(new_final)

	# kosten1 = [12, 26, 27, 30, 37, 39, 41]
	# kosten2 = [19, 20, 21, 23, 36, 37, 38]
	# kosten3 = [16, 17, 31, 33, 36, 56, 57]
	# kosten4 = [3, 34, 36, 39, 41, 43, 58]

costs_2 = {1: 19, 2: 20, 3: 21, 4: 23, 5: 36, 6: 37, 7: 38} 

bound = 0

def dfs_recursive(graph, vertex, path=[], count=0):

	radios = [1, 2, 3, 4, 5, 6, 7]
	#radios = [19, 20, 21, 23, 36, 37, 38]

	total_cost = 0

	path += [vertex] 
	neigh_station = set()

	for region in graph.get(vertex):
		
		neigh_station.add(region.radio)
	
	options = [1, 2, 3, 4, 5, 6, 7]
	#options = [19, 20, 21, 23, 36, 37, 38]
	
	if vertex.radio is not 0:

		options.remove(vertex.radio)

	for i in range(len(radios)):

		if radios[i] in neigh_station:
			options.remove(radios[i])

	vertex.radio = min(options)
	total_cost += costs_2[min(options)]
	
	global bound 
	bound += total_cost
	
	for neighbour in graph[vertex]:	
		
		# ga naar vorige in de lijst ipv naar buur  
		if neighbour not in path:
			neigh_station = []
			path = dfs_recursive(graph, neighbour, path, count=1)
		
	return path 
print(bound)
#dfs_recursive(adjacency_matrix, list(new_final.keys())[0])
dfs_recursive(adjacency_matrix, list(final.keys())[0])
print(bound)