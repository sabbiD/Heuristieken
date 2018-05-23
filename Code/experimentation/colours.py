def colours(regions):
	colours = {"1": "#a6cee3", "2": "#b2df8a", "3": "#fb9a99", "4": "#fdbf6f", "5": "#1f78b4", "6": "#33a02c", "7": "#e31a1c"}

	region_colours = {}

	for key in regions:
		region_colours[key.index] = colours[str(key.radio)]
		
	return region_colours, colours
