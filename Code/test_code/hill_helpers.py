# Team KGB, Radio Russia
# hill_helpers.py contains the helper functions for hill_climber.py
# shared_regions checks whether a region has a conflict (i.e. has the same radio
# station as one of its neighbours), and returns the amount of conflicts and which
# regions have a conflict.
# change_regions changes the radio station of a conflicting regions such that
# this region does not have a conflict anymore.

import random
import operator
from helpers import neighbour_set


# Check how many conflicts there are, return amount of conflicts + list of 
# regions that have a conflict
def shared_regions(final_regions):

	conflicts = 0
	conflict_radios = []

	for region in final_regions:

		# Set with neighbouring radios
		neighb_station = neighbour_set(final_regions, region)

		# Check whether region's radio is same as one of its neighbours
		if region.radio in neighb_station:
			conflicts += 1
			conflict_radios.append(region)

	return conflicts, conflict_radios


# Change the station of a conflicting region
def change_region(key_region, final_regions, radios):

	options = list(radios)

	# Set with neighbouring radios
	neighb_station = neighbour_set(final_regions, key_region)

	# Create a list with possible radios to be used
	for i in range(len(radios)):

		# Remove from list if neighbour has this radio
		if radios[i] in neighb_station:
			options.remove(radios[i])

		# If there are no options left, keep old radio
		if not options:
			return key_region.radio

		# Change radio to lowest possible option
		else:
			key_region.radio = min(options)

			return key_region.radio
