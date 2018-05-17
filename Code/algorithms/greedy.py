# for running without main.py uncomment
# from data_structure import data_structure
# from ukraine import country

# regions = country()

# final_regions = data_structure(regions)

def greedy(regions):

	for key in regions:

		radios = [1, 2, 3, 4, 5, 6, 7]
		options = [1, 2, 3, 4, 5, 6, 7]

		# first region V already has first option
		if key == next(iter(regions)):
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

	print(regions)
	return regions
