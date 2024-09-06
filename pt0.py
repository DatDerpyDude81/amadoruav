import geopandas
import re
input=open("inferences.txt","r")
WKT=[]
for line in input:
    line = re.sub(r'[\x00-\x1f]', '', line)
    WKT.append(f"Point ("+line+")")

geopandaData=geopandas.GeoSeries.from_wkt(WKT, index=None, crs=None, on_invalid='raise')
print(geopandaData)