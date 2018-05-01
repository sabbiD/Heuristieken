from ukraine import country


regions = country()

class Region:
	def __init__(self, index, radio=0):
		self.index = index
		self.radio = radio

	def __str__(self):

		return ("Region {}: Radio {}".format(self.index
			, self.radio))

alle_buren = []
temp = {}
final = {}

# make dict for every region with objects as values
for key in regions:
	classy = Region(key)
	temp[key] = classy

# make region objects for every neighbour
for values in regions.values():
	new = []
	for buur in values:
		for sleutel in temp:
			if buur == sleutel:
				buur = temp.get(sleutel)
				new.append(buur)
	alle_buren.append(new)

counter = 0

# make final dict with key(region) as object and values(neighbours) as objects
for value in temp.values():
	final[value] = alle_buren[counter]
	counter += 1

# Add radiostations to regions
def radio(index):

	for key in index:
		radio = 1

		print(key)
		
		neighb_station = set()


		for buur in index.get(key):
			neighb_station.add(buur.radio)
		print(neighb_station)

		for i in range(7):
			if radio in neighb_station:
				radio += 1

			else:
				break
		key.radio = radio

radio(final)

for key in final:
	print("key is", end="")
	print(key)
	for buur in final.get(key):
		print(buur)

