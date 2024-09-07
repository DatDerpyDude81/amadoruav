import numpy
from sklearn.cluster import KMeans
import numpy as np

data=np.loadtxt("inferences.txt",dtype=np.float64)

kmeans = KMeans(n_clusters=5,random_state=0, n_init="auto").fit(data)

print(kmeans.cluster_centers_) 