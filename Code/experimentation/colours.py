""" Colour scheme for the map 
	
	colours.py contains a colour scheme for the regions, where regions get coloured based on 
	their radio station.

"""


def colours(regions):
	
	colours = {"1": "#a6cee3", "2": "#b2df8a", "3": "#fb9a99", "4": "#fdbf6f", "5": "#1f78b4", "6": "#33a02c", "7": "#e31a1c"}

	# Create empty dict, to store regions and corresponding colour
	region_colours = {}

	for region in regions:
		region_colours[region.index] = colours[str(region.radio)]
		
	return region_colours, colours
