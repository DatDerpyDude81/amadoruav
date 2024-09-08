import shapely
import numpy as np
import matplotlib.pyplot as plt


#load file
data=np.loadtxt("pt1/navigate.txt",dtype=np.float64)
geofenceindex=int(data[0][0])
waypointindex=int(data[0][1])

geofencecoords=data[1:geofenceindex]

waypointcoords=data[geofenceindex:waypointindex+geofenceindex]


geofence=shapely.Polygon(geofencecoords)
waypoint=shapely.Polygon(waypointcoords)

gx,gy = geofence.exterior.xy
wx,wy= waypoint.exterior.xy


for x,y in np.nditer((wx,wy)):
    

plt.plot(gx,gy)
plt.plot(wx,wy)
plt.show()
