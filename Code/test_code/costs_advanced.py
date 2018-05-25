""" Linear and logarithmic cost function. 
	
	Functions to calculate the costs of the distribution with variable cost schemes.

"""
import math

kosten1 = [12, 26, 27, 30, 37, 39, 41]
kosten2 = [19, 20, 21, 23, 36, 37, 38]
kosten3 = [16, 17, 31, 33, 36, 56, 57]
kosten4 = [3, 34, 36, 39, 41, 43, 58]

costs = [kosten1, kosten2, kosten3, kosten4]


def costs_linear_decline(score):
	
	if score == 1:
		return score

	money = {1 : 0, 2:0, 3:0, 4:0}

	radios = []
	counter = 1
	for i in costs:
		moneyz = 0		
		for key in score:
			
			radio = score.get(key)
				
			radios.append(radio)

			# 1 unit goedkoper voor elk volgende van zelfde station
			cash = mini * maxi - ((maxi ^ 2 + maxi)/2)
			
			moneyz += cash
			
			radios.remove(maxi)
			
			i.remove(mini)

		money[counter]=moneyz
		counter += 1

	return(money)


def costs_log_decline(score):
	
	if score == 1:
		return score

	money = {1 : 0, 2:0, 3:0, 4:0}

	radios = []
	counter = 1
	for i in costs:
		moneyz = 0		
		for key in score:
			
			radio = score.get(key)
				
			radios.append(radio)

			for n in range(7):

			mini = min(i)
			
			maxi = max(radios)

			# add price of first station
			cash += mini 

			# add price of every following station which gets 10% cheaper
			for i in range(maxi - 2):
				new_price = mini * 0.9
				cash += new_price
				mini = new_price
			
			moneyz += cash
			
			radios.remove(maxi)
			
			i.remove(mini)

		money[counter]=moneyz
		counter += 1

	return(money)







