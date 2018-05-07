from data_structure import data_structure
from ukraine import country
import random

regions = country()

final_regions = data_structure(regions)

def randomizer(regions):
	
	for key in regions:

		radios = [1, 2, 3, 4]#,"5","6","7"]

		key.radio = random.choice(radios)
		
		neighb_station = set()

		for buur in regions.get(key):
			neighb_station.add(buur.radio)

			if key.radio in neighb_station:
				radios.remove(key.radio)

				if not radios:
					return 1
					
				key.radio = random.choice(radios)

			else:
				break

	return regions