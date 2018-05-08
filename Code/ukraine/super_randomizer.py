from data_structure import data_structure
from ukraine import country
import random
import time
from random import shuffle



regions = country()

final_regions = data_structure(regions)


def randomizer(regions):
	start_time = time.time()

	keys = list(regions.keys())
	random.shuffle(keys)
	
	for key in keys:

		radios = [1, 2, 3, 4, 5 ,6 ,7]

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
	
	print("--- %s seconds ---" % (time.time() - start_time))
	return regions

print(randomizer(final_regions))
