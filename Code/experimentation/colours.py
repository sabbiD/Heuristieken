def colours(regions):
	colours = {"1": "#a6cee3", "2": "#1f78b4", "3": "#b2df8a", "4": "#f4cae4", "5": "#e6f5c9", "6": "#fb9a99", "7": "#fdbf6f"}

	region_colours = {}

	for key in regions:
		region_colours[key.index] = colours[str(key.radio)]
		
	return region_colours
