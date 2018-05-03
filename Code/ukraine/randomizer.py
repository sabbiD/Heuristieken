from ukraine import country
from data_structure import data_structure
import random

regions = country()
data_structure = data_structure(regions)

def randomizer(regions):

	# for random.choice(key) ?
	for key in regions:

		radios = [1, 2, 3, 4]#,"5","6","7"]

		key.radio = random.choice(radios)
		
		neighb_station = set()


		for neighbour in regions.get(key):
			neighb_station.add(neighbour.radio)

			if key.radio in neighb_station:
				radios.remove(key.radio)
				key.radio = random.choice(radios)

			else:
				break

	return regions
