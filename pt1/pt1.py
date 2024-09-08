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


#redmvoe waypoints that are outside of the geofence
index=0
for x,y in waypointcoords:
    
    if geofence.contains(shapely.Point(x,y))==False:
        waypointcoords=np.delete(waypointcoords,index,0)
    index+=1






waypoint=shapely.Polygon(waypointcoords)

intersect=shapely.intersection(geofence,waypoint)

x,y=intersect.exterior.xy
plt.plot(x,y,"r")

gx,gy = geofence.exterior.xy
wx,wy= waypoint.exterior.xy
plt.plot(gx,gy,"b")
gx,gy = geofence.exterior.xy
wx,wy= waypoint.exterior.xy
plt.plot(gx,gy)
plt.plot(wx,wy)

plt.show()
