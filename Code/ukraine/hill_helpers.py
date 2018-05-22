import random
import operator


# check how many conflicts there are, return amount of conflicts + list of regions that have a conflict
def shared_regions(final_regions):

	conflicts = 0
	conflict_radios = []

	for key in final_regions:

		neighb_stations = set()

		# create set with neighbors
		# (make function to create neighbor set, used in almost every function right now)
		for neighbor in final_regions.get(key):
			neighb_stations.add(neighbor.radio)

		# check for conflict
		if key.radio in neighb_stations:
			conflicts+=1
			conflict_radios.append(key)

	return conflicts, conflict_radios


# change the station of a conflicting region
def change_region(key_region, final_regions, radios):

	neighb_station = set()
	options = [1,2,3,4,5,6,7]

	for neighbor in final_regions.get(key_region):
		neighb_station.add(neighbor.radio)

	# check all possible radios
	for i in range(len(radios)):

		# if option is in neighbours
		if radios[i] in neighb_station:

			# remove option
			options.remove(radios[i])

	if not options:
		return key_region.radio

	# change radio to lowest possible option
	else:
		key_region.radio = min(options)

		return key_region.radio

def ldo_hill(conflict_radios, final_regions):

	neighbors = {}

	for key in conflict_radios:
		neighb_count = 0
		for buur in final_regions.get(key):
			print("buur is {}".format(buur))
			neighb_count +=1

		neighbors[key] = neighb_count
	print("neighbor count is {}".format(neighbors))

	order = []
	for i in conflict_radios:
		keys = max(neighbors.items(), key=operator.itemgetter(1))[0]
		order.append(keys)
		del neighbors[keys]

	return order

def random_hill(conflict_radios):
	order = random.shuffle(conflict_radios)
	return order

