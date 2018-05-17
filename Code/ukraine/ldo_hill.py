import operator

def ldo_hill(conflict_radios, final_regions):

	neighbors = {}

	for key in conflict_radios:
		print("key is {}".format(key))
		neighb_count = 0
		for buur in final_regions.get(key):
			print("buur is {}".format(buur))
			neighb_count +=1

		neighbors[key] = neighb_count
	print("neighbor count is {}".format(neighbors))

	order = []
	for i in conflict_radios:
		keys = max(neighbors.items(), key=operator.itemgetter(1))[0]
		order.append(keys)
		del neighbors[keys]

	return order