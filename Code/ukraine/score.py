# from ukraine import country
# #from randomizer import randomizer
# from data_structure import data_structure
# #from radio_costs import radio_costs
# from radio import radio

# regions = country()

# final_regions = data_structure(regions)

# regions = radio(final_regions)

def score(regions):
	for i in range(1):
		used_stations={"1": 0, "2": 0, "3": 0, "4":0, "5":0, "6": 0, "7": 0}

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
					add = str(mother)
					used_stations[add]+=1

		return fail, used stations
		
#print(score(final_regions))
	




