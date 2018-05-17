import operator

def ldo(final_regions):

	neighbors = {}

	for key in final_regions:
		neighb_count = 0
		for buur in final_regions.get(key):
			neighb_count +=1

		neighbors[key] = neighb_count

	order = []
	for i in range(27):
		keys = max(neighbors.items(), key=operator.itemgetter(1))[0]
		order.append(keys)
		del neighbors[keys]

	return order