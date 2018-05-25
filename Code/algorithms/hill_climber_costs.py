""" Hill-climber
	
	Hill_climber_costs.py contains a hill climber function for map colouring.
	This algorithm starts with a random, valid solution, and tries to minimize the costs.
	The hill climber function uses 3 helper functions from hill_helpers.py.
	With help from https://ai.stackexchange.com/questions/5377/hill-climbing-search-map-coloring-problem.

"""

import random
from randomy import randomy
from hill_helpers import shared_regions, change_region, calculate_costs
from helpers import reset


def hill_climber_costs(data, amount_radios):
	
	# Create initial state randomly
	random_state = randomy(data, amount_radios)

	# Loop until valid state is found
	while random_state == 1:
		reset(data)
		random_state = randomy(data, amount_radios)

	# Check the costs
	costs = calculate_costs(random_state)

	# Attempt to minimize the costs 100 times
	for i in range(100):

		# Change a random region
		key_region = random.choice(list(random_state.keys()))
		old_radio = key_region.radio
		change_radio = change_region(key_region, data, amount_radios)
		new_radio = change_radio[0]
		new_state = change_radio[1]
		new_costs = calculate_costs(new_state)

		# If cost is less than before, take new state
		if new_costs < costs:
			costs = new_costs
			random_state = new_state

		# Otherwise turn radio back and continue with old state
		else:
			key_region.radio = old_radio

	return new_state
