import numpy as np 
import matplotlib.pyplot as plt
from randomy import randomy
from data_structure import data_structure
#from ukraine import country
# from score import score
from costs import costs
# from costs import distribution
from distribution import compare
import time

# regions = country()

# final_regions = data_structure(regions)

all_lists = compare()
totals = []
for i in all_lists[1]:

	if i == 1:
		print(i)
		break
	else:
		totals.append(i.get(2))


plt.hist(totals)
plt.show()