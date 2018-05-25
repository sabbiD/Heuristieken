""" Plot function for histogram
	
	plot.py contains a function for loading a barchart displaying the cost distribution.
	Takes arguments from main.py.

"""

import numpy as np 
import matplotlib.pyplot as plt


def histogram(result, name, algorithm, choice, version):

	# Fail check
	if not result:
		print("No histogram could be made because there were no succesfull tries.")
	
	else:
		"{}.png".format(name)
		totals = []
		
		# Create list of costs
		for i in result:

			if i == 1:
				break
			else:
				totals.append(i.get(2))
		
		# Calculate average
		average = 0
		for number in totals:
			average += number
		average = average/len(totals)

		# Directions for plot, mapping costs and average
		plt.hist(totals)
		plt.axvline(average, color='k', linestyle='dashed', linewidth=1)
		plt.xlabel('Costs')
		plt.ylabel('Count')
		plt.title(algorithm + ' algorithm, ' + choice + ", " + version)
		plt.savefig("../Heuristieken/Results/{}.png".format(name))

		plt.show()