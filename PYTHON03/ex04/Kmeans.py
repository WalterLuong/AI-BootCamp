# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Kmeans.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: wluong <wluong@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/23 19:42:36 by wluong            #+#    #+#              #
#    Updated: 2023/03/28 20:56:40 by wluong           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from csvreader import CsvReader
import matplotlib.pyplot as plt
import numpy as np
import random

class KmeansClustering:

    def __init__(self, max_iter=20, ncentroid=5):
        self.ncentroid = ncentroid # number of centroids
        self.max_iter = max_iter # number of max iterations to update the centroids
        self.centroids = [] # values of the centroids
        # self.clusters= [[],[],[],[]] # list of datas for each centroid
        self.clusters = [[] for x in range(4)]

    def __euclidian_distance(self, centroid, point):
        dist = sum((x - y) ** 2 for x,y in zip(centroid, point))
        return dist

    def __mean_cluster(self, X):
        mean = []
        for i in range(len(X[0])):
            mean[i] = sum(X[:,i]) / len(X)
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
                for j in range(len(self.centroids)):
                    self.centroids[i] = self.__mean_cluster(self.clusters[i])


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

if __name__ == '__main__':
    kmeans = KmeansClustering()
    # colors = ['r', 'g', 'b', 'c', 'm', 'y', 'k']
    with CsvReader('./solar_system_census.csv', ',', True) as data:
        md = np.array(data.getdata())
    md = np.delete(md, 0, axis=1).astype(float)
    # print(md[:,0])
    centroids = random.sample(range(len(md)), 4)
    
    kmeans.fit(md)
    print(kmeans.clusters[0])
    # print(kmeans.clusters[1])
    # print(kmeans.clusters[2])
    # print(kmeans.clusters[3])
    a = np.array(kmeans.clusters[0]).astype(float)
    b = np.array(kmeans.clusters[1]).astype(float)
    c = np.array(kmeans.clusters[2]).astype(float)
    d = np.array(kmeans.clusters[3]).astype(float)

    print("Centroid = " + str(kmeans.centroids[0]))

    cl1 = np.array(kmeans.centroids[0]).astype(float)
    cl2 = np.array(kmeans.centroids[1]).astype(float)
    cl3 = np.array(kmeans.centroids[2]).astype(float)
    cl4 = np.array(kmeans.centroids[3]).astype(float)

    fig = plt.figure()

    ax = fig.add_subplot(projection='3d')
    # ax.scatter(md[:,0], md[:,1], md[:,2], marker='^')
    ax.scatter(cl1[0], cl1[1], cl1[2], marker='*', c='g')
    ax.scatter(cl2[0], cl2[1], cl2[2], marker='*', c='g')
    ax.scatter(cl3[0], cl3[1], cl3[2], marker='*', c='g')
    ax.scatter(cl4[0], cl4[1], cl4[2], marker='*', c='g')
    ax.scatter(a[:,0], a[:,1], a[:,2], marker='o', c='r')
    ax.scatter(b[:,0], b[:,1], b[:,2], marker='o', c='b')
    ax.scatter(c[:,0], c[:,1], c[:,2], marker='o', c='y')
    ax.scatter(d[:,0], d[:,1], d[:,2], marker='o', c='g')

    plt.title('Habitants du systeme solaire')
    plt.xlabel('Height')
    plt.ylabel('Weight')
    ax.set_zlabel('Bone Density')
    plt.show()