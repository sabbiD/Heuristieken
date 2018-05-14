# for running without main.py uncomment
# from data_structure import data_structure
# from ukraine import country
import random

# regions = country()

# final_regions = data_structure(regions)

def randomy(regions):
	
	for key in regions:
			key.radio = 1

	keys = list(regions.keys())
	random.shuffle(keys)
		
	for key in keys:

		radios = [1, 2, 3, 4, 5, 6, 7]

		neighb_station = set()

		for buur in regions.get(key):
			neighb_station.add(buur.radio)

		for i in neighb_station:

			radios.remove(i)
			if not radios:
				return 1


		key.radio = random.choice(radios)

	return regions

# print(randomy(final_regions))

# def check(regions):

# 	no = 0
# 	for i in range(10000):
# 		x = randomy(regions)

# 		if x == 1:
# 			no += 1
# 		else:
# 			return x


