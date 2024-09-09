import shapely
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
    
    if geofence.contains(shapely.Point(x,y))==False:
        waypointcoords=np.delete(waypointcoords,index,0)
    index+=1



waypoint=shapely.Polygon(waypointcoords)

intersect=shapely.intersection(geofence,waypoint)



#detect the vertices of the intersection that also touch the geofence,add them to an array
coords=intersect.exterior.coords
#too lazy to use numpy
vert=[]
for coord in coords:
    x,y=coord
    if shapely.touches(geofence,shapely.Point(x,y)):
        plt.plot(x,y,"bo")
        vert.append([x,y])
#create snap reference
ref=shapely.Polygon(vert)

#shrink the snap ref so its 25 feet away from vertices
xs = list(ref.exterior.coords.xy[0])
ys = list(ref.exterior.coords.xy[1])
#find x and y centers
x_center = 0.5 * min(xs) + 0.5 * max(xs)
y_center = 0.5 * min(ys) + 0.5 * max(ys)
#find smallest corner
min_corner = shapely.Point(min(xs), min(ys))
center = shapely.Point(x_center, y_center)
#find scale of the object, so buffering behaves predictably
shrink_distance = center.distance(min_corner)*0.02
shrunkref = ref.buffer(-shrink_distance)

x,y=shrunkref.exterior.xy
plt.plot(x,y,"bo")


#snap waypoint polygon onto vertices
waypoint=shapely.snap(waypoint,shrunkref,tolerance=1)

homepos=waypointcoords.tolist()[0]
homepos.append(50)
#convert to qgroundcontrol json file

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
"type":1,
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
                "command": 0,
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


