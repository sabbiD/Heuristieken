import random
from hill_helpers import shared_regions, change_region, ldo_hill
import operator

def hill_climber(data, amount_radios):

	radios = [1,2,3,4]

	# create initial state randomly
	for key in data:

		key.radio = random.choice(radios)

	costs = 0
	iterations = 0

	# check how many conflicts there are
	shared = shared_regions(data)

	# list of keys that have a conflict
	conflict_radios = shared[1]

	# amount of conflicts
	conflicts = shared[0]

	while conflicts is not 0:

		# change a random region
		key_region = random.choice(conflict_radios)

		old_radio = key_region.radio

		change_radio = change_region(key_region, data, amount_radios)
		new_radio = change_radio

		# count amount of conflicts
		shared_new = shared_regions(data)

		new_conflicts = shared_new[0]

		# if amount of conflicts is less, take change as new state
		if new_conflicts < conflicts:
			conflicts = new_conflicts
			conflict_radios = shared_new[1]
			costs += 1

		# else: turn radio back, continue with old state
		else:
			key_region.radio = old_radio

		iterations += 1

		# sometimes infinite loop if random order does not work out
		if iterations == 1000:
			return 1
	return data, costs



