""" Hill-climber
	
	Hill_climber.py contains a hill climber function for map colouring.
	The hill climber function uses 2 helper functions from hill_helpers.py
	With help from https://ai.stackexchange.com/questions/5377/hill-climbing-search-map-coloring-problem.

"""

import random
from randomy import randomy
from hill_helpers import shared_regions, change_region, calculate_costs
from helpers import reset


def hill_climber_costs(data, amount_radios):
	
	# Create initial state randomly
	random_state = randomy(data, amount_radios)
	while random_state == 1:
		reset(data)
		random_state = randomy(data, amount_radios)

	# Check how many conflicts there are
	shared = shared_regions(random_state)

	# List of keys that have a conflict
	conflict_radios = shared[1]

	# Amount of conflicts
	conflicts = shared[0]
	print(conflicts)


	# Check the costs
	costs = calculate_costs(random_state)
	print(costs)

	for i in range(1000):

		# Change a random region
		key_region = random.choice(list(random_state.keys()))
		old_radio = key_region.radio
		change_radio = change_region(key_region, data, amount_radios)
		new_radio = change_radio[0]
		new_state = change_radio[1]

		# Count amount of conflicts
		new_costs = calculate_costs(new_state)
		new_shared = shared_regions(random_state)
		
		# Amount of conflicts
		new_conflicts = new_shared[0]
		print(new_conflicts)

		# If amount of conflicts is less than before, take change as new state
		if new_costs < costs:
			costs = new_costs
			random_state = new_state

		# Otherwise turn radio back and continue with old state
		else:
			key_region.radio = old_radio

	print(costs)
	return new_state
