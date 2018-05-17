from helpers import neighbour_set

def greedy(data, order):

	for key in data:
		key.radio = 0

	i = 0
	for key in order:
		radios = [1, 2, 3, 4, 5, 6, 7]
		options = [1, 2, 3, 4, 5, 6, 7]

		# first region V already has first option
		if i == 0:
			key.radio = 1

		# colour all remaining V-1 regions with lowest possible option
		else:

			neighb_station = neighbour_set(data, key)
			
			# check all possible radios
			for i in range(len(radios)):

				# if option is in neighbours
				if radios[i] in neighb_station:

					# remove option
					options.remove(radios[i])

		# choose lowest available option
		key.radio = min(options)
		i += 1
	return data

