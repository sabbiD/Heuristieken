# Team KGB, Radio Russa
# distribution.py contains a compare function that collects all the necessary results from the algorithm,
# later enabelling us to compare them with each other. Takes commandos from main.py

from score import score
from costs import costs
from costs import distribution
from depth_first import depth_first
from helpers import reset, random_order, ldo
import random
import time

def compare(algorithm, argument, regions, iterations, soort):

	fail = 0
	radio = {4:0, 5:0, 6:0, 7:0}

	# Create empty lists to store data
	all_scores = []
	all_costs = []
	all_amount = []
	all_even = []
	all_time = []
	
	# Start looping with the desired amount of iterations
	for i in range(iterations):
		start_time = time.time()

		reset(regions)

		# Order choice, random or ldo
		if soort == "random_order":
			argument = random_order(regions)
		elif soort == "ldo":
			argument = ldo(regions)

		# Call the desired algorithm	
		if algorithm == depth_first:
			main_radio = algorithm(regions, argument[0])
		
		else:
			main_radio = algorithm(regions, argument)

		# Account for fails
		if main_radio == 1:
			fail += 1

		else:

			# Count the radio stations
			scores = score(main_radio)

			main_score = scores[0]
			
			amount = scores[1]
			
			radio[amount] += 1
			
			# Append data to lists, including costs, distribution score and time
			all_amount.append(amount)

			all_scores.append(main_score)

			distributions = distribution(main_score)
			
			all_even.append(distributions)

			main_costs = costs(main_score)

			all_costs.append(main_costs)

			main_time = time.time() - start_time
			
			all_time.append(main_time)

	# Check for fails
	if not all_time:
		mean_time = 0
	else:
		mean_time = sum(all_time)/len(all_time)

	
	return all_scores, all_costs, all_amount, all_even, radio, mean_time, fail












	
		
