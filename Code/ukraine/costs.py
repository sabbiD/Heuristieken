from score import score


kostenA = [12, 26, 27, 30, 37, 39, 41]
kostenB = [19, 20, 21, 23, 36, 37, 38]
kostenC = [16, 17, 31, 33, 36, 56, 57]
kostenD = [3, 34, 36, 39, 41, 43, 58]

costs = [kostenA, kostenB, kostenC, kostenD]

money = []


x = score()
radios = []


#print(radios)

for i in costs:

	for key in x:
		radio = x.get(key)
		radios.append(radio)
	
	for price in i:
		cash = 0
		
		if not radios:
			break
		
		high = max(radios)
		radios.remove(high)

		low = min(i)
		i.remove(low)

		cash += high * low

	money.append(cash)

print(money)






	
