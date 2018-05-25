""" Cost and distribution function
	
	costs.py contains two functions, "costs" and "distribution". Both take one argument, namely the distribution
	of the radio stations. The cost function calculates the costs for the country, one for each scheme. 
	The distribution function calculates how evenly the radio stations are distributed. 

"""
 

def costs(score):
	
	# Check for fails
	if score == 1:
		return score
	
	# The four cost schemes
	cost1 = [12, 26, 27, 30, 37, 39, 41]
	cost2 = [19, 20, 21, 23, 36, 37, 38]
	cost3 = [16, 17, 31, 33, 36, 56, 57]
	cost4 = [3, 34, 36, 39, 41, 43, 58]

	costs = [cost1, cost2, cost3, cost4]

	# Empty dictionary for storing the final cost calculations + empty list for the used radio stations 
	money = {1 : 0, 2:0, 3:0, 4:0}
	radios = []
	
	counter = 1
	
	# Loop through cost schemes
	for scheme in costs:	
		price = 0		
		
		# Loop through regions
		for item in score:
			
			radio = score.get(item)
				
			radios.append(radio)
		
		# Loop that multiplies cheapest price with the station that is most used	
		for n in range(7):

			mini = min(scheme)
			
			maxi = max(radios)
			
			cash = mini * maxi
			
			price += cash
			
			# Remove station and price that is already used
			radios.remove(maxi)
			
			scheme.remove(mini)

		money[counter] = price
		counter += 1

	# Return the dictionary
	return(money)


def distribution(score, data):
	
	# Check for fails
	if score == 1:
		return score
	
	# Initiate variables to store the used stations ("use"), and the distribution score ("even")
	use = 0
	even = 0 
	
	# First loop, remember how many stations were used
	for item in score:
		value = score.get(item)
		if value != 0:
			use += 1
	
	length = len(data)
	
	# Calculate the ultimate usage
	ultimate = length/use
	
	# Second loop, calculate the difference between the ultimate usage and our usage
	for key in score:
		value = score.get(key)	
		
		if value == 0:
			continue
		
		else:
			
			diff = value - ultimate

			# If difference is positive: add to "even"
			if diff >= 0:
				even += diff
			
			# If difference is negative, transform to positive and add to "even"	
			else: 
				diff = (diff - diff) - diff
				even += diff
				

	return even










	
