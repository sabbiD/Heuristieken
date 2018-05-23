import numpy as np 
import matplotlib.pyplot as plt

def histogram(result, name):
	"{}.png".format(name)
	totals = []
	for i in result:

		if i == 1:
			break
		else:
			totals.append(i.get(2))
	average = 0
	for number in totals:
		average += number
	average = average/len(totals)

	plt.hist(totals)
	plt.axvline(average, color='k', linestyle='dashed', linewidth=1)
	plt.xlabel('Costs')
	plt.ylabel('Count')
	plt.savefig("../Heuristieken/Results/{}.png".format(name))

	plt.show()