# voeg de huidige structuur toe aan path
import os, sys
directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "Code"))
sys.path.append(os.path.join(directory, "Code", "classes"))
sys.path.append(os.path.join(directory, "code", "algoritmes"))

# importeer de gebruikte structuur
from datastructuur import DataStructuur
from bruteforce import randomize
from hillclimber import hill_climber
from breadthfirst import breadth_first
from genetic import genetic
from score import score
