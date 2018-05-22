import csv
from randomy import randomy
from data_structure import data_structure
from score import score
from costs import costs
from costs import distribution
from randomy import randomy
from radio import radio
from greedy import greedy
from depth_first import depth_first
from hill_climber import hill_climber
from helpers import reset, random_order
import random
import time

def compare(algorithm, argument, regions, iterations, soort):

	fail = 0
	radio = {4:0, 5:0, 6:0, 7:0}

	all_scores = []
	all_costs = []
	all_amount = []
	all_even = []
	all_time = []
	
	for i in range(iterations):
		start_time = time.time()

		reset(regions)
		if soort == "random_order":
			argument = random_order(regions)
			
		if algorithm == depth_first:
			first = random.choice(argument)
			main_radio = algorithm(regions, argument[0])
		
		else:
			main_radio = algorithm(regions, argument)

		if main_radio == 1:
			fail += 1

		else:
			scores = score(regions)
			main_score = scores[0]
			amount = scores[1]
			radio[amount]+= 1
			all_amount.append(amount)

			all_scores.append(main_score)

			distributions = distribution(main_score)
			
			all_even.append(distributions)

			main_costs = (costs(main_score))

			all_costs.append(main_costs)

			main_time = time.time() - start_time
			all_time.append(main_time)

	mean_time = sum(all_time)/len(all_time)
	
	return all_scores, all_costs, all_amount, all_even, radio, mean_time, fail












	
		
