import csv
from randomy import randomy
from data_structure import data_structure
from ukraine import country
from score import score
from costs import costs
from costs import distribution
import time

OUTPUT_CSV = 'ukraine.csv'

regions = country()

final_regions = data_structure(regions)


def compare():
	start_time = time.time()
	all_scores = []
	all_dist = []
	all_costs = []
	for i in range(100):
		print("Try no. {}".format(i))
		random_radio = randomy(final_regions)
		#print (random_radio)

		random_score = score(random_radio)
		print("Score: ")
		print(random_score)
		all_scores.append(random_score)

		random_distribution = distribution(random_score)
		print("Distribution: ")
		print(random_distribution)
		all_dist.append(random_distribution)

		random_costs = (costs(random_score))
		print("Costs: ")
		print(random_costs)
		all_costs.append(random_costs)

	# for i in range(100):
		
	# 	if all_costs[i] != 1:
	# 		print(min(all_costs[i]))

	print("--- %s seconds ---" % (time.time() - start_time))
	return random_score, random_distribution, random_costs

csv = compare()





def write_csv(outfile, compare):
	
	writer = csv.writer(outfile)
	writer.writerow(['Score', 'Distribution', 'Costs'])
	
	
	for i in range(100):
		writer.writerow(compare[i])



with open(OUTPUT_CSV, 'w', newline='') as output_file:
	write_csv(output_file, csv)

# write_csv(csv[0], csv[1], csv[2])







	
		
