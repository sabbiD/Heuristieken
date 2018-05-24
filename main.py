# voeg de huidige structuur toe aan path
import os, sys
directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "Code"))
sys.path.append(os.path.join(directory, "Code", "algorithms"))
sys.path.append(os.path.join(directory, "Code", "data_structuur"))
sys.path.append(os.path.join(directory, "Code", "experimentation"))
sys.path.append(os.path.join(directory, "Data"))

# importeer de gebruikte structuur
from country import country
from data_structure import data_structure
from randomy import randomy
from radio import radio
from greedy import greedy
from depth_first import dfs_recursive, depth_first
from hill_climber import hill_climber
from distribution import compare
from helpers import ldo, reset, random_order
from map import make_map
from csv_writer import write_csv
from plot import histogram

def main():

	# ask user for country
	print("Radio Russia attempts to create a distribution of radio stations for the provinces of the countries Ukraine, US, Russia and China.\nNote: russia takes a VERY long time")
	country_answer = input("Would you like to choose a country (y/n)? ").lower()

	while not (country_answer == "y" or country_answer == "n"):
		country_answer = input("This is not a valid option. Please choose from y (yes) or n (no): ").lower()

	while country_answer == "y":
		choice = input("\nPlease choose a country (ukraine, us, china, russia): ").lower()

		while not (choice == "ukraine" or choice == "us" or choice == "russia" or choice == "china"):
			choice = input("This is not a valid country. Please choose from Ukraine, US, Russia or China: ").lower()

		# create correct variables for data structure and map
		if (choice == "ukraine"):
			file_name = os.path.join(directory, "Data", "ukr_admbnda_adm1_q2_sspe_20171221.shp")
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

		# create data structure
		regions = country(file_name, name)
		data = data_structure(regions, choice)

		# FIRST PART: 
		# ask user which algorithm they would like to run and visualize this in a map

		print("\nThere are multiple algorithms to choose from: radio, random, greedy, depth-first, hill-climber")
		algorithm_answer = input("Would you like to run an algorithm (y/n)? ").lower()

		while not (algorithm_answer == "y" or algorithm_answer == "n"):
			algorithm_answer = input("This is not a valid option. Please choose from y (yes) or n (no): ").lower()

		while algorithm_answer == "y":
			algorithm = input("\nWhich algorithm would you like to run (radio, random, greedy, depth-first, hill-climber)? ").lower()

			while not (algorithm == "radio" or algorithm == "random" or algorithm == "greedy" or algorithm == "depth-first" or algorithm == "hill-climber"):
				algorithm = input("This is not a valid option. Please choose from radio, random, greedy, depth-first or hill-climber: ").lower()

			# radio algorithm with either random order or ldo order
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
				make_map(radios, file_name, number, x, y, choice, algorithm, order_choice)

			# random algorithm with 4, 5, 6, or 7 stations
			elif (algorithm == "random"):

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

				# run until a valid solution is found
				random = randomy(data, radios)
				count = 1
				while random == 1:
					reset(data)
					random = randomy(data, radios)
					count += 1
				print("It took {} tries to create a valid distribution!".format(count))
				make_map(random, file_name, number, x, y, choice, algorithm, amount_radios)

			# greedy algorithm with random order or ldo order
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

				while hill == 1:
					hill = hill_climber(data, radios)
					count += 1

					# 
					if count == 1000:
						print("In 1000 tries, no valid distribution could be made for {} radios".format(amount_radios))
						success = "no"
						break

				if success == "yes":
					print("It took {} tries to create a valid distribution!".format(count))
					make_map(hill, file_name, number, x, y, choice, algorithm, amount_radios)


			# SECOND PART: 
			# Run algorithm x times and write scores to csv for comparison.

			score_answer = input("\nWould you like to calculate the best scores for this algorithm (y/n) ?" ).lower()

			while not (score_answer == "y" or score_answer == "n"):
				score_answer = input("This is not a valid option. Please choose from y (yes) or n (no): ").lower()

			if score_answer == "y":

				while True:
					try:
						iterations = int(input("How many iterations would you like to run? "))
					except ValueError:
						print("This is not a valid amount of iterations. Please enter an integer ")
						continue
					else:
						break

				name = input("What is the csv file name? The output will be saved in the folder 'Results': ")

				if (algorithm == "random"):
					keuze_soort = amount_radios
					soort = "random"
					result = compare(randomy, radios, data, iterations, soort)

				elif (algorithm == "radio"):
					keuze_soort = order_choice
					if order_choice == "random":
						soort = "random_order"
					else:
						soort = "ldo"
					result = compare(radio, order, data, iterations, soort)

				elif algorithm == "greedy":
					keuze_soort = order_choice
					if order_choice == "random":
						soort = "random_order"
					else:
						soort = "ldo"
					result = compare(greedy, order, data, iterations, soort)

				elif algorithm == "depth-first":
					keuze_soort = order_choice
					if order_choice == "random":
						soort = "random_order"
					else:
						soort = "ldo"
					result = compare(depth_first, order, data, iterations, soort)

				elif algorithm == "hill-climber":
					keuze_soort = amount_radios
					soort = "hill-climber"
					result = compare(hill_climber, radios, data, iterations, soort)

				write_csv(result, name)
				histogram(result[1], name, algorithm, choice, keuze_soort)

			algorithm_answer = input("\nWould you like to try another algorithm for this country (y/n) ")

			while not (algorithm_answer == "y" or algorithm_answer == "n"):
				algorithm_answer = input("This is not a valid option. Please choose from y (yes) or n (no): ").lower()

			if algorithm_answer == "n":
				country_answer = input("\nWould you like to try another country (y/n)? ")

				while not (country_answer == "y" or country_answer == "n"):
					country_answer = input("This is not a valid option. Please choose from y (yes) or n (no): ").lower()
					
	if country_answer == "n":
		print("\nThank you and goodbye! Kisses from KGB.\nP.S. We know where you live...")

if __name__ == "__main__":
	main()
