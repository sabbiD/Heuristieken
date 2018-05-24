# Team KGB, Radio Russa
# radio.py contains a simple home-made function to create a distribution of
# radio stations.

from helpers import neighbour_set


def radio(data, order):

	for region in order:
		radio = 1
			
		# Set with neighbouring radios
		neighb_station = neighbour_set(data, region)

		# Start with option 1, if option is in neighbour set, increment option
		for i in range(7):
			if radio in neighb_station:
				radio += 1

			else:
				break

		# Region gets remaining option
		region.radio = radio

	return data