#imporrrtttsssss
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.neighbors import LocalOutlierFactor
import numpy as np
import re
#load data as a numpy array
data=np.loadtxt("inferences.txt",dtype=np.float64)
#require moar digits
np.printoptions(precision=8)

#create sklearn outlier factor object
outliers=LocalOutlierFactor(n_neighbors=25).fit_predict(data)

#GET OUTTA HERE OUTLIERS
np.delete(data,outliers)


#create KMeans clustering model based on data
kmeans = KMeans(n_clusters=5,random_state=0, n_init="auto").fit(data)
np.set_printoptions(precision=10)
centers=kmeans.cluster_centers_
centers=np.around(centers, decimals=5)
centers=np.sort(centers,axis=0)

    




#format the output. 
#Probably not the best way to do it but if this code was really used on a drone I would just use the pure numpy array
#D1 code yapping
str=np.array2string(centers,formatter={'float_kind':lambda x: "%.5f" % x})
str=str.replace("["," ").replace("]"," ").replace("  ","")


