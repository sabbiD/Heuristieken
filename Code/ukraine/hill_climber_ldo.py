import random
from data_structure import data_structure
from ukraine import country
from hill_helpers import shared_regions, change_region
from ldo_hill import ldo_hill
import operator
from map2 import make_map

regions = country()

final_regions = data_structure(regions)

def hill_climber(final_regions):

	radios = [1,2,3,4]#,5,6,7]

	# create initial state randomly
	for key in final_regions:

		key.radio = random.choice(radios)

	costs = 0

	# check how many conflicts there are
	shared = shared_regions(final_regions)

	# list of keys that have a conflict
	conflict_radios = shared[1]


	order = ldo_hill(conflict_radios, final_regions)


	# amount of conflicts
	conflicts = shared[0]
	#print("amount of conflicts is {}".format(conflicts))

	while conflicts is not 0:

		# change a random region
		key_region = order[0]
		print("region to be changed is {}".format(key_region))
		old_radio = key_region.radio

		change_radio = change_region(key_region, final_regions, radios)

		print("region radio is now {}".format(change_radio))

		new_radio = change_radio

		# count amount of conflicts
		shared_new = shared_regions(final_regions)

		new_conflicts = shared_new[0]

		# if amount of conflicts is less, take change as new state
		if new_conflicts < conflicts:
			conflicts = new_conflicts
			print("amount of conflicts is now {}".format(conflicts))
			conflict_radios = shared_new[1]
			order = ldo_hill(conflict_radios, final_regions)
			costs += 1

		# else: turn radio back, continue with old state
		else:
			key_region.radio = old_radio
			print("ELSE amount of conflicts was {}".format(conflicts))
			print("ELSE amount of conflicts is now {}".format(new_conflicts))
			print("ELSE radio is now {}".format(key_region.radio))

	print(costs)
	return final_regions

make_map(hill_climber(final_regions))





