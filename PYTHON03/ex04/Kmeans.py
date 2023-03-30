# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Kmeans.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: wluong <wluong@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/23 19:42:36 by wluong            #+#    #+#              #
#    Updated: 2023/03/30 16:20:03 by wluong           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from csvreader import CsvReader
import matplotlib.pyplot as plt
import numpy as np
import random
import sys
import time

class KmeansClustering:

    def __init__(self, max_iter=20, ncentroid=4):
        self.ncentroid = ncentroid # number of centroids
        self.max_iter = max_iter # number of max iterations to update the centroids
        self.centroids = [] # values of the centroids
        self.clusters = [[] for x in range(ncentroid)] # list of datas for each centroid
        if not isinstance(max_iter, int) or max_iter <= 0:
            raise TypeError
        if not isinstance(ncentroid, int) or ncentroid <= 0:
            raise TypeError

    def __euclidian_distance(self, centroid, point):
        """
        Calcul of the distance between a data and a centroid
        """
        dist = sum((x - y) ** 2 for x,y in zip(centroid, point))
        return dist

    def __mean_cluster(self, X):
        """
        Calcul of the mean between all data from a cluster
        """
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
        colors = ['r', 'g', 'b', 'y', 'm', 'c', 'k']

        fig = plt.figure() #Deuxieme figure avec visualisation des clusters
        ax = fig.add_subplot(projection='3d')

        random_data_index = random.sample(range(len(X)), self.ncentroid)
        for i in range(len(random_data_index)):
            self.centroids.append(X[random_data_index[i]])
        for iteration in range(self.max_iter):
            ax.cla()
            self.clusters = [[] for x in range(self.ncentroid)]
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
            for nb in range(len(self.centroids)):
                ax.scatter(self.centroids[nb][0], self.centroids[nb][1], self.centroids[nb][2],marker='^', c='black')
            for point in range(len(self.clusters)):
                p = np.array(self.clusters[point]).astype(float)
                ax.scatter(p[:,0], p[:,1], p[:,2], marker='o', c=colors[point])
            plt.draw()
            plt.pause(0.1)
        plt.show()


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
        planets = ['Asteroid Belt', 'Earth', 'Mars', 'Venus']
        predict = []
        for data in X:
            dist = self.__euclidian_distance(data, self.centroids[0])
            which_planet = (0, dist)
            for i in range(len(self.centroids)):
                new_dist = self.__euclidian_distance(data, self.centroids[i])
                if new_dist < which_planet[1]:
                    which_planet = (i, new_dist)
            predict.append(planets[which_planet[0]])
        return np.array(predict)

if __name__ == '__main__':

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

    kmeans = KmeansClustering(max_iter=int(max_it[1]), ncentroid=int(ncent[1])) #Algorithme de K-means Clustering
    md = np.delete(md, 0, axis=1).astype(float) #Suppression de l'index

    kmeans.fit(md) #Entrainement de l'algorithme
    a = [[176.05, 62.04, 0.5]]
    # print(kmeans.centroids)
    print(kmeans.predict(np.array(a)))
    # print(kmeans.predict(md))