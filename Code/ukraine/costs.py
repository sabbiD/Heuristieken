def costs(score):
	if score == 1:
		return score
	kosten1 = [12, 26, 27, 30, 37, 39, 41]
	kosten2 = [19, 20, 21, 23, 36, 37, 38]
	kosten3 = [16, 17, 31, 33, 36, 56, 57]
	kosten4 = [3, 34, 36, 39, 41, 43, 58]

	costs = [kosten1, kosten2, kosten3, kosten4]


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
			
			cash = mini * maxi
			
			moneyz += cash
			
			radios.remove(maxi)
			
			i.remove(mini)

		money[counter]=moneyz
		counter += 1

	return(money)#, list(score.values()))

def distribution(score):
	if score == 1:
		return score
	use = 0
	even = 0 
	for key in score:

		value = score.get(key)
		if value != 0:
			use+=1
	
	ultimate = round(27/use,1)
	
	
	for key in score:
		value = score.get(key)
		
		
		if value == 0:
			even += ultimate
		
		
		else:
			percent = round(27/value,1)
			diff = ultimate - percent

			
			if diff > 0:
				even+=diff
				
			else: 
				diff = (diff - diff) - diff
				even+=diff
				

	return even










	
