# for trying out code without main.py uncomment
# from ukraine import country
from data_structure import data_structure
from helpers import ldo
from helpers import reset
from helpers import random_order

# regions = country()

# final_regions = data_structure(regions)

# order = random_order(final_regions)
#print(order)

def radio(order):

	# reset(final_regions)
	#print(order)
	for key in order:
		radio = 1
		
		neighb_station = set()


		for neighbor in final_regions.get(key):
			neighb_station.add(neighbor.radio)

		for i in range(7):
			if radio in neighb_station:
				radio += 1

			else:
				break
		key.radio = radio

	return final_regions

# print(radio(order))