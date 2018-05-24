import shapefile as shp
import numpy as np
import matplotlib.pyplot as plt
from shapely.geometry import Polygon
from descartes.patch import PolygonPatch
from colours import colours 
# from colours import regions
import fiona
from data_structure import data_structure
from country import country
from randomizer import randomizer
from radio import radio
import matplotlib.lines as mlines


regions = country("ukr_admbnda_adm1_q2_sspe_20171221.shp", "ADM1_PCODE")

final_regions = data_structure(regions)

random = randomizer(final_regions)
#print(random)

sf = shp.Reader("ukr_admbnda_adm1_q2_sspe_20171221.shp")
#print(fiona.open("ukr_admbnda_adm1_q2_sspe_20171221.shp")[0]['properties'])

plt.figure()
ax = plt.axes()
ax.set_title(list(sf.iterRecords())[0][12], fontsize=20)

counter = 0
name_list = []

for i in list(sf.iterRecords()):
	name_list.append(list(sf.iterRecords())[counter][4])
	counter += 1

#print(name_list)

counter = 0

for shape in list(sf.iterShapes()):
	# region_names = [feature['properties']['ADM1_PCODE'] for
	#      feature in fiona.open("ukr_admbnda_adm1_q2_sspe_20171221.shp")]
	#b = shape()
	#print(b)
	#print(shapes())

	#print(region_names)
	color_value = name_list[counter]
	color = colours(random)
	#print(color_value)
	#print(color[color_value])
	# color = list(color.values())
	#print(list(color))

	# check how many parts one region has
	nparts = len(shape.parts)

	#if region has one part color whole part 
	if nparts == 1:
		polygon = Polygon(shape.points)
		patch = PolygonPatch(polygon, facecolor=color[color_value], alpha=1.0, zorder=2)
		ax.add_patch(patch)

	# if more than one part than color every part the same color
	else:
		for ip in range(nparts):
			iO= shape.parts[ip]
			if ip < nparts-1:
				il = shape.parts[ip+1] - 1
			else: 
				il = len(shape.points)

			polygon = Polygon(shape.points[iO:il+1])
			patch = PolygonPatch(polygon, facecolor=color[color_value], alpha=1.0, zorder=2)
			ax.add_patch(patch)


	counter += 1

colours = {"1": "#b3e2cd", "2": "#fdcdac", "3": "#cbd5e8", "4": "#f4cae4", "5": "#e6f5c9", "6": "#fff2ae", "7": "#f1e2cc"}


# specific coordinates for ukraine
station_1 = mlines.Line2D([], [], color=colours["1"], marker="s", fillstyle="full", label='Station 1', markersize=15)
station_2 = mlines.Line2D([], [], color=colours["2"], marker="s", fillstyle="full", label='Station 2', markersize=15)
station_3 = mlines.Line2D([], [], color=colours["3"], marker="s", fillstyle="full", label='Station 3', markersize=15)
station_4 = mlines.Line2D([], [], color=colours["4"], marker="s", fillstyle="full", label='Station 4', markersize=15)
station_5 = mlines.Line2D([], [], color=colours["5"], marker="s", fillstyle="full", label='Station 5', markersize=15)
station_6 = mlines.Line2D([], [], color=colours["6"], marker="s", fillstyle="full", label='Station 6', markersize=15)
station_7 = mlines.Line2D([], [], color=colours["7"], marker="s", fillstyle="full", label='Station 7', markersize=15)

plt.legend(handles=[station_1, station_2, station_3, station_4, station_5, station_6, station_7], shadow=True, fancybox=True, prop={'size': 12})

plt.xlim(22, 41)
plt.ylim(43, 53)
plt.show()
