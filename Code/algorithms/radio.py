from helpers import neighbour_set

def radio(data, order):

	for key in order:
		radio = 1
			
		neighb_station = neighbour_set(data, key)

		for i in range(7):
			if radio in neighb_station:
				radio += 1

			else:
				break
		key.radio = radio

	return data