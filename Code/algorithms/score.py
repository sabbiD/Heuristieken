def score(regions):
	for i in range(1):
		used_stations={"1": 0, "2": 0, "3": 0, "4":0, "5":0}

		fail = 0

		if regions == 1:
			fail = 1
		else:
			
			# Create empty mother integer
			mother = 0
			#Create empty set for the children radio stations
			children = set()

			#Get the mother radiostation from the random set		
			for key in regions:
				
				mother = key.radio
			
				# Get the children radio stations
				for i in regions.get(key):
					children.add(i.radio)

				children = set()
				
				if mother in children:
					fail+=1
					
				else:
					add = str(mother)
					used_stations[add]+=1
		return used_stations
		
	




