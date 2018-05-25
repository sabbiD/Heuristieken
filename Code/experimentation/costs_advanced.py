""" Linear and logarithmic cost function. 
	
	Functions to calculate the costs of the distribution of stations with variable cost schemes.

"""

import math


cost1 = [12, 26, 27, 30, 37, 39, 41]
cost2 = [19, 20, 21, 23, 36, 37, 38]
cost3 = [16, 17, 31, 33, 36, 56, 57]
cost4 = [3, 34, 36, 39, 41, 43, 58]

costs = [cost1, cost2, cost3, cost4]



def costs_linear_decline(score):
	
	if score == 1:
		return score

	# Empty dictionary for storing the final cost calculations + empty list for the used radio stations
	money = {1 : 0, 2:0, 3:0, 4:0}

	radios = []
	counter = 1
	
	# Loop through cost schemes
	for scheme in costs:
		
		price = 0		
		
		# Loop through regions
		for key in score:
			
			radio = score.get(key)
				
			radios.append(radio)

			# With 
			cash = mini * maxi - ((maxi ^ 2 + maxi)/2)
			
			price += cash
			
			radios.remove(maxi)
			
			scheme.remove(mini)

		money[counter]=moneyz
		counter += 1

	return(money)


def costs_log_decline(score):
	
	if score == 1:
		return score

	# Empty dictionary for storing the final cost calculations + empty list for the used radio stations
	money = {1 : 0, 2:0, 3:0, 4:0}

	radios = []
	counter = 1
	
	# Loop through cost schemes
	for scheme in costs:
		
		price = 0		
		
		for key in score:
			
			radio = score.get(key)
				
			radios.append(radio)

			for n in range(7):

			mini = min(scheme)
			
			maxi = max(radios)

			# Add price of first station
			cash += mini 

			# Add price of every following station which gets 10% cheaper
			for i in range(maxi - 2):
				new_price = mini * 0.9
				cash += new_price
				mini = new_price
			
			price += cash
			
			radios.remove(maxi)
			
			scheme.remove(mini)

		money[counter]=moneyz
		counter += 1

	return(money)







