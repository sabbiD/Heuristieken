""" Hill-climber 2.0
	
	Hill_climber.py contains a hill climber function for map colouring.
	The hill climber function uses 2 helper functions from hill_helpers.py
	With help from https://ai.stackexchange.com/questions/5377/hill-climbing-search-map-coloring-problem.

"""
import random
from randomy import randomy
from hill_helpers import shared_regions, change_region, calculate_costs


def hill_climber_costs(data, amount_radios):

	radios = amount_radios
	
	# Create initial state randomly
	random_state = randomy(data, amount_radios)
	while random_state == 1:
		reset(data)
		random_state = randomy(data, amount_radios)

	# Check the costs
	shared = shared_regions(random_state)

	# List of keys that have a conflict
	conflict_radios = shared[1]

	# Amount of conflicts
	conflicts = shared[0]

	costs = 0
	iterations = 0

	while conflicts is not 0:

		# Change a random region
		key_region = random.choice(conflict_radios)
		old_radio = key_region.radio
		change_radio = change_region(key_region, data, amount_radios)
		new_radio = change_radio

		# Count amount of conflicts
		shared_new = shared_regions(data)
		new_conflicts = shared_new[0]

		# If amount of conflicts is less than before, take change as new state
		if new_conflicts < conflicts:
			conflicts = new_conflicts
			conflict_radios = shared_new[1]

			# Increment costs if a change was made
			costs += 1

		# Otherwise turn radio back and continue with old state
		else:
			key_region.radio = old_radio

		iterations += 1

		# If conflicts is not 0 after 100 tries, algorithm failed
		if iterations == 100:
			return 1

	return data
