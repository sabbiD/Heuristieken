# voeg de huidige structuur toe aan path
import os, sys
directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "Code"))
sys.path.append(os.path.join(directory, "Code", "algorithms"))
sys.path.append(os.path.join(directory, "Code", "data_structuur"))

# importeer de gebruikte structuur
from country import country
from data_structure import data_structure
from randomy import randomy
from radio import radio
from greedy import greedy
from depth_first import dfs_recursive
from hill_climber import hill_climber
from distribution import compare
# from score import score
# from costs import costs
# from distribution import distribution
from helpers import ldo, reset, random_order
from map import make_map
from csv_writer import write_csv

def main():

    # ask user for country
    print("Radio Russia attempts to create a distribution of radio stations for the provinces of the countries Ukraine, US, Russia and China.\nNote: russia takes a VERY long time")
    country_answer = input("Would you like to choose a country (y/n)? ")

    while country_answer == "y":

        choice = input("Please choose a country (ukraine, us, china, russia): ")

        # while choice is "ukraine" or choice is "us" or choice is "russia" or choice is "china":
        #     choice = input("This is not a valid country. Please choose from Ukraine, US, Russia or China: ")

        # create correct variables for data structure and map
        if (choice.lower() == "ukraine"):
            file_name = "ukr_admbnda_adm1_q2_sspe_20171221.shp"
            name = "ADM1_PCODE"
            number = 4
            x = [22, 41]
            y = [43, 53]

        elif (choice.lower() == "us"):
            file_name = "cb_2016_us_state_500k.shp"        
            name = "STATEFP"
            number = 3
            x = [-130, -60]
            y = [25, 50]

        elif (choice.lower() == "russia"):
            file_name = "RUS_adm1.shp"
            name = "ID_1"
            number = 3
            x = [15, 190]
            y = [35, 85]

        elif (choice.lower() == "china"):
            file_name = "CHN_adm1.shp"
            name = "ID_1"
            number = 3
            x = [70, 135]
            y = [15, 60]

        # create data structure
        regions = country(file_name, name)
        data = data_structure(regions)
        print("Data structure created!")

        # FIRST PART: 
        # ask user which algorithm they would like to run and visualize this in a map

        print("There are multiple algorithms to choose from: radio, random, greedy, depth-first, hill-climber")
        algorithm_answer = input("Would you like to run an algorithm (y/n)? ")

        while algorithm_answer == "y":


            algorithm = input("which algorithm would you like to run (radio, random, greedy, depth-first, hill-climber)? ")

            # while algorithm != "radio" or algorithm != "random" or algorithm != "greedy" or algorithm != "hill-climber" or algorithm != "depth-first":
            #     algorithm = input("This is not a valid algorithm. Please choose from radio, random, greedy, hill-climber or depth-first: ")

            # radio algorithm with either random order or ldo order
            if (algorithm == "radio"):
                
                order_choice = input("would you like to use a random order (random) or a largest degree ordering (ldo)? ")

                # while order_choice != "random" or order_choice != "ldo":
                #     order_choice = input("This is not a valid order. Please enter random or ldo: ")

                if order_choice == "random":
                    order = random_order(data)
                elif order_choice == "ldo":
                    order = ldo(data)

                reset(data)
                radios = radio(data, order)
                make_map(radios, file_name, number, x, y)

            # random algorithm with 4, 5, 6, or 7 stations
            elif (algorithm == "random"):

                amount_radios = input("With how many stations would you like to run the algorithm (4, 5, 6, 7)? ")

                # while amount != "4" or amount != "5" or amount != "6" or amount != "7":
                #     amount = input("This is not a valid amount. Please enter 4, 5, 6 or 7: ")

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
                make_map(random, file_name, number, x, y)

            # greedy algorithm with random order or ldo order
            elif (algorithm == "greedy"):

                order_choice = input("would you like to use a random order (random) or a largest degree ordering (ldo)?")

                # while order_choice != "random" or order_choice != "ldo":
                #     order_choice = input("This is not a valid order. Please enter random or ldo: ")

                if order_choice == "random":
                    order = random_order(data)
                elif order_choice == "ldo":
                    order = ldo(data)

                reset(data)
                greed = greedy(data, order)
                make_map(greed, file_name, number, x, y)

            elif (algorithm == "depth-first"):
                order_choice = input("would you like to use a random order (random) or a largest degree ordering (ldo)?")

                # while order_choice != "random" or order_choice != "ldo":
                #     order_choice = input("This is not a valid order. Please enter random or ldo: ")

                if order_choice == "random":
                    order = random_order(data)
                elif order_choice == "ldo":
                    order = ldo(data)

                reset(data)

                dfs_recursive(data, order[0])
                make_map(data, file_name, number, x, y)

            elif (algorithm == "hill-climber"):

                amount_radios = input("With how many stations would you like to run the algorithm (4, 5, 6, 7)?")

                # while amount != "4" or amount != "5" or amount != "6" or amount != "7":
                #     amount = input("This is not a valid amount. Please enter 4, 5, 6 or 7: ")

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
                while hill == 1:
                    reset(data)
                    hill = hill_climber(data, radios)
                    count += 1
                    if count == 10000:
                        print("No valid distribution could be made for {} radios".format(amount_radios))
                        break

                print("It took {} tries to create a valid distribution! {} radios were changed".format(count, hill[1]))
                make_map(hill[0], file_name, number, x, y)


            # SECOND PART: 
            # Run algorithm x times and write scores to csv for comparison.

            score_answer = input("Would you like to calculate the best scores for this algorithm (y/n) ?" )

            if score_answer == "y":
                iterations = int(input("How many iterations would you like to run? "))
                name = input("What is the csv file name? ")

                if (algorithm == "random"):
                    soort = "random"
                    result = compare(randomy, radios, data, iterations, soort)

                elif (algorithm == "radio"):
                    if order_choice == "random":
                        soort = "random"
                    else:
                        soort = "ldo"
                    result = compare(radio, order, data, iterations, soort)

                elif algorithm == "greedy":
                    if order_choice == "random":
                        soort = "random"
                    else:
                        soort = "ldo"
                    result = compare(greedy, order, data, iterations, soort)


                elif algorithm == "depth-first":
                    if order_choice == "random":
                        soort = "order"
                    else:
                        soort = "ldo"
                    result = compare(dfs_recursive, order, data, iterations, soort)

                elif algorithm == "hill-climber":
                    soort = "hill-climber"
                    result = compare(hill_climber, radios, data, iterations, soort)


                write_csv(result, name)

            algorithm_answer = input("Would you like to try another algorithm for this country (y/n) ")

            if algorithm_answer == "n":
                country_answer = input("Would you like to try another country (y/n)? ")

if __name__ == "__main__":
    main()
