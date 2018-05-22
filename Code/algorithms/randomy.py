from helpers import neighbour_set
import random

def randomy(regions, radios):
	
	keys = list(regions.keys())
	random.shuffle(keys)

	for key in keys:
		available = list(radios)

		neighb_station = neighbour_set(regions, key)

		for i in neighb_station:

			if i != 0:
				available.remove(i)

			if not available:

				return 1

		key.radio = random.choice(available)

	return regions


