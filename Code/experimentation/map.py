""" Map visualization

Uses shapefiles to create maps of countries on a plot.
And colours these maps according to station with colour function.

Sources:
- https://sensitivecities.com/so-youd-like-to-make-a-map-using-python-EN.html#.WwaE70jRA2w
- https://gis.stackexchange.com/questions/131716/plot-shapefile-with-matplotlib?rq=1
- https://chrishavlin.wordpress.com/2016/11/16/shapefiles-tutorial/

"""

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

	# Open shapefile for country and plot figure
	sf = shp.Reader(file_name)
	plt.figure()
	ax = plt.axes()

	# Add plot title with country name
	plt.title(country, fontsize=20)
	plt.text(x[0] + 5, y[0] + 1, algorithm + "\n" + order_choice, 
		ha='center', fontsize=15)

	# Initialize counter for number of region
	counter = 0
	name_list = []

	for i in list(sf.iterRecords()):

		# Append region names to name list 
		name_list.append(list(sf.iterRecords())[counter][number])
		counter += 1


	counter = 0

	for shape in list(sf.iterShapes()):
		
		# Get color for region
		color_value = name_list[counter]
		color = colours(final_regions)

		# Get dict with region and color for map
		color_regions = color[0]

		# Get dict with station and color for legend
		color_legend = color[1]

		# Check how many parts one region has
		nparts = len(shape.parts)

		# If region is made up of one part color whole part 
		if nparts == 1:
			
			polygon = Polygon(shape.points)
			patch = PolygonPatch(polygon, facecolor=color_regions[color_value])
			ax.add_patch(patch)

		# If more than one part then color every part of region the same color
		else:
			
			for ip in range(nparts):
				iO = shape.parts[ip]
				
				if ip < nparts-1:
					il = shape.parts[ip+1] - 1
				
				else:
					il = len(shape.points)

				polygon = Polygon(shape.points[iO:il+1])
				patch = PolygonPatch(polygon, facecolor=color_regions[color_value])
				ax.add_patch(patch)

		counter += 1

	# Add legend to plot 
	station_1 = mlines.Line2D([], [], color=color_legend["1"], marker="s", 
				fillstyle="full", label='Station 1', markersize=15)
	station_2 = mlines.Line2D([], [], color=color_legend["2"], marker="s", 
				fillstyle="full", label='Station 2', markersize=15)
	station_3 = mlines.Line2D([], [], color=color_legend["3"], marker="s", 
				fillstyle="full", label='Station 3', markersize=15)
	station_4 = mlines.Line2D([], [], color=color_legend["4"], marker="s", 
				fillstyle="full", label='Station 4', markersize=15)
	station_5 = mlines.Line2D([], [], color=color_legend["5"], marker="s", 
				fillstyle="full", label='Station 5', markersize=15)
	station_6 = mlines.Line2D([], [], color=color_legend["6"], marker="s", 
				fillstyle="full", label='Station 6', markersize=15)
	station_7 = mlines.Line2D([], [], color=color_legend["7"], marker="s", 
				fillstyle="full", label='Station 7', markersize=15)

	plt.legend(handles=[station_1, station_2, station_3, station_4, station_5, 
				station_6, station_7], shadow=True, fancybox=True, prop={'size': 12})

	# Scale to country coordinates
	plt.xlim(x)
	plt.ylim(y)
	plt.show()