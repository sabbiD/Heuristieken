""" Helpers

	helpers.py contains the helper functions for the algorithms.
	neighbour set creates a set of the neighbours of a region.
	random_order creates a random ordering of the data
	ldo creates a LDO ordering of the data
	reset puts all radio stations to 0
	 
"""

import operator
import random


# Create a set of the neighbour radios of a region
def neighbour_set(data, key):

	neighb_station = set()

	# Add each neighbour station to set
	for neighbor in data.get(key):
		neighb_station.add(neighbor.radio)

	return neighb_station


# Create a random ordering of the data
def random_order(data):

	order = list(data.keys())
	random.shuffle(order)
	return order


# Create a LDO ordering of the data
def ldo(data):

	# Shuffle data
	order = random_order(data)
	neighbors = {}

	# Count amount of neighbours per region
	for region in order:
		neighb_count = 0

		for buur in data.get(region):
			neighb_count +=1

		neighbors[region] = neighb_count

	ldo_order = []

	# Create order
	for i in data:

		# Get key with maximum amount of neighbours
		keys = max(neighbors.items(), key=operator.itemgetter(1))[0]
		ldo_order.append(keys)

		# Delete key from dictionary
		del neighbors[keys]

	return ldo_order


# Set all radio stations to 0
def reset(data):
	for region in data:
		region.radio = 0


