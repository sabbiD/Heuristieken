from data_structure import data_structure
from ukraine import country

regions = country()

final_regions = data_structure(regions)

def radio(regions):
	count = {'1': 0, '2': 0, '3':0, '4':0}#, '5':0}#,#'6':0, '7':0 }

	for key in regions:
		radio = 1

		#print(key)
		
		neighb_station = set()


		for neighbor in regions.get(key):
			neighb_station.add(neighbor.radio)
		#print(neighb_station)
		

		for i in range(7):
			
			if radio in neighb_station:
				
				radio += 1

			else:
				break
		
		
		minimum = min(count, key = count.get)
		
		if (minimum == (radio - 1)):
			key.radio = radio
			count[str(radio)]+=1
		else:
			key.radio = minimum
			count[str(minimum)]+=1
		#print('key is {}'.format(key.radio))
	print(count)

	return regions

radio(final_regions)
