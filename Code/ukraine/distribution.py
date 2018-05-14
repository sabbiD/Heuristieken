import csv

def distribution(score):

	radio = []
	for key in score:

		if key == 0:
			break
		
		div = key #score.get(key)
		div = round((div/27)*100, 1)
		radio.append(div) 


	return radio

f = open('ukraine.csv', 'w')
for i in range(50):

	money = costs()
	dist = money[1]

	set_random = distribution(dist)

	f.writelines(str(money) + "\n" + str(set_random)+ "\n")

f.close()



	
		
