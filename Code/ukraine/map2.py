import shapefile as shp
import numpy as np
import matplotlib.pyplot as plt
from shapely.geometry import Polygon
from descartes.patch import PolygonPatch
from colours import colours 
import fiona
from kajsa_search import kajsa_search
from data_structure import data_structure
from ukraine import country
from sebile_search import final_regions

#regions = country()
#final_regions = data_structure(regions)

start = list(final_regions.keys())[0]
depth = kajsa_search(final_regions, start)


def make_map(final_regions):

	sf = shp.Reader("ukr_admbnda_adm1_q2_sspe_20171221.shp")
	#print(fiona.open("ukr_admbnda_adm1_q2_sspe_20171221.shp")[0]['properties'])

	plt.figure()
	ax = plt.axes()

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
		color = colours(final_regions)
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

	# specific coordinates for ukraine
	plt.xlim(22, 41)
	plt.ylim(43, 53)
	plt.show()


