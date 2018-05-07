def costs(scoree):
	kosten1 = [12, 26, 27, 30, 37, 39, 41]
	kosten2 = [19, 20, 21, 23, 36, 37, 38]
	kosten3 = [16, 17, 31, 33, 36, 56, 57]
	kosten4 = [3, 34, 36, 39, 41, 43, 58]

	costs = [kosten1, kosten2, kosten3, kosten4]


	money = []

	radios = []


	for i in costs:
		moneyz = 0		
		for key in scoree:
			radio = scoree.get(key)
				
			radios.append(radio)
			

		for n in range(4):

			mini = min(i)
			
			maxi = max(radios)
			
			cash = mini * maxi
			
			moneyz += cash
			
			radios.remove(maxi)
			
			i.remove(mini)

		money.append(moneyz)

	return(money, list(scoree.values()))











	
