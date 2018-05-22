from data_structure import data_structure
from ukraine import country

regions = country()

final_regions = data_structure(regions)

def radio_even(regions):
	count = {'1': 0, '2': 0, '3':0, '4':0}#, '5':0}#,#'6':0, '7':0 }

	for key in regions:
		radio = 1
		new_radio = 1

		neighb_station = set()


		for neighbor in regions.get(key):
			neighb_station.add(neighbor.radio)		

		for i in range(7):
			
			if radio in neighb_station:
				
				new_radio += 1

			else:
				break
		
		minimum = min(count, key = count.get)
		
		if (minimum == (radio)):
			key.radio = new_radio
			count[str(radio)]+=1
		else:
			key.radio = minimum
			count[str(minimum)]+=1

	return regions

x = radio_even(final_regions)

for key in x:
	print("key {}".format(key.radio))

	for buur in x.get(key):
		print(buur.radio)
