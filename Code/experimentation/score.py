""" Score function

	score.py contains a function that checks how many times each radio station was used

"""
def score(regions):
	
	# Fail check
	if regions != 1:
	
		# Loop through regions, create empty dict for storing the usage of stations and set for the max use
		for region in range(len(regions)):
			used_stations={"1": 0, "2": 0, "3": 0, "4":0, "5":0, "6": 0, "7": 0}
			used = set()
				
			#Get the radio station from the list of regions		
			for region in regions:
				region_station = region.radio	
				
				# Add station to set and dict
				used.add(region_station)
				add = str(region_station)
				used_stations[add]+=1
		
		# Amount keeps track of how many stations were used per region (4, 5, 6 or 7)
		amount = max(used)
		return used_stations, amount
	else:
		return regions

	




