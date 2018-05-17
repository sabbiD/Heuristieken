# First we have to specify the problem:

# Initial State: The map all colored randomly.
# Successor Function (Transition Model): Change the color of a region.
# Goal Test: The map all colored such that two adjacent regions do not share a color.
# Cost Function: Assigns 1 to change the color of a region.
# Now that we have the specification of the problem, we have to choose the search algorithm to solve the problem. In this case "Hill Climbing".

# As we choose "Hill Climbing" we have to specify one more function (the objective function):

# Heuristic Function: Returns the number of adjacent regions that share the same color.
# Now that we have the problem formulated, we apply the "Hill Climbing" algorithm to try to minimize the heuristic function.

# As @Philippe Oliver said, you could have several problems using just "Hill Climbing" like:

# Local minimums.
# Flat local minimums

import random
from data_structure import data_structure
from ukraine import country

regions = country()

final_regions = data_structure(regions)

# initial state --> random

for key in final_regions:
	key.radio = random.choice(1,7)

print(final_regions)