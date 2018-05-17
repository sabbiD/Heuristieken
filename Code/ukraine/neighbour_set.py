def neighbour_set(regions, key):

	neighb_station = set()
	for neighbor in regions.get(key):

		neighb_station.add(neighbor.radio)

	return neighb_station