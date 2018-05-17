import operator
import random

def neighbour_set(regions, key):

	neighb_station = set()
	for neighbor in regions.get(key):

		neighb_station.add(neighbor.radio)

	return neighb_station

def ldo(data):

	neighbors = {}

	for key in data:
		neighb_count = 0
		for buur in data.get(key):
			neighb_count +=1

		neighbors[key] = neighb_count

	order = []
	for i in data:
		keys = max(neighbors.items(), key=operator.itemgetter(1))[0]
		order.append(keys)
		del neighbors[keys]
	return order

def random_order(final_regions):
	order = list(final_regions.keys())
	random.shuffle(order)
	return order

def reset(final_regions):
	for key in final_regions:
		key.radio = 0


