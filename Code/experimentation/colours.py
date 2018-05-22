def colours(regions):
	colours = {"1": "#b3e2cd", "2": "#fdcdac", "3": "#cbd5e8", "4": "#f4cae4", "5": "#e6f5c9", "6": "#fff2ae", "7": "#f1e2cc"}

	region_colours = {}

	for key in regions:
		region_colours[key.index] = colours[str(key.radio)]
		
	return region_colours
