def score(regions):
	
	if regions != 1:
	
		for i in range(len(regions)):
			used_stations={"1": 0, "2": 0, "3": 0, "4":0, "5":0, "6": 0, "7": 0}
			used = set()
			score = regions

			fail = 0

			if score == 1:
				fail = 1
			else:
				
				# Create empty mother integer
				mother = 0
				#Create empty set for the children radio stations
				children = set()

				#Get the mother radiostation from the random set		
				for key in score:
					
					mother = key.radio

					# Get the children radio stations
					for i in score.get(key):

						children.add(i.radio)

					children = set()
					
					if mother in children:
						fail+=1
						
					else:
						used.add(mother)
						add = str(mother)
						used_stations[add]+=1
		amount = max(used)
		return used_stations, amount
	else:
		return regions

	




