from data_structure import data_structure
from ukraine import country
from randomizer import randomizer
from radio import radio

regions = country()

final_regions = data_structure(regions)

random = radio(final_regions)

def colours(regions):
	colours = {"1": "#1f78b4", "2": "#b2df8a", "3": "#33a02c", "4": "#fb9a99", "5": "#f03b20"}

	region_colours = {}

	for key in regions:
		region_colours[index] = colours[str(key.radio)]
		
	return region_colours

#print(colours(random))

