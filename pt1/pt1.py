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


#remove waypoints that are outside of the geofence
#why do I even have to do this
index=0
for x,y in waypointcoords:
    
    if geofence.contains(shapely.Point(x,y))==False:
        waypointcoords=np.delete(waypointcoords,index,0)
    index+=1






waypoint=shapely.Polygon(waypointcoords)

intersect=shapely.intersection(geofence,waypoint)


#If a vertice on the intersected polygon is on the geofence, then it will have 2 neighbors that are also on the geofence
#so we detect the "middle" vertice, keep it ,a delete the other 2 vertices, forming a smooth path around the geofence
coords=intersect.exterior.coords
ind=0
for coord in coords:
    if shapely.touches(geofence,shapely.Point(coord)):
        pass
        
    ind+=1


gx,gy=geofence.exterior.xy
plt.plot(gx,gy)
ix,iy=intersect.exterior.xy
plt.plot(ix,iy,"bo")





plt.show()
