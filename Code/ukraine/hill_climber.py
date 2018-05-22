import random
from data_structure import data_structure
from ukraine import country
from hill_helpers import shared_regions, change_region

regions = country()

final_regions = data_structure(regions)

def hill_climber(final_regions):

	radios = [1,2,3,4]#,5,6,7]

	# create initial state randomly
	for key in final_regions:

		key.radio = random.choice(radios)

	# costs: not used right now, but each accepted change should increment costs
	costs = 0

	# check how many conflicts there are
	shared = shared_regions(final_regions)

	# list of keys that have a conflict
	conflict_radios = shared[1]

	# amount of conflicts
	conflicts = shared[0]

	# change radios until there are no more conflicts
	while conflicts is not 0:

		# choose a random conflict region
		key_region = random.choice(conflict_radios)

		# keep track of radio in case changing does not decrease conflicts
		old_radio = key_region.radio

		# change region
		change_radio = change_region(key_region, final_regions, radios)
		new_radio = change_radio

		# count new amount of conflicts
		shared_new = shared_regions(final_regions)
		new_conflicts = shared_new[0]

		# if amount of conflicts is less, take change as new state
		if new_conflicts < conflicts:

			conflicts = new_conflicts
			conflict_radios = shared_new[1]
			costs += 1

		# else: keep old station, continue with old state
		else:
			key_region.radio = old_radio

	return final_regions

hill_climber(final_regions)





