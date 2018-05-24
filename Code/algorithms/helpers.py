import operator
import random

def neighbour_set(regions, key):

	neighb_station = set()
	for neighbor in regions.get(key):

		neighb_station.add(neighbor.radio)

	return neighb_station

def random_order(final_regions):
	order = list(final_regions.keys())
	random.shuffle(order)
	return order

def ldo(data):

	order = random_order(data)
	neighbors = {}

	for key in order:
		neighb_count = 0
		for buur in data.get(key):
			neighb_count +=1

		neighbors[key] = neighb_count

	ldo_order = []
	
	for i in data:
		keys = max(neighbors.items(), key=operator.itemgetter(1))[0]
		ldo_order.append(keys)
		del neighbors[keys]

	return ldo_order

def reset(final_regions):
	for key in final_regions:
		key.radio = 0

def basic_ldo(data):
	new_data = data.copy()

	for region in data:
		

