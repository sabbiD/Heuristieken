# for running without main.py uncomment
from data_structure import data_structure
from ukraine import country
from map2 import make_map
from ldo import ldo

regions = country()

final_regions = data_structure(regions)

order = ldo(final_regions)


def greedy(regions):

	for key in regions:
		key.radio = 0

	i = 0
	for key in order:
		radios = [1, 2, 3, 4, 5, 6, 7]
		options = [1, 2, 3, 4, 5, 6, 7]

		# first region V already has first option
		if i == 0:
			print(key)
			key.radio = 1

		# colour all remaining V-1 regions with lowest possible option
		else:

			neighb_station = set()

			# get neighbor radios
			for neighbor in regions.get(key):

				neighb_station.add(neighbor.radio)
			
			# check all possible radios
			for i in range(len(radios)):

				# if option is in neighbours
				if radios[i] in neighb_station:

					# remove option
					options.remove(radios[i])

		# choose lowest available option
		key.radio = min(options)
		i += 1
	return regions

greedy(final_regions)
make_map(final_regions)

