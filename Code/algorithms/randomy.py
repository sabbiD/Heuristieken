# Team KGB, Radio Russia
# randomy creates a random distribution of x radiotypes with the
# constraint that a neighbouring region cannot have the same type.

from helpers import neighbour_set
import random


# Creates a random distribution of x radio types (with constraints)
def randomy(regions, radios):
	
	# Create a random order
	order = list(regions.keys())
	random.shuffle(order)

	# Change each region in random order
	for region in order:
		available = list(radios)

		# Create set of neighbours
		neighb_station = neighbour_set(regions, region)

		for i in neighb_station:

			# Remove all neighbouring stations from available radios
			if i != 0:
				available.remove(i)

			if not available:
				return 1

		# Pick a random available radio
		region.radio = random.choice(available)

	return regions


