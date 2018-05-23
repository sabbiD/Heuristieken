import shapefile as shp
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
from shapely.geometry import Polygon
from descartes.patch import PolygonPatch
from colours import colours 
import fiona
from data_structure import data_structure

def make_map(final_regions, file_name, number, x, y, country, algorithm, order_choice):

	sf = shp.Reader(file_name)
	plt.figure()
	ax = plt.axes()

	# plot title with country name
	ax.set_title(country, fontsize=20)
	ax.set_title(algorithm, order_choice)

	# initialize counter for number of region
	counter = 0
	name_list = []

	for i in list(sf.iterRecords()):
		print(i)
		# append region names to list 
		name_list.append(list(sf.iterRecords())[counter][number])
		counter += 1


	counter = 0

	for shape in list(sf.iterShapes()):
		
		# get color for region 
		color_value = name_list[counter]
		color = colours(final_regions)
		color_regions = color[0]
		color_legend = color[1]

		# check how many parts one region has
		nparts = len(shape.parts)

		#if region is made up of one part color whole part 
		if nparts == 1:
			polygon = Polygon(shape.points)
			patch = PolygonPatch(polygon, facecolor=color_regions[color_value], alpha=1.0, zorder=2)
			ax.add_patch(patch)

		# if more than one part than color every part of region the same color
		else:
			for ip in range(nparts):
				iO= shape.parts[ip]
				if ip < nparts-1:
					il = shape.parts[ip+1] - 1
				else: 
					il = len(shape.points)

				polygon = Polygon(shape.points[iO:il+1])
				patch = PolygonPatch(polygon, facecolor=color_regions[color_value], alpha=1.0, zorder=2)
				ax.add_patch(patch)


		counter += 1

	# add legend to plot 
	station_1 = mlines.Line2D([], [], color=color_legend["1"], marker="s", fillstyle="full", label='Station 1', markersize=15)
	station_2 = mlines.Line2D([], [], color=color_legend["2"], marker="s", fillstyle="full", label='Station 2', markersize=15)
	station_3 = mlines.Line2D([], [], color=color_legend["3"], marker="s", fillstyle="full", label='Station 3', markersize=15)
	station_4 = mlines.Line2D([], [], color=color_legend["4"], marker="s", fillstyle="full", label='Station 4', markersize=15)
	station_5 = mlines.Line2D([], [], color=color_legend["5"], marker="s", fillstyle="full", label='Station 5', markersize=15)
	station_6 = mlines.Line2D([], [], color=color_legend["6"], marker="s", fillstyle="full", label='Station 6', markersize=15)
	station_7 = mlines.Line2D([], [], color=color_legend["7"], marker="s", fillstyle="full", label='Station 7', markersize=15)

	plt.legend(handles=[station_1, station_2, station_3, station_4, station_5, station_6, station_7], shadow=True, fancybox=True, prop={'size': 12})

	# scale to country coordinates
	plt.xlim(x)
	plt.ylim(y)
	plt.show()

