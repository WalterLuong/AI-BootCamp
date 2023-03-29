# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Kmeans.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: wluong <wluong@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/23 19:42:36 by wluong            #+#    #+#              #
#    Updated: 2023/03/29 02:09:25 by wluong           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from csvreader import CsvReader
import matplotlib.pyplot as plt
import numpy as np
import random
import sys

class KmeansClustering:

    def __init__(self, max_iter=20, ncentroid=4):
        self.ncentroid = ncentroid # number of centroids
        self.max_iter = max_iter # number of max iterations to update the centroids
        self.centroids = [] # values of the centroids
        # self.clusters= [[],[],[],[]] # list of datas for each centroid
        self.clusters = [[] for x in range(4)]
        if not isinstance(max_iter, int) or max_iter <= 0:
            raise TypeError
        if not isinstance(ncentroid, int) or ncentroid <= 0:
            raise TypeError

    def __euclidian_distance(self, centroid, point):
        dist = sum((x - y) ** 2 for x,y in zip(centroid, point))
        return dist

    def __mean_cluster(self, X):
        mean = [0, 0, 0]
        for i in range(len(X[0])):
            for j in range(len(X)):
                mean[i] += X[j][i]
        mean[0] /= len(X)
        mean[1] /= len(X)
        mean[2] /= len(X)
        return mean
    
    def fit(self, X):
        """
        Run the K-means clustering algorithm.
        For the location of the initial centroids, random pick ncentroids from the dataset.
        Args:
        -----
        X: has to be an numpy.ndarray, a matrice of dimension m * n.
        Return:
        -------
        None.
        Raises:
        -------
        This function should not raise any Exception.
        """
        random_data_index = random.sample(range(len(X)), 4)
        for i in range(len(random_data_index)):
            self.centroids.append(X[random_data_index[i]])
        for iteration in range(self.max_iter):
            self.clusters = [[] for x in range(4)]
            for data in X:
                dist = self.__euclidian_distance(data, self.centroids[0])
                cluster = (0, dist)
                for i in range(len(self.centroids)):
                    new_dist = self.__euclidian_distance(data, self.centroids[i])
                    if new_dist < cluster[1]:
                        cluster = (i, new_dist)
                self.clusters[cluster[0]].append(data)
            for j in range(len(self.clusters)):
                self.centroids[j] = self.__mean_cluster(self.clusters[j])


    def predict(self, X):
        """
        Predict from wich cluster each datapoint belongs to.
        Args:
        -----
        X: has to be an numpy.ndarray, a matrice of dimension m * n.
        Return:
        -------
        the prediction has a numpy.ndarray, a vector of dimension m * 1.
        Raises:
        -------
        This function should not raise any Exception.
        """
        return np.array(self.clusters)

if __name__ == '__main__':

    kmeans = KmeansClustering(30) #Algorithme de K-means Clustering
    if len(sys.argv) != 4:
        print("You need 4 arguments.")
        exit(1)
    filepath = sys.argv[1].split('=')
    ncent = sys.argv[2].split('=')
    max_it = sys.argv[3].split('=')
    if not len(filepath) == 2 and len(ncent) == 2 and len(max_it) == 2:
        print("Bad parameters in argv")
        exit(1)
    if not filepath[0] == 'filepath':
        print("Bad parameters in argv for filepath")
        exit(1)
    if not ncent[0] == 'ncentroid':
        print("Bad parameters in argv for ncentroid")
        exit(1)
    else:
        try:
            int(ncent[1])
        except:
            print("Bad parameter for ncentroid")
            exit(1)
    if not max_it[0] == 'max_iter':
        print("Bad parameters in argv for max_iter")
        exit(1)
    else:
        try:
            int(max_it[1])
        except:
            print("Bad parameter for max_iter")
            exit(1)



    try:
        with CsvReader(filepath[1], ',', True) as data:
            md = np.array(data.getdata()) #Récupération des données
    except:
        print("Can't open the file: ", filepath[1])
        exit(1)

    md = np.delete(md, 0, axis=1).astype(float) #Suppression de l'index

    kmeans.fit(md) #Entrainement de l'algorithme


    a = np.array(kmeans.clusters[0]).astype(float) #Cluster 1
    b = np.array(kmeans.clusters[1]).astype(float) #Cluster 2
    c = np.array(kmeans.clusters[2]).astype(float) #Cluster 3
    d = np.array(kmeans.clusters[3]).astype(float) #Cluster 4

    cl1 = np.array(kmeans.centroids[0]).astype(float) #Centroid 1
    cl2 = np.array(kmeans.centroids[1]).astype(float) #Centroid 2
    cl3 = np.array(kmeans.centroids[2]).astype(float) #Centroid 3
    cl4 = np.array(kmeans.centroids[3]).astype(float) #Centroid 4

    fig = plt.figure() #Premiere figure, sans visualisation des clusters
    ax2 = fig.add_subplot(projection='3d')
    ax2.scatter(md[:,0], md[:,1], md[:,2], marker='o', c='b')
    plt.show()

    fig = plt.figure() #Deuxieme figure avec visualisation des clusters
    ax = fig.add_subplot(projection='3d')
    ax.scatter(cl1[0], cl1[1], cl1[2], marker='^', c='black')
    ax.scatter(cl2[0], cl2[1], cl2[2], marker='^', c='black')
    ax.scatter(cl3[0], cl3[1], cl3[2], marker='^', c='black')
    ax.scatter(cl4[0], cl4[1], cl4[2], marker='^', c='black')
    ax.scatter(a[:,0], a[:,1], a[:,2], marker='o', c='r')
    ax.scatter(b[:,0], b[:,1], b[:,2], marker='o', c='b')
    ax.scatter(c[:,0], c[:,1], c[:,2], marker='o', c='y')
    ax.scatter(d[:,0], d[:,1], d[:,2], marker='o', c='g')
    plt.title('Habitants du système solaire')
    plt.xlabel('Height')
    plt.ylabel('Weight')
    ax.set_zlabel('Bone Density')
    plt.show()
    print(np.array(kmeans.predict(md)))