#imporrrtttsssss
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.neighbors import LocalOutlierFactor
import numpy as np

#load data as a numpy array
data=np.loadtxt("inferences.txt",dtype=np.float64)

#create sklearn outlier factor object
outliers=LocalOutlierFactor(n_neighbors=25).fit_predict(data)
np.delete(data,outliers)

#create KMeans clustering model based on data
kmeans = KMeans(n_clusters=5,random_state=0, n_init="auto").fit(data)

with open("outputs.out","w") as file:
    file.write(str(kmeans.cluster_centers_))