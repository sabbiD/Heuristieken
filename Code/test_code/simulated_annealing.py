
""" Simulated annealing

	Attempts to create a valid distribution of radio stations by changing
	a radiostation, and checking whether this reduces the amount of conflicts.
	If changing does not reduce the amount of conflicts, there is a certain 
	probability that the change is accepted, since sometimes it is necessary
	to accept a worse state in order to get a better solution in the end.

"""

import math
import random
from hill_helpers import shared_regions, change_region

def simulated_annealing(data, amount_radios):

	radios = amount_radios
	# Create initial state randomly
	for region in data:
		region.radio = random.choice(radios)

	# Check how many conflicts there are
	shared = shared_regions(data)

	# List of keys that have a conflict
	conflict_radios = shared[1]

	# Amount of conflicts
	conflicts = shared[0]

	costs = 0
	iterations = 0
	temperature = 1.0
	temperature_min = 0.0000001
	cooling_rate = 0.99

	while temperature > temperature_min:

		# Change a random region
		key_region = random.choice(conflict_radios)
		old_radio = key_region.radio
		change_radio = change_region(key_region, data, amount_radios)
		new_radio = change_radio

		# Count amount of conflicts
		shared_new = shared_regions(data)
		new_conflicts = shared_new[0]

		if new_conflicts >= conflicts: 
			probability = 2.71828 * ((new_conflicts -conflicts) / temperature)

			if probability < random.random():
				key_region.radio = old_radio
				iterations += 1
				temperature *= cooling_rate
				continue

		conflicts = new_conflicts
		conflict_radios = shared_new[1]

		# Increment costs if a change was made
		costs += 1
		iterations += 1
		temperature *= cooling_rate

		if conflicts == 0:
			break

	return data
