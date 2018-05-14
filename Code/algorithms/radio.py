# for trying out code without main.py uncomment
# from ukraine import country
# from data_structure import data_structure

# regions = country()

# final_regions = data_structure(regions)

def radio(regions):

	for key in regions:
		radio = 1
		
		neighb_station = set()


		for neighbor in regions.get(key):
			neighb_station.add(neighbor.radio)

		for i in range(7):
			if radio in neighb_station:
				radio += 1

			else:
				break
		key.radio = radio

	return regions

# print(radio(final_regions))