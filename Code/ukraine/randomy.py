from data_structure import data_structure
from ukraine import country
import random

regions = country()

final_regions = data_structure(regions)

def randomy(regions):
	
	# for key in regions:

	# 	radios = [1, 2, 3, 4]#,"5","6","7"]
		
	# 	neighb_station = set()

	# 	for buur in regions.get(key):
	# 		neighb_station.add(buur.radio)
	# 		print("neighbors: {}".format(neighb_station))

	# 	if key.radio in neighb_station:

	# 		if not radios:
	# 			return 1

	# 		radios.remove(key.radio)

	# 		key.radio = random.choice(radios)

	# 	print("key: {}".format(key.radio))
	# 	for buur in regions.get(key):
	# 		print("buur: {}".format(buur.radio))

	for key in regions:
			key.radio = 1

	keys = list(regions.keys())
	random.shuffle(keys)
		
	for key in keys:
		radios = [1, 2, 3, 4]

		neighb_station = set()


		for buur in regions.get(key):
			neighb_station.add(buur.radio)

		for i in neighb_station:

			radios.remove(i)
			if not radios:
				return 1


		key.radio = random.choice(radios)

		# if key.radio in neighb_station:
		# 	radios.remove(key.radio)

		# 	choice = random.choice(radios)
		# 	print(choice)
		# key.radio = choice
	return regions


# checken hoe vaak het lukt 
yes = 0
no = 0
for i in range(10000):
	x = randomy(final_regions)

	if x == 1:
		no += 1
	else:
		yes +=1

print("yes: {}".format(yes))
print("no: {}".format(no))
		

