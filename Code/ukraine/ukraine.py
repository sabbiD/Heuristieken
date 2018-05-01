from shapely.geometry import shape
import fiona
import string

def country():


	file_name = "ukr_admbnda_adm1_q2_sspe_20171221.shp"

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
	letter_list = []
	regio = ""
	buur = ""
	alphabets = string.ascii_lowercase
	names = set()

	for i in alphabets:
		letter_list.append(i)

	letter_list.append("aa")

	print(letter_list)

	# Vindt de neighbours van iedere regio in je shapefile
	for i, line, name in geoms:
		"letter_list[i]" = name

		if "letter_list[i]" not in names:
			names.add("letter_list[i]")
		#print("\nCurrent country: {}\nNeighbours: ".format(name))
		for lin, name_other in geoms:
			if line.touches(lin):
				#print("\t", name_other)
				buur = name_other
				neighbours.append(buur)

		regions[name] = neighbours
		counter += 1
		neighbours = []

	print(names)


	return(regions)




