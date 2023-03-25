# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Kmeans.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: wluong <wluong@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/23 19:42:36 by wluong            #+#    #+#              #
#    Updated: 2023/03/25 19:52:42 by wluong           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from csvreader import CsvReader
import matplotlib.pyplot as plt
import numpy as np

class KmeansClustering:

    def __init__(self, max_iter=20, ncentroid=5):
        self.ncentroid = ncentroid # number of centroids
        self.max_iter = max_iter # number of max iterations to update the centroids
        self.centroids = [] # values of the centroids

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
        for i in range(self.ncentroid):
            self.centroids[i] = X[np.random.randint(0, len(X))]
        
        for i in range(self.max_iter):
            self.classifications = {}
            for j in range(self.ncentroid):
                self.classifications[j] = []
            
            for x in X:
                distances = [np.linalg.norm(x - self.centroids[c]) for c in self.centroids]
                classification = distances.index(min(distances))
                self.classifications[classification].append(x)
            
            prev_centroids = list(self.centroids)
            
            for classification in self.classifications:
                self.centroids[classification] = np.average(self.classifications[classification], axis=0)
            
            optimized = True
            for c in self.centroids:
                original_centroid = prev_centroids[c]
                current_centroid = self.centroids[c]
                if np.sum((current_centroid - original_centroid) / original_centroid * 100.0) > self.tol:
                    optimized = False
            
            if optimized:
                break

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
        self.predictions = []
        for x in X:
            distances = [np.linalg.norm(x - self.centroids[c]) for c in self.centroids]
            classification = distances.index(min(distances))
            self.predictions.append(classification)
        return self.predictions

if __name__ == '__main__':


    kmeans = KmeansClustering()
    colors = ['r', 'g', 'b', 'c', 'm', 'y', 'k']

    with CsvReader('./solar_system_census.csv', ',', True) as data:
        index = np.array(int(x[0]) for x in data.getdata())
        height = np.array(x[1] for x in data.getdata())
        weight = np.array(float(x[2]) for x in data.getdata())
        bone_density = [float(x[3]) for x in data.getdata()]
        # plt.scatter(index, height, c = 'r')
        # plt.show()
        # plt.scatter(index, weight, c = 'b')
        # plt.show()
        # plt.scatter(index, bone_density, c = 'g')
        # plt.show()
    kmeans.fit(height)
    for classification in kmeans.classifications:
        color = colors[classification]
        for featureset in kmeans.classifications[classification]:
            plt.scatter(featureset[0], featureset[1], marker='x', color=color, s=150, linewidths=5, zorder=10)
    
    for centroid in kmeans.centroids:
        plt.scatter(kmeans.centroids[centroid][0], kmeans.centroids[centroid][1], marker='o', color='k', s=150, linewidths=5)
    plt.show()