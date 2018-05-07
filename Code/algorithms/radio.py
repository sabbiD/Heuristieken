def radio(regions):

	for key in regions:
		radio = 1

		print(key)
		
		neighb_station = set()


		for neighbor in regions.get(key):
			neighb_station.add(neighbor.radio)
		print(neighb_station)

		for i in range(7):
			if radio in neighb_station:
				radio += 1

			else:
				break
		key.radio = radio

	return regions
