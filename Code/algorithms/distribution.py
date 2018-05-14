import csv

def distribution(score, costs):

	radio = []
	for key in score:

		if key == 0:
			break
		
		div = score.get(key)
		div = round((div/27)*100, 1)
		radio.append(div) 

	f = open('ukraine.csv', 'w')
	for i in range(50):

		dist = costs[1]

		set_random = radio

		f.writelines(str(costs) + "\n" + str(set_random)+ "\n")

	f.close()

	return radio





	
		
