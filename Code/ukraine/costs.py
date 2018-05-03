from score import score


kostenA = [12, 26, 27, 30, 37, 39, 41]
kostenB = [19, 20, 21, 23, 36, 37, 38]
kostenC = [16, 17, 31, 33, 36, 56, 57]
kostenD = [3, 34, 36, 39, 41, 43, 58]

costs = [kostenA, kostenB, kostenC, kostenD]


money = []


x = score()
radios = []


for i in costs:
	moneyz = 0		
	for key in x:
		radio = x.get(key)
			
		radios.append(radio)
		


	for n in range(4):

		mini = min(i)
		
		maxi = max(radios)
		

		cash = mini * maxi
		
		moneyz += cash
		
		
		radios.remove(maxi)
		
		i.remove(mini)

	money.append(moneyz)

print(money)









	
