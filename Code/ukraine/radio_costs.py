from data_structure import data_structure
from ukraine import country

regions = country()

final_regions = data_structure(regions)

def radio(regions):
	#count = {'1': 0, '2': 0, '3':0, '4':0}#, '5':0}#,#'6':0, '7':0 }

	kosten1 = {"1": 12, "2": 26, "3": 27, "4": 30}#, 37, 39, 41]
	kosten2 = {"1" : 19, "2": 20, "3": 21, "4" : 23}#, 36, 37, 38]
	kosten3 = {"1" : 16, "2": 17, "3": 31, "4": 33}#, 36, 56, 57]
	kosten4 = {"1": 3, "2": 34, "3" : 36, "4" : 39}#, 41, 43, 58]

	cost_regions = {"cost1": {}, "cost2": {}, "cost3": {}, "cost4": {}}

	for key in regions:
		radio = 1

		neighb_station = set()

		for neighbor in regions.get(key):
			neighb_station.add(neighbor.radio)		

		for i in range(7):
			
			if radio in neighb_station:
				
				radio += 1

			else:
				break
		
		minimum1 = min(kosten1, key = kosten1.get)

		print("min")
		print(minimum1)

		minimum2 = min(kosten2, key = kosten1.get)
		minimum3 = min(kosten3, key = kosten1.get)
		minimum4 = min(kosten4, key = kosten1.get)
		
		print("radio-1")
		print(radio - 1)
		if (minimum1 == (radio - 1)):
			key.radio = radio
			#count[str(radio)]+=1
		else:
			key.radio = minimum1
			#count[str(minimum)]+=1
			
	return regions

print(radio(final_regions))