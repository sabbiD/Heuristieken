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
#from randomizer import randomizer
from randomy import randomy
from radio import radio
from greedy import greedy
from score import score
from costs import costs
from distribution import distribution
from map2 import make_map

def main():

    # ask user which country and create datastructure
    # add other shapefiles, add errorcheck (only 4 countries possible)
    print("Radio Russia attempts to create a distribution of radio stations for the provinces of the countries Ukraine, US, Russia and China.")
    choice = input("Please choose a country for which to create the datastructure: ")

    if (choice.lower() == "ukraine"):
        file_name = "ukr_admbnda_adm1_q2_sspe_20171221.shp"
    elif (choice.lower() == "us"):
        file_name = "bla"
    elif (choice.lower() == "russia"):
        file_name = "bla"
    elif (choice.lower() == "china"):
        file_name = "bla"
    else:
        print("This is not a valid country. Please choose from ukraine, us, russia or china")
        return

    # create data structure
    regions = country(file_name)
    data = data_structure(regions)
    print("Data structure created!")

    # ask user which algorithm they would like to run
    # run algorithms multiple times? ask how many iterations etc, maybe put in csv and visualize best option???
    # add other algorithms when done
    print("There are multiple algorithms to choose from: radio, random, greedy, depth-first,...")
    algorithm = input("which algorithm would you like to run? ")

    if (algorithm == "radio"):
        # simpele radiofunctie
        radios = radio(data)
        make_map(radios)

    elif (algorithm == "random"):
        random = randomy(data)
        make_map(random)

    elif (algorithm == "greedy"):
        greed = greedy(data)
        make_map(greed)

    else:
        print("error")
        return

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
