from ukraine import country

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

	all_neighbours = []
	temp = {}
	data_structure = {}

	# make dict for every region with objects as values
	for key in regions:
		temp[key] = Region(key)

	# make region objects for every neighbour
	for values in regions.values():
		new = []
		for neighbour in values:
			for key in temp:
				if neighbour == key:
					neighbour = temp.get(key)
					new.append(neighbour)
		all_neighbours.append(new)

	counter = 0

	# make final dict with key(region) as object and values(neighbours) as objects
	for value in temp.values():
		data_structure[value] = all_neighbours[counter]
		counter += 1
	
	return data_structure
	