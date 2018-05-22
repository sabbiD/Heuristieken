import random
from hill_helpers import shared_regions, change_region, ldo_hill, random_hill
import operator

def hill_climber(order_string, data):

	radios = [1,2,3,4]

	# create initial state randomly
	for key in data:

		key.radio = random.choice(radios)

	# costs = 0

	# check how many conflicts there are
	shared = shared_regions(data)

	# list of keys that have a conflict
	conflict_radios = shared[1]

	if order_string == "ldo":
		order = ldo_hill(conflict_radios, data)
	else:
		order = random_hill(conflict_radios)

	# amount of conflicts
	conflicts = shared[0]

	while conflicts is not 0:

		# change a random region
		key_region = order[0]
		old_radio = key_region.radio

		change_radio = change_region(key_region, data, radios)
		new_radio = change_radio

		# count amount of conflicts
		shared_new = shared_regions(data)

		new_conflicts = shared_new[0]

		# if amount of conflicts is less, take change as new state
		if new_conflicts < conflicts:
			conflicts = new_conflicts
			conflict_radios = shared_new[1]
		if order_string == "ldo":
			order = ldo_hill(conflict_radios, data)
		else:
			order = random_hill(conflict_radios)			
			# costs += 1

		# else: turn radio back, continue with old state
		else:
			key_region.radio = old_radio

	return data



