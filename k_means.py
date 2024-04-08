
import numpy
import random
import math

# Home of the main algorithm

class K_means:
    def __init__(self, k:int, data: numpy.ndarray):
        self.k = k
        self.data = data
        self.baricentres = []
        self.data[0][len(self.data[0])] = 'clusters'
        for index, line in enumerate(range(1, len(self.data))):          
            line[len(line)] = 0

    def rand_sample(self):
        rand_samples = []
        rand_samples_indexes = []

        for _ in range(self.k):
            rand_index = random.randint(0, len(self.data))
            rand_samples_indexes.append(rand_index)
            rand_samples.append(self.data[rand_index])
        
        return rand_samples, rand_samples_indexes
    
    @staticmethod
    def euclidian_distance(a_point_coords, b_point_coords) -> int:
        return math.sqrt(sum((a_coord - b_coord)**2 for (a_coord, b_coord) in (a_point_coords, b_point_coords)))

    def closest_point_to(self, point):
        euclidistances = [] 
        for line in self.data:
            euclidistances.append([line[0]], self.euclidian_distance(point[1:], line[1:]))

        return min(euclidistances, key=lambda x: x[1])

    def get_clusters(self):
        clustered_data = []
        for _ in range(self.k):
            clustered_data.append([])

        for line in self.data:
            clustered_data[line[-1]].append(line)

        return numpy.ndarray(clustered_data)
    
    def mean_clusters(self, clusters):
        means = []
        for cluster in clusters:
            means.append(numpy.mean(cluster, axis=0))
        self.baricentres.append(means)

    def get_cluster_variance(self)
        pass

    def fit(self):
        pass