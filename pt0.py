#imporrrtttsssss

from sklearn.cluster import KMeans
from sklearn.neighbors import LocalOutlierFactor
import numpy as np
#load data as a numpy array
data=np.loadtxt("inferences.txt",dtype=np.float64)
#create sklearn outlier factor object
outliers=LocalOutlierFactor(n_neighbors=25).fit_predict(data)
for line in data.readline():
    if outliers[line]==-1:
        data.pop(line)

#create KMeans clustering model based on data
kmeans = KMeans(n_clusters=5,random_state=0, n_init="auto").fit(data)

print(kmeans.cluster_centers_) 