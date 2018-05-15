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
all_scores = []
all_dist = []
all_costs = []

def look():
	start_time = time.time()
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

	print("--- %s seconds ---" % (time.time() - start_time))
	return random_score, random_distribution, random_costs

csv = look()





# def write_csv(score, distribution, costs):
	
# 	f = open('ukraine.csv', 'w')
	
# 	f.writelines(["Score", "Distribution", "Costs"])
	
# 	for i in range(100):

# 		f.writelines(str(score) + "\n" + str(distribution)+ "\n" + str(costs))

# 	f.close()


# write_csv(csv[0], csv[1], csv[2])







	
		
