from ukraine import country


regions = country()
#print(regions)
# ukraine = {'1': set(['2', '4']),
#          '2': set(['1', '3', '4', '5', '6']),
#          '3': set(['2', '6']),
#          '4': set(['1', '2', '5', '8', '7']),
#          '5': set(['2', '4', '6', '8', '9']),
#          '6': set(['2', '3', '5', '9'])
#          '7': set(['4', '8', '11', '10'])
#          '8': set(['4', '5', '7', '9', '11'])
#          }

# for i in ukraine:
# 	print (ukraine[i])

# regions = [ [4, 2], [1, 4, 5, 6, 3], [2, 6], [1, 2, 5, 8, 7], [4, 2, 6, 9, 8], 
# [2, 3, 5, 9], [4, 8, 11, 10], [4, 5, 7, 9, 11], [5, 6, 8, 11], [7, 11, 13, 17, 12],
# [8, 9, 7, 10, 13, 18, 14], [10, 17, 16], [10, 11, 18, 17], [11, 13, 18, 19, 15], 
# [14], [12, 17, 20], [10, 12, 16, 13, 18, 21, 20], [13, 17, 21, 19, 14, 11], 
# [14, 18, 21, 22], [16, 17, 21, 25, 24], [17, 20, 25, 26, 22, 19, 18], [23, 19, 21, 26],
# [22], [20, 25], [20, 21, 24, 16], [21, 25, 22] ]

"""
- For item in dictionary, set radio, 1-7, default is 1.
- Hypothetically: radio of item '1', is 1
- Check content all adjoining nodes.
- If a node contains radio station '1', break, and try radio station 2
- Repeat process with 2
- If no node has the station we are tryin to connect with item '1', set station.
- Proceed to next item

- Problem: how to give each item space for a value (radio station)

- Set afmaken
- Set in class lezen met loop
- Functie radio zender 
"""

class Region:
	def __init__(self, index, radio=0):
		self.index = index
		self.radio = radio

	def __str__(self):

		return ("Region {}: Radio {}".format(self.index
			, self.radio))


ukraine = {}
neighbours = []
provinces = set()

# Create array with all Regions
for key in regions:

	neighbour = regions.get(key)
	key = Region(key)
	provinces.add(key)
#print(provinces)
#print(regions)

# for key in regions:

# 	for buur in regions.get(key):

# 		if buur in provinces.index:
# 			ukraine[key] = 
# variabele maken van object of direct region objects meegeven als buur.
# eerst van alle regios een object maken.
# unique names for objects?

# for item in neighbour:
# 	#item = Region(item)

# 	if item == key.index:

# 	#ukraine[key] = item
# 	neighbours.append(item)

# ukraine[key] = neighbours
# input(ukraine)
# neighbours = []
	

#print(ukraine)
# Add radiostations to regions
def radio(index):

	#radio_list = []
	# radio van key vinden
	for key in index:
		radio = 0

		print(key)
		
		neighb_station = set()


		for buur in index.get(key):
			neighb_station.add(buur.radio)
		print(neighb_station)

		for i in range(7):
			if radio in neighb_station:
				#print("hoi")
				radio += 1
				#print(neighb_station)

			else:
				break
		#print(radio)
		key.radio = radio

# radio(ukraine)
# for key in ukraine:
# 	#print(key)

# 	for buur in ukraine.get(key):
		#print(buur)
