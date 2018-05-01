import shapefile as shp
import matplotlib.pyplot as plt

sf = shp.Reader("ukr_admbnda_adm1_q2_sspe_20171221.shp")

plt.figure()
for shape in sf.shapeRecords():
	x = [i[0] for i in shape.shape.points[:]]
	y = [i[1] for i in shape.shape.points[:]]
	plt.plot(x,y)
plt.show()