from ukraine import country
from randomizer import randomizer
from data_structure import data_structure

regions = country()

final_regions = data_structure(regions)

def score():
	for i in range(1):
		used_stations={"1": 0, "2": 0, "3": 0, "4":0}

		score = randomizer(final_regions)

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
					add = str(mother)
					used_stations[add]+=1
		return used_stations
		
	




