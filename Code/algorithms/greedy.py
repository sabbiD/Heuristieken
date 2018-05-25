""" Greedy algorithm

	greedy.py contains a greedy function for map colouring.
	With help from https://www.slideshare.net/PriyankJain26/graph-coloring-48222920

"""

from helpers import neighbour_set


def greedy(data, order):

	i = 0
	for region in order:
		
		radios = [1, 2, 3, 4, 5, 6, 7]
		options = [1, 2, 3, 4, 5, 6, 7]

		# First region V already has first option
		if i == 0:
			region.radio = 1

		# Colour all remaining V-1 regions with lowest possible option
		else:

			neighb_station = neighbour_set(data, region)
			
			# Create a list with possible radios to be used
			for i in range(len(radios)):
				if radios[i] in neighb_station:

					# Remove from list if neighbour has this radio
					options.remove(radios[i])

		# Choose lowest available option
		region.radio = min(options)

		i += 1

	return data
