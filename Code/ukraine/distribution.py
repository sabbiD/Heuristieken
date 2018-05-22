import csv
from randomy import randomy
from data_structure import data_structure
from ukraine import country
from score import score
from costs import costs
from costs import distribution
import time



regions = country()
final_regions = data_structure(regions)


def compare(function, regions, iterations):
	start_time = time.time()
	fail = 0
	radio = {4:0, 5:0, 6:0, 7:0}

	all_scores = []
	all_costs = []
	all_amount = []
	all_even = []
	
	for i in range(iterations):
		print("Try no. {}".format(i))
		main_radio = function(regions)
		if main_radio == 1:
			fail+=1
		#print (random_radio)
		else:
			scores = score(main_radio)
			main_score = scores[0]
			amount = scores[1]
			radio[amount]+= 1
			all_amount.append(amount)
			print("Score: {}".format(main_score))
			all_scores.append(main_score)

			distributions = distribution(main_score)
			
			all_even.append(distributions)

			main_costs = (costs(main_score))
			print("Costs: {}".format(main_costs))
			all_costs.append(main_costs)



	
	print("--- %s seconds ---" % (time.time() - start_time))
	main_time = time.time() - start_time
	
	return all_scores, all_costs, all_amount, all_even, radio, main_time, fail












	
		
