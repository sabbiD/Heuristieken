from data_structure import data_structure
from ukraine import country

regions = country()

final_regions = data_structure(regions)

# greedy:
# color first vertext with first color
# do following for remaining v-1 vertices:
# a: consider currently picked vertex and color it with lowest
# numbered color that has not been used on any previously colored vertices
# adjacent to it.
# if all previously used colors appear on vertices adjacent, assign new color

def greedy(regions):

	for key in regions:

		radios = [1, 2, 3, 4, 5, 6, 7]
		options = [1, 2, 3, 4, 5, 6, 7]

		# first region V already has first option
		if key == next(iter(regions)):
			continue

		# colour all remaining V-1 regions with lowest possible option
		else:

			neighb_station = set()

			# get neighbor radios
			for neighbor in regions.get(key):
				print("neighbour is {}".format(neighbor))
				neighb_station.add(neighbor.radio)
			
			# check all possible radios
			for i in range(len(radios)):

				# if option is in neighbours
				if radios[i] in neighb_station:

					# remove option
					options.remove(radios[i])

		# choose lowest available option
		key.radio = min(options)


			#print(neighb_station)
	print(regions)


greedy(final_regions)