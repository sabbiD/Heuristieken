from ukraine import country
import random

regions = country()

class Region:
	def __init__(self, index, radio=1):
		self.index = index
		self.radio = radio

	def __str__(self):

		return ("Region {}: Radio {}".format(self.index
			, self.radio))
	def __repr__(self):

		return str(self) + " \n" 

def data_structure(regions):
	all_neighbors = []
	temp = {}
	final_regions = {}

	# make dict for every region with objects as values
	for key in regions:
		temp[key] = Region(key)

	# make region objects for every neighbour
	for values in regions.values():
		new = []
		for neighbor in values:
			for key in temp:
				if neighbor == key:
					neighbor = temp.get(key)
					new.append(neighbor)
		all_neighbors.append(new)

	counter = 0

	# make final dict with key(region) as object and values(neighbours) as objects
	for value in temp.values():
		final_regions[value] = all_neighbors[counter]
		counter += 1

	return final_regions

final_regions = (data_structure(regions))

# Add radiostations to regions
def radio(regions):

	for key in regions:
		radio = 1

		print(key)
		
		neighb_station = set()


		for neighbor in regions.get(key):
			neighb_station.add(neighbor.radio)
		print(neighb_station)

		for i in range(7):
			if radio in neighb_station:
				radio += 1

			else:
				break
		key.radio = radio

	return regions

# randomizer
def randomizer(regions):

	
	for key in regions:

		radios = [1, 2, 3, 4]#,"5","6","7"]

		key.radio = random.choice(radios)
		
		neighb_station = set()


		for buur in regions.get(key):
			neighb_station.add(buur.radio)

			if key.radio in neighb_station:
				radios.remove(key.radio)

				if not radios:
					return 1
					
				key.radio = random.choice(radios)

			else:
				break

	return regions



