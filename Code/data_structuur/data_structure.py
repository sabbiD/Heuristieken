class Region:
	def __init__(self, index, radio=0):
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