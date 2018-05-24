# Team KGB, Radio Russia
# data_structure creates the datastructure for Radio Russia.
# The data structure consists of a dictionary,
# in which the keys are Region objects with an index and radio station,
# and in which the values are a list of neighbouring Region objects.


# Region class with index and radio station
class Region:


	def __init__(self, index, radio=0):
		self.index = index
		self.radio = radio


	def __str__(self):
		return ("Region: {}, Radio: {}".format(self.index, self.radio))


	def __repr__(self):
		return str(self) + " \n" 


# Create the data structure for a certain country
def data_structure(regions, country):

	all_neighbors = []
	temp = {}
	final_regions = {}

	# Make dict for every region with objects as keys
	for region in regions:
		temp[region] = Region(region)

	# Make region objects for every neighbour
	for values in regions.values():
		new = []
		for neighbor in values:
			for key in temp:
				if neighbor == key:
					neighbor = temp.get(key)
					new.append(neighbor)
		all_neighbors.append(new)

	counter = 0

	# Make final dict with key(region) as object and values(neighbours) as objects
	for value in temp.values():
		final_regions[value] = all_neighbors[counter]
		counter += 1

	region_count = len(final_regions)

	max_neighbours = 0

	for key in final_regions:
		length_neighbours = len(final_regions[key])
		if length_neighbours > max_neighbours:
			max_neighbours = length_neighbours

	print("Data structure created!\n{} has {} regions. The maximum amount of neighbours is {}".format(country, region_count, max_neighbours))
	return final_regions