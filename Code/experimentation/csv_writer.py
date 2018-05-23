import csv
# from distribution import compare
# from score import score
# from costs import costs
# from costs import distribution


def write_csv(compare, name):
	
	name = name + '.csv'
	score = compare[0]
	cost = compare[1]
	amount = compare[2]
	even = compare[3]
	used = compare[4]
	time = compare[5]
	fail = compare[6]

	lowest= []
	cheapest = []

	for i in cost:
		lowest_key = min(i, key=i.get)
		value = i.get(lowest_key)
		lowest.append(value)
		cheapest.append(lowest_key)
	
	# costs
	lowest_v = min(lowest)
	highest_v = max(lowest)
	mean_v = sum(lowest)/len(lowest)


	# distribution
	lowest_d = min(compare[3])
	highest_d = max(compare[3])
	mean_d = sum(compare[3])/len(compare[3])

	with open('../Heuristieken/Results/{}'.format(name), 'w') as csvfile:
		fieldnames = ['Try No', 'Score', 'Even Distribution Score', 'Cheapest Station', 'Costs', 'Amount of Stations',
		 'Lowest price', "Highest price", "Mean price", "Lowest distribution", "Highest distribution", "Mean distribution", 'Average Time', 'Fails', 'How many Stations']
		writer = csv.DictWriter(csvfile, fieldnames = fieldnames)

		writer.writeheader()
		for i in range(len(score)):
			writer.writerow({'Try No': i,'Score': score[i], 
				'Even Distribution Score': even[i], 
				'Cheapest Station': cheapest[i], 'Costs':lowest[i],
				 'Amount of Stations':amount[i]})
			
		
		writer.writerow({'Lowest price': lowest_v, "Highest price": highest_v, "Mean price": mean_v, "Lowest distribution": lowest_d, "Highest distribution": highest_d, "Mean distribution": mean_d, "Average Time": time, 'Fails': fail, 'How many Stations': used})



