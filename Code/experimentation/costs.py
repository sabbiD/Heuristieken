# Team KGB, Radio Russa
# costs.py contains two functions, "costs" and "distribution". Both take one argument, namely the distribution
# of the radio stations. The cost function calculates the costs for the country, one for each scheme. 
# The distribution function calculates how evenly the radio stations are distributed.  

def costs(score):
	
	# Check for fails
	if score == 1:
		return score
	
	# The four cost schemes
	kosten1 = [12, 26, 27, 30, 37, 39, 41]
	kosten2 = [19, 20, 21, 23, 36, 37, 38]
	kosten3 = [16, 17, 31, 33, 36, 56, 57]
	kosten4 = [3, 34, 36, 39, 41, 43, 58]

	costs = [kosten1, kosten2, kosten3, kosten4]

	# Empty dictionary for storing the final cost calculations + empty list for the used radio stations 
	money = {1 : 0, 2:0, 3:0, 4:0}
	radios = []
	
	counter = 1
	
	# Loop through cost schemes
	for i in costs:	
		price = 0		
		
		# Loop through regions
		for item in score:
			
			radio = score.get(item)
				
			radios.append(radio)
		
		# Loop that multiplies cheapest price with the station that is most used	
		for n in range(7):

			mini = min(i)
			
			maxi = max(radios)
			
			cash = mini * maxi
			
			price += cash
			
			# Remove station and price that is already used
			radios.remove(maxi)
			
			i.remove(mini)

		money[counter] = price
		counter += 1

	# Return the dictionary
	return(money)


def distribution(score):
	
	# Check for fails
	if score == 1:
		return score
	
	# Initiate variables to store the used stations ("use"), and the distribution score "even"
	use = 0
	even = 0 
	
	# First loop, store how many stations were used
	for item in score:
		value = score.get(item)
		if value != 0:
			use += 1
	
	# Calculate the ultimate even percentage
	ultimate = round(27/use,1)
	
	# Second loop, calculate the difference between the ultimate percentage and our percentage
	for key in score:
		value = score.get(key)	
		
		if value == 0:
			continue
		
		else:
			percent = round(27/value,1)
			diff = ultimate - percent

			# If difference is positive: add to "even"
			if diff > 0:
				even += diff
			
			# If difference is negative, transform to positive and add to "even"	
			else: 
				diff = (diff - diff) - diff
				even += diff
				
	# Even contains the accumulated differences between the ultimate percentages and our percentages
	return even










	
