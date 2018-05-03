# voeg de huidige structuur toe aan path
import os, sys
directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "Code"))
sys.path.append(os.path.join(directory, "Code", "algorithms"))
sys.path.append(os.path.join(directory, "Code", "datastructuur"))
sys.path.append(os.path.join(directory, "Code", "datastructuur", "ukraine"))

# importeer de gebruikte structuur
from ukraine_structure import country
from data_structure import data_structure
from randomizer import randomizer
from radio import radio

def main():
    regions = country()
    data_structuur = data_structuur(regions)

    # probeer verschillende algoritmes
    # random
    random = randomize(data_strucuur)

    # simpele radiofunctie
    radio = radio(data_structuur)

    print("Random verdeling")
    print(random)
    print("Radio verdeling")
    print(radio)
    
if __name__ == "__main__":
    main()
