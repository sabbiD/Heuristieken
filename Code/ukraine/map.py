import fiona
from shapely.geometry import Point, Polygon, MultiPoint, MultiPolygon
from shapely.prepared import prep
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.collections import PatchCollection
from descartes import PolygonPatch
from matplotlib.colors import BoundaryNorm
from matplotlib.cm import ScalarMappable


shapefilename = 'ukr_admbnda_adm1_q2_sspe_20171221'
shp = fiona.open(shapefilename+'.shp')
coords = shp.bounds
shp.close()

w, h = coords[2] - coords[0], coords[3] - coords[1]
extra = 0.01

m = Basemap(
    projection='tmerc', ellps='WGS84',
    lon_0=np.mean([coords[0], coords[2]]),
    lat_0=np.mean([coords[1], coords[3]]),
    llcrnrlon=coords[0] - extra * w,
    llcrnrlat=coords[1] - (extra * h), 
    urcrnrlon=coords[2] + extra * w,
    urcrnrlat=coords[3] + (extra * h),
    resolution='i',  suppress_ticks=True)


_out = m.readshapefile(shapefilename, name='ukraine', drawbounds=False, color='none', zorder=2)

# set up a map dataframe
df_map = pd.DataFrame({
    'poly': [Polygon(xy) for xy in m.ukraine],
    'region_name': [region['ADM1_PCODE'] for region in m.ukraine_info]})
df_map['area_m'] = df_map['poly'].map(lambda x: x.area)
#df_map['area_km'] = df_map['area_m'] / 100000

# breaks = [0.] + [4., 24., 64., 135.] + [1e20]
# def self_categorize(entry, breaks):
#     for i in range(len(breaks)-1):
#         if entry > breaks[i] and entry <= breaks[i+1]:
#             return i
#     return -1
# df_map['jenks_bins'] = df_map.hood_hours.apply(self_categorize, args=(breaks,))

# labels = ['Never been\nhere']+["> %d hours"%(perc) for perc in breaks[:-1]]

# Or, you could always use Natural_Breaks to calculate your breaks for you:
# from pysal.esda.mapclassify import Natural_Breaks
# breaks = Natural_Breaks(df_map[df_map['hood_hours'] > 0].hood_hours, initial=300, k=3)
# df_map['jenks_bins'] = -1 #default value if no data exists for this bin
# df_map['jenks_bins'][df_map.hood_count > 0] = breaks.yb
# 
# jenks_labels = ['Never been here', "> 0 hours"]+["> %d hours"%(perc) for perc in breaks.bins[:-1]]

def custom_colorbar(cmap, ncolors,**kwargs):    
    """Create a custom, discretized colorbar with correctly formatted/aligned labels.
    
    cmap: the matplotlib colormap object you plan on using for your graph
    ncolors: (int) the number of discrete colors available
    labels: the list of labels for the colorbar. Should be the same length as ncolors.
    """
    from matplotlib.colors import BoundaryNorm
    from matplotlib.cm import ScalarMappable
        
    # norm = BoundaryNorm(range(0, ncolors), cmap.N)
    # mappable = ScalarMappable(cmap=cmap, norm=norm)
    # mappable.set_array([])
    # mappable.set_clim(-0.5, ncolors+0.5)
    # colorbar = plt.colorbar(mappable, **kwargs)
    # colorbar.set_ticks(np.linspace(0, ncolors, ncolors+1)+0.5)
    # colorbar.set_ticklabels(range(0, ncolors))
    # #colorbar.set_ticklabels(labels)
    # return colorbar

figwidth = 14
fig = plt.figure(figsize=(figwidth, figwidth*h/w))
ax = fig.add_subplot(111, frame_on=False)

cmap = plt.get_cmap('Blues')
# draw neighborhoods with grey outlines
df_map['patches'] = df_map['poly'].map(lambda x: PolygonPatch(x, ec='#111111', lw=.8, alpha=1., zorder=4))
pc = PatchCollection(df_map['patches'], match_original=True)
# apply our custom color values onto the patch collection
# cmap_list = [cmap(val) for val in (df_map.jenks_bins.values - df_map.jenks_bins.values.min())/(
#                   df_map.jenks_bins.values.max()-float(df_map.jenks_bins.values.min()))]
pc.set_facecolor('#ff3232')
ax.add_collection(pc)

#Draw a map scale
m.drawmapscale(coords[0] + 0.08, coords[1] + -0.01,
    coords[0], coords[1], 10.,
    fontsize=16, barstyle='fancy', labelstyle='simple',
    fillcolor1='w', fillcolor2='#555555', fontcolor='#555555',
    zorder=5, ax=ax,)

# ncolors+1 because we're using a "zero-th" color
#cbar = custom_colorbar(cmap, ncolors= 7) #labels=jenks_labels, shrink=0.5)
#cbar.ax.tick_params(labelsize=16)

fig.suptitle("Ukraine", fontdict={'size':24, 'fontweight':'bold'}, y=0.92)
#ax.set_title("Using location data collected from my Android phone via Google Takeout", fontsize=14, y=0.98)
#qax.text(1.35, 0.04, "Collected from 2012-2014 on Android 4.2-4.4\nGeographic data provided by data.seattle.gov", 
#    ha='right', color='#555555', style='italic', transform=ax.transAxes)
#ax.text(1.35, 0.01, "BeneathData.com", color='#555555', fontsize=16, ha='right', transform=ax.transAxes)

plt.savefig('ukraine.png', dpi=100, frameon=True) #bbox_inches='tight', pad_inches=0, facecolor='#F2F2F2')
plt.show()
