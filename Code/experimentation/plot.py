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


	plt.hist(totals)
	plt.xlabel('Costs')
	plt.ylabel('Count')
	plt.savefig("../Heuristieken/Results/{}.png".format(name))

	plt.show()