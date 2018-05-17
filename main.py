# voeg de huidige structuur toe aan path
import os, sys
directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "Code"))
sys.path.append(os.path.join(directory, "Code", "algorithms"))
sys.path.append(os.path.join(directory, "Code", "data_structuur"))
#print(os.path.abspath("ukr_admbnda_adm1_q2_sspe_20171221.shp")

# importeer de gebruikte structuur
from country import country
from data_structure import data_structure
from randomy import randomy
from radio import radio
from greedy import greedy
from score import score
from costs import costs
from distribution import distribution
from reset import reset
from helpers import ldo
from helpers import reset
from helpers import random_order
from map import make_map
from depth_first import dfs_recursive
def main():

    # ask user for country
    print("Radio Russia attempts to create a distribution of radio stations for the provinces of the countries Ukraine, US, Russia and China.")
    choice = input("Please choose a country for which to create the datastructure: ")

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

    # ask user which algorithm they would like to run
    print("There are multiple algorithms to choose from: radio, random, greedy, depth-first, depth-recursive")
    algorithm = input("which algorithm would you like to run? ")

    # while algorithm != "radio" or algorithm != "random" or algorithm != "greedy" or algorithm != "hill-climber" or algorithm != "depth-first":
    #     algorithm = input("This is not a valid algorithm. Please choose from radio, random, greedy, hill-climber or depth-first: ")


    # radio algorithm with either random order or ldo order
    if (algorithm == "radio"):
        
        order_choice = input("would you like to use a random order (random) or a largest degree ordering (ldo)?")

        # while order_choice != "random" or order_choice != "ldo":
        #     order_choice = input("This is not a valid order. Please enter random or ldo: ")

        if order_choice == "random":
            order = random_order(data)
        elif order_choice == "ldo":
            order = ldo(data)

        reset(data)
        radios = radio(order, data)
        make_map(radios, file_name, number, x, y)

    # random algorithm with 4, 5, 6, or 7 stations
    elif (algorithm == "random"):

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

        # run until a valid solution is found
        random = randomy(data, radios)

        while random == 1:
            reset(data)
            random = randomy(data, radios)
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
        greed = greedy(order, data)
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

        # new_final = dict(data)

        # # stack for regions leftover
        # for key in list(new_final):

        #     if len(new_final[key]) < 5:
        #         del new_final[key]

        # dfs_recursive(data, list(new_final.keys())[0])
        # dfs_recursive(data, list(data.keys())[0])
        dfs_recursive(data, order[0])
        print(data)
        make_map(data, file_name, number, x, y)


    # How do we show optimal costs etc?
    # score: check how many times failed, how many times not failed (if multiple iterations)
    answer = input("would you like to check the distribution and optimal cost scheme? (y/n) ")

    if (algorithm == "random" and answer == "y"):
        scoree = score(random)
        if (scoree[0] == 1):
            print("failed")
        else:
            kosten = costs(scoree[1])
            print("Kostenschema's: {}".format(kosten))
            verdeling = distribution(scoree[1],kosten)
            print("Verdeling: {}".format(verdeling))

    elif (algorithm == "radio" and answer == "y"):
        scoree = score(radios)
        if (scoree[0] == 1):
            print("failed")
        else:
            kosten = costs(scoree[1])
            print("Kostenschema's: {}".format(kosten))
            verdeling = distribution(scoree[1],kosten)
            print("Verdeling: {}".format(verdeling))

    elif (algorithm == "greedy" and answer == "y"):
        scoree = score(greed)
        if (scoree[0] == 1):
            print("failed")
        else:
            kosten = costs(scoree[1])
            print("Kostenschema's: {}".format(kosten))
            verdeling = distribution(scoree[1],kosten)
            print("Verdeling: {}".format(verdeling))

    else:
        print("error")
        return

if __name__ == "__main__":
    main()
