import random
from data_structure import data_structure
from ukraine import country


# check how many conflicts there are, return list of regions that have a conflict
def shared_regions(final_regions):

	conflicts = 0
	conflict_radios = []

	for key in final_regions:

		neighb_stations = set()
		for neighbor in final_regions.get(key):
			neighb_stations.add(neighbor.radio)

		if key.radio in neighb_stations:
			conflicts+=1
			conflict_radios.append(key)

	#print(conflict_radios)
	return conflicts, conflict_radios


def change_region(key_region, final_regions, radios):

	neighb_station = set()
	options = [1,2,3,4]#,5]#,6,7]


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

	else:
		key_region.radio = min(options)

		return key_region.radio

