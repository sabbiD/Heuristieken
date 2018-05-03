regions = [ [4, 2], [1, 4, 5, 6, 3], [2, 6], [1, 2, 5, 8, 7], [4, 2, 6, 9, 8], 
[2, 3, 5, 9], [4, 8, 11, 10], [4, 5, 7, 9, 11], [5, 6, 8, 11], [7, 11, 13, 17, 12],
[8, 9, 7, 10, 13, 18, 14], [10, 17, 16], [10, 11, 18, 17], [11, 13, 18, 19, 15], 
[14], [12, 17, 20], [10, 12, 16, 13, 18, 21, 20], [13, 17, 21, 19, 14, 11], 
[14, 18, 21, 22], [16, 17, 21, 25, 24], [17, 20, 25, 26, 22, 19, 18], [23, 19, 21, 26],
[22], [20, 25], [20, 21, 24, 16], [21, 25, 22] ]

# change array to correct format (0-25)
for i in range(len(regions)):
	for j in range(len(regions[i])):
		regions[i][j] -= 1


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

# Create Region Class
class Region:
	def __init__(self, index, neighbours = [], radio = 0):
		self.index = index
		self.neighbours = neighbours
		self.radio = radio
   
	def __str__(self):
		return ("{}: Neighbours: {} = Radio {}".format(self.index, self.neighbours, self.radio))

ukraine = []

# Create array with all Regions
for i in range (26):
	index = str(i)
	ukraine.append(Region(index))
	ukraine[i].neighbours = regions[i]

# Add radiostations to regions
def radio(index):

	neighbours = []
	radio_station = set()
	radio = 1

	# Create radiostation set
	for i in range(len(index.neighbours)):
		neighbours.append(index.neighbours[i])
		radio_station.add(ukraine[neighbours[i]].radio)
	
	# Add radios
	for i in range(7):
		if radio in radio_station:
			radio += 1
		else:
			break
	index.radio = radio
	return
	
# Add radios to Ukraine
for i in range(len(ukraine)):
	radio(ukraine[i])
	print(ukraine[i])







