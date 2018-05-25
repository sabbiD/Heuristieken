""" Shapefile transformer

	country.py uses shapefiles to create a dictionary with regions as keys,
	and a list of neighbours as values.
	With help from: Wouter and Quinten

"""

from shapely.geometry import shape
import fiona
import string


# Create dictionary of regions with neighbours as values
def country(file_name, name):

	file_name = file_name

	# Retrieve tuple with name and coordinates from shapefile
	geoms =[(shape(feature['geometry']), feature['properties'][name]) for
	    feature in fiona.open(file_name)]

	# Create dictionary with all regions and its neighbours
	regions = dict()
	counter = 0;
	neighbours = []

	# Find neighbours of each region in the shapefile
	for line, name in geoms:
		for lin, name_neighbour in geoms:
			if line.touches(lin):
				neighbours.append(name_neighbour)

		regions[name] = neighbours
		counter += 1
		neighbours = []

	return(regions)
	




