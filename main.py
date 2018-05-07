# voeg de huidige structuur toe aan path
import os, sys
directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "Code"))
sys.path.append(os.path.join(directory, "Code", "algorithms"))
sys.path.append(os.path.join(directory, "Code", "data_structuur"))

# importeer de gebruikte structuur
from ukraine import country
from data_structure import data_structure
from randomizer import randomizer
from radio import radio
from score import score
from costs import costs
from distribution import distribution

def main():

    # ask user which country and create datastructure
    # add other shapefiles, add errorcheck (only 4 countries possible)
    choice = input("Please choose a country (ukraine): ")

    if (choice.lower() == "ukraine"):
        file_name = "ukr_admbnda_adm1_q2_sspe_20171221.shp"
    else:
        print("error")
        return

    regions = country(file_name)
    data = data_structure(regions)


    # ask user to run algorithm
    algorithm = input("which algorithm (radio, randomizer) would you like to run? ")

    if (algorithm == "radio"):
            # simpele radiofunctie
        radios = radio(data)
        print("Radio verdeling:")
        print(radios)

    elif (algorithm == "randomizer"):
        random = randomizer(data)
        print("Random verdeling:")
        print(random)

    else:
        print("error")
        return

    answer = input("would you like to check the distribution and optimal cost scheme? (y/n) ")

    if (algorithm == "randomizer" and answer == "y"):
        scoree = score(random)
        kosten = costs(scoree)
        print("Kostenschema's: {}".format(kosten))
        verdeling = distribution(scoree)
        print("Verdeling: {}".format(verdeling))

    elif (algorithm == "radio" and answer == "y"):
        scoree = score(radios)
        kosten = costs(scoree)
        print("Kostenschema's: {}".format(kosten))
        verdeling = distribution(scoree)
        print("Verdeling: {}".format(verdeling))

    else:
        print("error")
        return

if __name__ == "__main__":
    main()
