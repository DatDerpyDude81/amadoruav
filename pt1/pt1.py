import shapely
from shapely.ops import nearest_points
import numpy as np
import matplotlib.pyplot as plt
import json

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
    
    if geofence.contains(shapely.Point(x,y))==False and shapely.touches(geofence,shapely.Point(x,y))==False:
        waypointcoords=np.delete(waypointcoords,index,0)
        
    index+=1



waypoint=shapely.Polygon(waypointcoords)
qx,qy=waypoint.exterior.xy
plt.plot(qx,qy)
intersect=shapely.intersection(geofence,waypoint)

print(waypointcoords)

#detect the vertices of the intersection that also touch the geofence,add them to an array
coords=intersect.exterior.coords # type: ignore
#too lazy to use numpy
vert=[]
for coord in coords:
    x,y=coord
    if shapely.touches(geofence,shapely.Point(x,y)):
        plt.plot(x,y,"bo")

        vert.append([x,y])

waypoint=shapely.Polygon(waypointcoords)


#create snap reference
ref=shapely.Polygon(vert)

waypoint=shapely.snap(waypoint,ref,tolerance=1)
homepos=waypoint.exterior.coords[0]
homepos=list(homepos)
homepos.append(50)
#convert to qgroundcontrol json file

gx,gy=geofence.exterior.xy
plt.plot(gx,gy)
ix,iy=waypoint.exterior.xy
plt.plot(ix,iy)
plt.show()
data={
  "fileType": "Plan",
  "geoFence": {
    "circles": [],
    "polygons": [{"inclusion":True,
        "polygon":geofencecoords.tolist(),
        "version":1}],
    "version": 2
  },
  "groundStation": "QGroundControl",
  "mission": {"plannedHomePosition": homepos,
"vehicleType": 2,
"version": 2,
"cruiseSpeed": 15,
"firmwareType": 12,
"globalPlanAltitudeMode": 1,
"hoverSpeed": 15,
"items":[]},
  "rallyPoints": {
    "points": [],
    "version": 2
  },
  "version": 1
}
num=0

for coords in waypoint.exterior.coords:
    x,y=coords
    data["mission"]["items"].append(
        {
                "AMSLAltAboveTerrain": 100,
                "Altitude": 100,
                "AltitudeMode": 1,
                "autoContinue": True,
                "command": 16,
                "doJumpId": 29,
                "frame": 2,
                "params": [
                    #what
                    0,
                    0,
                    0,
                    None,
                    x,
                    y,
                    100
                ],
                "type": "SimpleItem",

        }



    )
    num+=1

with open("navigate.plan","w") as file:
    file.write(json.dumps(data))


