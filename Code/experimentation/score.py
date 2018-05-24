# Team KGB, Radio Russa
# score.py contains a function that checks how many times each radio station was used
def score(regions):
	
	# Fail check
	if regions != 1:
	
		# Loop through regions
		for region in range(len(regions)):
			used_stations={"1": 0, "2": 0, "3": 0, "4":0, "5":0, "6": 0, "7": 0}
			used = set()
				
			# Create empty mother integer
			#mother = 0
			
			#Create empty set for the children (neighbours)
			#children = set()

			#Get the mother radio station from the set		
			for region in regions:
				
				region_station = region.radio

				# Get the children radio stations
				#for i in regions.get(key):

					#children.add(i.radio)

				#children = set()
				
				#if mother in children:
					#fail+=1
					
				#else:
				used.add(region_station)
				add = str(region_station)
				used_stations[add]+=1
		amount = max(used)
		return used_stations, amount
	else:
		return regions

	




