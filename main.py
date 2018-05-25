""" Main

	 main.py is the main program for Radio Russia.
	 The first part allows a user to (via the terminal) choose a country and visualize 
	 the map for a certain algorithm.
	 In part 2, the user can run a certain number of iterations for this algorithm, 
	 and create a csv with the results. In addition, a plot with the cost distribution
	 will be shown. 
	 
"""

# Add current structure to path
import os, sys
directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "Code"))
sys.path.append(os.path.join(directory, "Code", "algorithms"))
sys.path.append(os.path.join(directory, "Code", "data_structuur"))
sys.path.append(os.path.join(directory, "Code", "experimentation"))
sys.path.append(os.path.join(directory, "Data"))

# Import the used structure
from country import country
from data_structure import data_structure
from randomy import randomy
from radio import radio
from greedy import greedy
from depth_first import dfs_recursive, depth_first
from hill_climber import hill_climber
from hill_climber_costs import hill_climber_costs
from distribution import compare
from helpers import ldo, reset, random_order
from map import make_map
from csv_writer import write_csv
from plot import histogram


def main():

	# Ask the user to choose a country
	print("Radio Russia attempts to create a distribution of radio stations for the provinces of the countries Ukraine, US, Russia and China.\nNote: russia takes a VERY long time")
	country_answer = input("Would you like to choose a country (y/n)? ").lower()

	while not (country_answer == "y" or country_answer == "n"):
		country_answer = input("This is not a valid option. Please choose from y (yes) or n (no): ").lower()

	while country_answer == "y":
		choice = input("\nPlease choose a country (ukraine, us, china, russia): ").lower()

		while not (choice == "ukraine" or choice == "us" or choice == "russia" 
			or choice == "china"):
			choice = input("This is not a valid country. Please choose from Ukraine, US, Russia or China: ").lower()

		# Create correct variables for data structure and map
		if (choice == "ukraine"):
			file_name = os.path.join(directory, "Data", 
				"ukr_admbnda_adm1_q2_sspe_20171221.shp")
			name = "ADM1_PCODE"
			number = 4
			x = [22, 41]
			y = [43, 53]

		elif (choice == "us"):
			file_name = os.path.join(directory, "Data", "cb_2016_us_state_500k.shp")     
			name = "STATEFP"
			number = 3
			x = [-130, -60]
			y = [25, 50]

		elif (choice == "russia"):
			file_name = os.path.join(directory, "Data", "RUS_adm1.shp")
			name = "ID_1"
			number = 3
			x = [15, 190]
			y = [35, 85]

		elif (choice == "china"):
			file_name = os.path.join(directory, "Data", "CHN_adm1.shp")
			name = "ID_1"
			number = 3
			x = [70, 135]
			y = [15, 60]

		# Create data structure
		regions = country(file_name, name)
		data = data_structure(regions, choice)

		# FIRST PART: 
		# ask user which algorithm they would like to run and visualize this in a map

		print("\nThere are multiple algorithms to choose from: radio, random, greedy, depth-first, hill-climber, hill-climber-costs")
		algorithm_answer = input("Would you like to run an algorithm (y/n)? ").lower()

		while not (algorithm_answer == "y" or algorithm_answer == "n"):
			algorithm_answer = input("This is not a valid option. Please choose from y (yes) or n (no): ").lower()

		while algorithm_answer == "y":
			algorithm = input("\nWhich algorithm would you like to run (radio, random, greedy, depth-first, hill-climber, hill-climber-costs)? ").lower()

			while not (algorithm == "radio" or algorithm == "random" 
				or algorithm == "greedy" or algorithm == "depth-first" or 
				algorithm == "hill-climber" or algorithm == "hill-climber-costs"):
				algorithm = input("This is not a valid option. Please choose from radio, random, greedy, depth-first, hill-climber or hill-climber-costs: ").lower()

			# Radio algorithm with either random order or ldo order
			if (algorithm == "radio"):

				order_choice = input("Would you like to use a random order (random) or a largest degree ordering (ldo)? ").lower()

				while not (order_choice == "random" or order_choice == "ldo"):
					order_choice = input("This is not a valid order. Please enter random or ldo: ").lower()

				if order_choice == "random":
					order = random_order(data)
				elif order_choice == "ldo":
					order = ldo(data)

				reset(data)
				radios = radio(data, order)
				make_map(radios, file_name, number, x, y, choice, algorithm,
				 order_choice)

			# Random algorithm with 4, 5, 6, or 7 stations
			elif (algorithm == "random"):

				amount_radios = input("With how many stations would you like to run the algorithm (4, 5, 6, 7)? ").lower()

				while not(amount_radios == "4" or amount_radios == "5" 
					or amount_radios == "6" or amount_radios == "7"):
					amount_radios = input("This is not a valid amount. Please enter 4, 5, 6 or 7: ").lower()

				if amount_radios == "4":
					radios = [1, 2, 3, 4]
				elif amount_radios == "5":
					radios = [1, 2, 3, 4, 5]
				elif amount_radios == "6":
					radios = [1, 2, 3, 4, 5, 6]
				elif amount_radios == "7":
					radios = [1, 2, 3, 4, 5, 6, 7]

				# Run until a valid solution is found
				random = randomy(data, radios)
				count = 1
				while random == 1:
					reset(data)
					random = randomy(data, radios)
					count += 1
				print("It took {} tries to create a valid distribution!".format(count))
				make_map(random, file_name, number, x, y, choice, algorithm, 
					amount_radios)

			# Greedy algorithm with random order or ldo order
			elif (algorithm == "greedy"):

				order_choice = input("Would you like to use a random order (random) or a largest degree ordering (ldo)? ").lower()

				while not(order_choice == "random" or order_choice == "ldo"):
					order_choice = input("This is not a valid order. Please enter random or ldo: ").lower()

				if order_choice == "random":
					order = random_order(data)
				elif order_choice == "ldo":
					order = ldo(data)

				reset(data)
				greed = greedy(data, order)
				make_map(greed, file_name, number, x, y, choice, algorithm, order_choice)

			# Depth first algorithm with random order or ldo order
			elif (algorithm == "depth-first"):
				order_choice = input("would you like to use a random order (random) or a largest degree ordering (ldo)? ").lower()

				while not(order_choice == "random" or order_choice == "ldo"):
					order_choice = input("This is not a valid order. Please enter random or ldo: ").lower()

				if order_choice == "random":
					order = random_order(data)
				elif order_choice == "ldo":
					order = ldo(data)

				reset(data)
				depth = depth_first(data, order[0])
				make_map(depth, file_name, number, x, y, choice, algorithm, order_choice)

			# Hill-climber algorithm with 4, 5, 6 or 7 radios
			elif (algorithm == "hill-climber"):

				amount_radios = input("With how many stations would you like to run the algorithm (4, 5, 6, 7)? ").lower()

				while not(amount_radios == "4" or amount_radios == "5" or amount_radios == "6" or amount_radios == "7"):
					amount_radios = input("This is not a valid amount. Please enter 4, 5, 6 or 7: ").lower()

				if amount_radios == "4":
					radios = [1, 2, 3, 4]
				elif amount_radios == "5":
					radios = [1, 2, 3, 4, 5]
				elif amount_radios == "6":
					radios = [1, 2, 3, 4, 5, 6]
				elif amount_radios == "7":
					radios = [1, 2, 3, 4, 5, 6, 7]

				hill = hill_climber(data, radios)
				count = 1
				success = "yes"

				# Run until a valid solution is found
				while hill == 1:
					hill = hill_climber(data, radios)
					count += 1

					# Break after 1000 iterations
					if count == 10000:
						print("In 1000 tries, no valid distribution could be made for {} radios".format(amount_radios))
						success = "no"
						break

				if success == "yes":
					print("It took {} tries to create a valid distribution!".format(count))
					make_map(hill, file_name, number, x, y, choice, algorithm, amount_radios)

			# Hill-climber algorithm that starts with a random valid solution,
			# and tries to optimize the costs
			elif (algorithm == "hill-climber-costs"):

				amount_radios = input("With how many stations would you like to run the algorithm (4, 5, 6, 7)? ").lower()

				while not(amount_radios == "4" or amount_radios == "5" or amount_radios == "6" or amount_radios == "7"):
					amount_radios = input("This is not a valid amount. Please enter 4, 5, 6 or 7: ").lower()

				if amount_radios == "4":
					radios = [1, 2, 3, 4]
				elif amount_radios == "5":
					radios = [1, 2, 3, 4, 5]
				elif amount_radios == "6":
					radios = [1, 2, 3, 4, 5, 6]
				elif amount_radios == "7":
					radios = [1, 2, 3, 4, 5, 6, 7]

				hill_costs = hill_climber_costs(data, radios)

				make_map(hill_costs, file_name, number, x, y, choice, algorithm, amount_radios)


			# SECOND PART: 
			# Run algorithm x times and write scores to csv for comparison.
			# Create histogram with cost distribution

			print("\nYou can now run multiple iterations for this algorithm and create a CSV with the results.")
			print("This will also create a histogram with the cost distribution.")
			score_answer = input("\nWould you like to run multiple iterations for this algorithm (y/n)? " ).lower()

			while not (score_answer == "y" or score_answer == "n"):
				score_answer = input("This is not a valid option. Please choose from y (yes) or n (no): ").lower()

			if score_answer == "y":

				# Ask for amount of iterations
				while True:
					try:
						iterations = int(input("How many iterations would you like to run? "))
					except ValueError:
						print("This is not a valid amount of iterations. Please enter an integer ")
						continue
					else:
						break

				# Ask for csv file name
				name = input("What is the csv file name? The output will be saved in the folder 'Results': ")

				# Random algorithm
				if (algorithm == "random"):
					type_choice = amount_radios
					type_algorithm = "random"
					result = compare(randomy, radios, data, iterations, type_algorithm)

				# Radio algorithm
				elif (algorithm == "radio"):
					type_choice = order_choice
					if order_choice == "random":
						type_algorithm = "random_order"
					else:
						type_algorithm = "ldo"
					result = compare(radio, order, data, iterations, type_algorithm)

				# Greedy algorithm
				elif algorithm == "greedy":
					type_choice = order_choice
					if order_choice == "random":
						type_algorithm = "random_order"
					else:
						type_algorithm = "ldo"
					result = compare(greedy, order, data, iterations, type_algorithm)

				# Depth-first algorithm
				elif algorithm == "depth-first":
					type_choice = order_choice
					if order_choice == "random":
						type_algorithm = "random_order"
					else:
						type_algorithm = "ldo"
					result = compare(depth_first, order, data, iterations, type_algorithm)

				# Hill-climber algorithm
				elif algorithm == "hill-climber":
					type_choice = amount_radios
					type_algorithm = "hill-climber"
					result = compare(hill_climber, radios, data, iterations, type_algorithm)

				# Hill-climber algorithm with costs
				elif algorithm == "hill-climber-costs":
					type_choice = amount_radios
					type_algorithm = "hill-climber"
					result = compare(hill_climber_costs, radios, data, iterations, type_algorithm)

				# Create CSV and histogram
				write_csv(result, name)
				histogram(result[1], name, algorithm, choice, type_choice)

			# Ask if user wants to try another algorithm
			algorithm_answer = input("\nWould you like to try another algorithm for this country (y/n) ")

			while not (algorithm_answer == "y" or algorithm_answer == "n"):
				algorithm_answer = input("This is not a valid option. Please choose from y (yes) or n (no): ").lower()

			# Ask if user wants to try another country
			if algorithm_answer == "n":
				country_answer = input("\nWould you like to try another country (y/n)? ")

				while not (country_answer == "y" or country_answer == "n"):
					country_answer = input("This is not a valid option. Please choose from y (yes) or n (no): ").lower()
					
	if country_answer == "n":
		print("\nThank you and goodbye! Kisses from KGB.\nP.S. We know where you live...")

if __name__ == "__main__":
	main()
