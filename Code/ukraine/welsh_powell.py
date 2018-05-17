# order in degrees.
# first color the first vertex with 1
# then go through the list and color all possible vertices with color 1
# remove these from the list
# color the first one with color 2
# etc etc

# for running without main.py uncomment
from data_structure import data_structure
from ukraine import country
#from map2 import make_map
from ldo import ldo

regions = country()

final_regions = data_structure(regions)

order = ldo(final_regions)

for key in final_regions:
	key.radio = 0

colors = [1,2,3,4,5]
def welsh_powell(order, color):
	i = 0
	for key in order:
		neighb_station = set()
		for neighbor in final_regions.get(key):
			neighb_station.add(neighbor.radio)

		if color not in neighb_station:
			key.radio = color
			order.remove(key)

	i += 1

	while order:
		welsh_powell(order, colors[i])

	return final_regions

welsh_powell(order, colors[0])

for key in final_regions:
	print(key)
	for neighbor in final_regions.get(key):
		print("neighbor {}".format(neighbor))










	# def greedy(regions):

	# for key in regions:
	# 	key.radio = 0

	# i = 0
	# for key in order:
	# 	radios = [1, 2, 3, 4, 5, 6, 7]
	# 	options = [1, 2, 3, 4, 5, 6, 7]

	# 	# first region V already has first option
	# 	if i == 0:
	# 		print(key)
	# 		key.radio = 1

	# 	# colour all remaining V-1 regions with lowest possible option
	# 	else:

	# 		neighb_station = set()

	# 		# get neighbor radios
	# 		for neighbor in regions.get(key):

	# 			neighb_station.add(neighbor.radio)
			
	# 		# check all possible radios
	# 		for i in range(len(radios)):

	# 			# if option is in neighbours
	# 			if radios[i] in neighb_station:

	# 				# remove option
	# 				options.remove(radios[i])

	# 	# choose lowest available option
	# 	key.radio = min(options)
	# 	i += 1
	# return regions
