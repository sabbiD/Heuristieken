import operator

def ldo(data):

	neighbors = {}

	for key in data:
		neighb_count = 0
		for buur in data.get(key):
			neighb_count +=1

		neighbors[key] = neighb_count

	order = []
	print(len(data))
	for i in data:
		keys = max(neighbors.items(), key=operator.itemgetter(1))[0]
		order.append(keys)
		del neighbors[keys]

	return order