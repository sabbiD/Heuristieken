from shapely.geometry import shape
import fiona
import string

def country(file_name):

	file_name = file_name

	# NOTE: Gebruik deze lines om te kijken hoe de key heet die je nodig hebt
	# voor de namen/id's
	#print(fiona.open(file_name)[0]['properties'])

	# Haal een tuple met de coordinaten en de naam uit de shapefile
	geoms =[(shape(feature['geometry']), feature['properties']['ADM1_PCODE']) for
	    feature in fiona.open(file_name)]

	class Region:
		def __init__(self, index, radio=0):
			self.index = index
			self.radio = radio

		def __str__(self):

			return ("Region {}: Radio {}".format(self.index
				, self.radio))

	# make dictionary with all regions and its neighbours
	regions = dict()
	counter = 0;
	neighbours = []

	# Vindt de neighbours van iedere regio in je shapefile
	for line, name in geoms:
		#print("\nCurrent country: {}\nNeighbours: ".format(name))
		for lin, name_other in geoms:
			if line.touches(lin):
				#print("\t", name_other)
				neighbours.append(name_other)

		regions[name] = neighbours
		counter += 1
		neighbours = []


	return(regions)




